import csv

def read_csv_file(fname):
    packing_mode_dict = {}

    with open(fname, 'r') as f:
        reader = csv.reader(f, delimiter=';')
        next(reader) # skip header

        for row in reader:
            template_name = row[1]
            packing_mode = row[4].lower()

            if packing_mode in packing_mode_dict:
                packing_mode_dict[packing_mode].add(template_name)
            else:
                packing_mode_dict[packing_mode] = set(template_name)

    return packing_mode_dict;

def generate_psql_script(packing_mode_dict):
    when_clauses = ""

    for packing_mode, template_names in packing_mode_dict.items():
        names = convert_set_to_psql_any_array(template_names)
        w = "WHEN bt.name = {} THEN '\"{}\"'::jsonb".format(names, packing_mode)
        when_clauses += padded_when_clause(w)

    path = "'{order_packing_mode,default_value}'"

    return """
    UPDATE
        booking_templates bt
    SET
	fields_schema = jsonb_set(
            fields_schema,
            {},
	    CASE
            {}
            END,
	    FALSE
	)
    WHERE
	bt.deleted_at IS NULL
	AND bt.format = 2;
    """.format(path, when_clauses)

def convert_set_to_psql_any_array(s):
    tmp = ','.join([repr(x) for x in s])
    return "ANY(ARRAY[{}])".format(tmp)

def padded_when_clause(when_clause):
    return '\n                ' + when_clause + '\n';

if __name__ == '__main__':
    packing_mode_dict = read_csv_file('default_packing_mode.csv')
    psql_script = generate_psql_script(packing_mode_dict)
    print(psql_script)
