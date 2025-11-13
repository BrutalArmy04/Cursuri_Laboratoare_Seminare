-- mail privat prof andrei.riclea98@gmail.com

--ex 1 a
-- client     server (cilindru) - pun tipul de baza de date 
-- utilitarul incarca pe disc. aplicatiile client se conecteaza la server cu comenzi (select etc)
-- utilitar -> server -> baza de date

-- ex 1 c
--count(*) - ia in calcul null
--count(1) - nu ia in calcul

--ex 2 b e adev
--ex 3 c e fals
--ex 4 d
--ex 5 c 
--ex 6 a (select merge doar daca returneaza un singur rand)
--ex 7 a
--ex 8 c
--ex 9 c
--ex 10 d (nu stie unde sa le puna. trb sa mentionez lista coloanelor daca vreau sa pun mai putine)s

--ex 11

CREATE TABLE EMP_SRO AS SELECT * FROM EMPLOYEES;
COMMENT ON TABLE EMP_SRO IS 'Informatii despre angajati';

--ex 12

SELECT * FROM USER_TAB_COMMENTS
WHERE TABLE_NAME = 'EMP_SRO';

--ex 13

SELECT SYSDATE FROM DUAL;
ALTER SESSION SET NLS_DATE_FORMAT = 'DD.MM.YYYY HH24:MI:SS'; 
SELECT SYSDATE FROM DUAL;

--ex 14

SELECT EXTRACT(YEAR FROM SYSDATE) 
FROM DUAL;

--ex 15

SELECT EXTRACT(MONTH FROM SYSDATE), EXTRACT(DAY FROM SYSDATE)
FROM DUAL;

--ex 16

SELECT * FROM USER_TABLES
WHERE TABLE_NAME LIKE UPPER('EMP_\%') ESCAPE '\';

--ex 17

--  Exemplu generare script 
--  SELECT 'DROP TABLE ' || table_name || ';' FROM user_tables WHERE table_name LIKE upper('%_***'); 

--  Exemplu salvare query output in fisier 
--  spool 'c:/sterg_tabele.sql';  
--  SELECT 'DROP TABLE ' || table_name || ';' FROM user_tables  
--  WHERE TABLE_NAME LIKE UPPER(‘emp\_%’) ESCAPE ‘\’; 
--  spool off; 

Set feedback off; 
SET PAGESIZE 0;
spool "D:\Facultate\SGBD\";
SELECT 'DROP TABLE ' || table_name || ';' FROM user_tables 
WHERE table_name LIKE UPPER('emp_%');
spool off;

--ex 19

--antetul headerlor este cea scrisa in select, daca e pe mai multe pagini se copiaza antetul. La final sunt cate linii au fost incluse

--ex 20
--set feedback off nu mai spune cate linii au fost folosite

--ex 21
--nu mai apare deloc antetul daca pun set pagesize 0

--ex 22

--ex 23
-- scriptul cu spool (cu select)

spool "D:\Facultate\SGBD\insert.sql"
SELECT
'INSERT INTO DEPARTMENTS (DEPARTMENT_ID, DEPARTMENT_NAME, MANAGER_ID, LOCATION_ID) VALUES (' ||
NVL(TO_CHAR(DEPARTMENT_ID),'NULL') || ', ' ||
CASE WHEN DEPARTMENT_NAME IS NULL THEN 'NULL' ELSE '''' ||
REPLACE(DEPARTMENT_NAME, '''', '''''') || '''' END || ', ' ||
NVL(TO_CHAR(MANAGER_ID),'NULL') || ', ' ||
NVL(TO_CHAR(LOCATION_ID),'NULL') || ');'
FROM DEPARTMENTS;
spool off


--alter user hr identified by oracle account unlock;


