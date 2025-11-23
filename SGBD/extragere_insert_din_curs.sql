SELECT
    'INSERT INTO TIP_PLATA (ID_TIP_PLATA, COD, DESCRIERE) VALUES ('
    || NVL(TO_CHAR(ID_TIP_PLATA), 'NULL') || ', '
    || CASE
         WHEN COD IS NULL THEN 'NULL'
         ELSE '''' || REPLACE(REPLACE(COD, '''', ''''''), CHR(10), ' ') || ''''
       END || ', '
    || CASE
         WHEN DESCRIERE IS NULL THEN 'NULL'
         ELSE '''' || REPLACE(REPLACE(DESCRIERE, '''', ''''''), CHR(10), ' ') || ''''
       END
    || ');' AS insert_line
FROM TIP_PLATA;

select * from FACTURI;

-- Enable proper formatting
BEGIN
   DBMS_METADATA.SET_TRANSFORM_PARAM(DBMS_METADATA.SESSION_TRANSFORM, 'PRETTY', TRUE);
   DBMS_METADATA.SET_TRANSFORM_PARAM(DBMS_METADATA.SESSION_TRANSFORM, 'SQLTERMINATOR', TRUE);
END;
/

-- Get complete DDL
SELECT DBMS_METADATA.GET_DDL('TABLE', 'FACTURI') AS table_ddl
FROM dual;

DECLARE 
  TYPE rec IS RECORD (id tip_plata.id_tip_plata%TYPE, 
                      den tip_plata.descriere%TYPE); 
  TYPE tab_ind IS TABLE OF rec 
       INDEX BY PLS_INTEGER; 
  t    tab_ind; 
  start_time NUMBER;
  end_time NUMBER;
BEGIN 
  start_time := DBMS_UTILITY.GET_TIME;
  
   DELETE FROM tip_plata  
   WHERE  id_tip_plata NOT IN (SELECT id_tip_plata  
                               FROM facturi) 
   RETURNING id_tip_plata, descriere BULK COLLECT INTO t; 
   
  DBMS_OUTPUT.PUT_LINE('Tabloul are ' || t.COUNT  
         ||' elemente:'); 
  FOR i IN t.FIRST..t.LAST LOOP 
      DBMS_OUTPUT.PUT_LINE(t(i).id ||' '|| t(i).den); 
  END LOOP; 
  
  end_time := DBMS_UTILITY.GET_TIME;
  DBMS_OUTPUT.PUT_LINE('Execution time: ' || (end_time - start_time)/100 || ' seconds');
  
ROLLBACK; 
END;
/


select * from facturi;
--copy facturi

create table FACTURI_COPY as select * from FACTURI where 1=0;

--add data to copy table
insert into FACTURI_COPY select * from FACTURI;

select * from FACTURI_COPY;


--copy insert statements from FACTURI_COPY
-- ID_FACTURA    ID_CASA    ID_CLIENT    ADRESA_LIVRARE    ADRESA_FACTURARE    ID_TIP_LIVRARE DATA            STATUS    ID_TIP_PLATA

SELECT
    'INSERT INTO FACTURI_COPY (ID_FACTURA, ID_CASA, ID_CLIENT, ADRESA_LIVRARE, ADRESA_FACTURARE, ID_TIP_LIVRARE, DATA, STATUS, ID_TIP_PLATA) VALUES ('
    || NVL(TO_CHAR(ID_FACTURA), 'NULL') || ', '
    || NVL(TO_CHAR(ID_CASA), 'NULL') || ', '
    || NVL(TO_CHAR(ID_CLIENT), 'NULL') || ', '
    || CASE
         WHEN ADRESA_LIVRARE IS NULL THEN 'NULL'
         ELSE '''' || REPLACE(REPLACE(ADRESA_LIVRARE, '''', ''''''), CHR(10), ' ') || ''''
       END || ', '
    || CASE
         WHEN ADRESA_FACTURARE IS NULL THEN 'NULL'
         ELSE '''' || REPLACE(REPLACE(ADRESA_FACTURARE, '''', ''''''), CHR(10), ' ') || ''''
       END || ', '
    || NVL(TO_CHAR(ID_TIP_LIVRARE), 'NULL') || ', '
    || CASE
         WHEN DATA IS NULL THEN 'NULL'
         ELSE '''' || TO_CHAR(DATA, 'YYYY-MM-DD HH24:MI:SS') || ''''
       END || ', '
    || CASE
         WHEN STATUS IS NULL THEN 'NULL'
         ELSE '''' || REPLACE(REPLACE(STATUS, '''', ''''''), CHR(10), ' ') || ''''
       END || ', '
    || NVL(TO_CHAR(ID_TIP_PLATA), 'NULL')
    || ');' AS insert_line
FROM FACTURI_COPY;
 
--extract create table statement from facuturi with all constraints, indexes, etc. for example CREATE TABLE LOB_ARTICOL_VGD (ID_TEXT NUMBER, TITLU VARCHAR2(100), ARTICOL CLOB);
SELECT DBMS_METADATA.GET_DDL('TABLE', 'FACTURI_COPY') AS table_ddl
FROM dual;
TABLE_DDL
_______________________________________________

  CREATE TABLE "SGBD_CURS23"."FACTURI_COPY"
   (    "ID_FACTURA" NUMBER(4,0),
        "ID_CASA" NUMBER(4,0),
        "ID_CLIENT" NUMBER(4,0),
        "ADRESA_LIVRARE" VARCHAR2(255 BYTE),
        "ADRESA_FACTURARE" VARCHAR2(255 BYTE),
        "ID_TIP_LIVRARE" NUMBER(4,0),
        "DATA" DATE,
        "STATUS" VARCHAR2(1 BYTE),
        "ID_TIP_PLATA" NUMBER(4,0)
    ) SEGMENT CREATION DEFERRED
    PCTFREE 10 PCTUSED 40 INITRANS 1 MAXTRANS 255
    NOCOMPRESS LOGGING
    TABLESPACE "USERS"
;



