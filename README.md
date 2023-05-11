# Usage
```console
root:~$ python generate_default_packing_mode_migration_script.py
```
# Result
```sql
    UPDATE
        booking_templates bt
    SET
	fields_schema = jsonb_set(
            fields_schema,
            '{order_packing_mode,default_value}',
	    CASE
            
                WHEN bt.name = ANY(ARRAY['PUD Domestic','Multileg','OD Export Container','Container Single Leg','Copy - Single Task',' ','FCL EXPORT (Integrated)','Multileg - Import/Export','Container Multileg','2 leg with empty leg 1.2','2 leg with empty leg 1.1','1 leg with empty leg 1','two-legs-second-empty','Copy - FCL Export','L','Multileg - Export (Leg1 Empty)','Container-template','Point To Point (Containers)','2 Legs - 1 MT - Allow insert','Template 3 legs with empty leg 1','Copy - Multileg - Import/Export','t','nina US 2 leg 1 empty','MARKEM','l','Container Multi-Leg','Copy - Multileg - Import (Leg2 Empty)','Single Leg DMPI','Export- Container Multi-Leg','FCL Export Dept to Terminal','FCL Import','Single Leg- Domestic & Cargo','C','FCL Export','nina 2 leg 1 empty','mt-464','Copy - Multileg (Test) - Import / Export','g','Copy - 2 leg with empty leg 2','o','Copy - 2 leg with empty leg 1','Multileg - Import (Leg2 Empty)','3 leg with empty leg 3','two-legs','Copy - 3 leg with empty leg 1','OD Import Container','Copy - 3 leg with empty leg 2','FCL Multi Leg','Clarke Cargo P2P LCL','FCL IMPORT (Integrated)','vessel','Copy - Multi Task','micheal_prod_default_template','Container Movement Export','Copy - 3 leg with none empty leg','a','Copy - 2 leg with none empty leg','Vallen SG multi-leg','n','r','Multileg (Test) - Import / Export','Copy - FCL Export Dept to Terminal','mt-320-demo','truly_default_template','QA-Container-Template','template 1 leg within empty leg','QCM','Copy - Multileg - Import / Export','QA 2 leg 1 empty','Container Multi-Leg Export','-','Nanhai Export LCL Corp Sender','u','Test QA full required fields','Container Movement Import','new_t1','M','Clarke Cargo FCL','Single Leg - Domestic & Cargo','Multileg  - Export (Leg1 Empty)','e','1 MT - Allow Insert','i','885 Empty Legs - Leg 1 Is Empty','Export','Copy - VESSEL','Container Movement']) THEN '"cnt"'::jsonb

                WHEN bt.name = ANY(ARRAY['TEST QA','Woolworths Test Template','TDK LD','TEST APP','cxvvv','t1','MNX',' ','OD Single Leg','Test template with UOM','Test QA','FTL Domestic','Nina template','Multi-Leg','Bobtail Bookings','Test template UOM','F','L','all-fields-edited-name-abc','S','123','T','Test new version','MT-500','default_template','FTL Single Leg','Royce Template','one-leg','e','g','i','l','n','34234','aas','Test Multiple Legs']) THEN '"ftl"'::jsonb

                WHEN bt.name = ANY(ARRAY['M.SG Last Mile Template - Copy','mt-500-test','Order Template','Tung - Point To Point','Sandstone','Fujifilm','Test Send','kytest','single_task','SDL Manifest','Muji Home Delivery','QA full required fields','template-using-new-label','Template with sender id','KVC Template','B2C','DIETMONSTA YOJEE','PDS Local','Vallen SG Deliveries','test-eta-opening-closing','Thanh - Point To Point','Test tasks','Point To Point 2','Copy - 1 leg template','TNN - QA UOM','Single Leg Custom','full fields','Copy - LTL Single Leg','MT-500-one','Copy - point_to_point','test-template-with-uom','YOJEE','Copy - QA full required fields','Single Leg - 1PU 1 DO','LTL Single Leg','OD-Single Leg','Point To Point','point_to_point','qa-template-one','_','Test template','a','e','SendSingapore','g','i','k','2 legs','l','n','Single Task','Simple','s','Ceva','t','checking-template','SG Maersk Last Mile Template','LTL Multi Leg','test template']) THEN '"ltl"'::jsonb

            END,
	    FALSE
	)
    WHERE
	bt.deleted_at IS NULL
	AND bt.format = 2;
```
