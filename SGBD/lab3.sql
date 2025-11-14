--1

SELECT TRUNC(SYSDATE, 'MONTH')
FROM DUAL;

--TRUNC -> 'DAY' = 27-10-2025 18:27 -> 27-10-25 00:00
--TRUNC -> 'MONTH' = 27-10-2025 18:27 -> 1-10-25 00:00

--NE DA ZILELE DIN LUNA
SELECT TRUNC((SYSDATE), 'MONTH') + LEVEL - 1
FROM DUAL
CONNECT BY LEVEL <= EXTRACT(DAY FROM LAST_DAY(SYSDATE));



SELECT A.ZI, COUNT(*)
FROM (SELECT TRUNC((SYSDATE), 'MONTH') + LEVEL - 1 AS ZI
FROM DUAL
CONNECT BY LEVEL <= EXTRACT(DAY FROM LAST_DAY(SYSDATE))) A
LEFT JOIN (
SELECT BOOK_DATE, COUNT(RT.BOOK_DATE)
FROM RENTAL RT GROUP BY BOOK_DATE) B
ON A.ZI = B.BOOK_DATE;


-- select  

--     ziua,  

--  (select count(*) from rental where to_char(book_date,'dd.mm.yyyy') = to_char(ziua,'dd.mm.yyyy')) as nr 

-- from  ( 

--     select trunc(sysdate,'month') + level - 1 ziua 

--     from   dual 

--     connect by level <= extract (day from last_day(sysdate)) 

-- ); 

--SET SERVEROUTPUT ON -> DE RULAT MEREU LA INCEPUT

SET SERVEROUTPUT ON;
BEGIN
    DBMS_OUTPUT.PUT_LINE('hELLO wORLD');
END;
/

--declarare (declar var locale)

DECLARE
    a NUMBER; -- echivalent cu int a
    -- nu pot 2 instructiuni in ac timp, adica b,c number e gresit
    b NUMBER := 7;
    c number;
BEGIN
    a:=5;
    DBMS_OUTPUT.PUT_LINE('VAR b = ' || b);  -- concatenare ||
END;
/

DECLARE
    a number:=5;
BEGIN
    DECLARE
        a number :=7;
    BEGIN
        a:=6;--DBMS_OUTPUT.PUT_LINE('VAR a = ' || a);  -- concatenare ||
    END;
    DBMS_OUTPUT.PUT_LINE('VAR a = ' || a);  -- concatenare ||
end;
/

--<<bloc 1>> -> numim blocurile inainte de declare / begin

<<bloc1>>
DECLARE
    a number:=5;
BEGIN
    <<bloc2>>
    DECLARE
        a number :=7;
    BEGIN
        bloc1.a:=6;
        DBMS_OUTPUT.PUT_LINE('VAR a = ' || a);  -- concatenare ||
    END;
    DBMS_OUTPUT.PUT_LINE('VAR a = ' || a);  -- concatenare ||
end;
/

-- :a -> rezolutie de scope
-- variable a -> declar inafara blocurilor

variable a number;
DECLARE
    b number;
BEGIN
    :a:=5;
    b:=6;
end;



DECLARE
    v_id number :=101;
    v_nume employees.last_name%type;
    v_prenume employees.first_name%type; -- asta ia tipul coloanei date

BEGIN
    select last_name, first_name
    into v_nume, v_prenume
    from EMPLOYEES
    where employee_id = v_id;
    dbms_output.put_line(v_nume || ' ' || v_prenume);
end;

--4

DECLARE 
  v_dep departments.department_name%TYPE; 
  nr_angajati number;
BEGIN 
  SELECT department_name, count(employee_id)
  INTO   v_dep, nr_angajati
  FROM   employees e, departments d 
  WHERE  e.department_id=d.department_id  
  GROUP BY department_name 
  HAVING COUNT(*) = (SELECT MAX(COUNT(*)) 
                     FROM   employees 
                     GROUP BY department_id); 
  DBMS_OUTPUT.PUT_LINE('Departamentul '|| v_dep || ' ' || nr_angajati); 
END; 
/


-- select into crapa cand nu gaseste nimic sau cand trebuie sa puna mai multe valori intr-o variabila
-- nu pune null automat


--7

SET VERIFY on; 
DECLARE 
   v_cod           employees.employee_id%TYPE:=&p_cod; 
   v_bonus         NUMBER(8); 
   v_salariu_anual NUMBER(8); 
BEGIN 
   SELECT salary*12 INTO v_salariu_anual 
   FROM   employees  
   WHERE  employee_id = v_cod; 
   IF v_salariu_anual>=200001  
      THEN v_bonus:=20000; 
   ELSIF v_salariu_anual BETWEEN 100001 AND 200000  
      THEN v_bonus:=10000; 
   ELSE v_bonus:=5000; 
END IF; 
DBMS_OUTPUT.PUT_LINE('Bonusul este ' || v_bonus); 
END; 
/ 
--SET VERIFY ON


-- tema e1 si e3

-- e1

DECLARE 
 numar number(3):=100; 
mesaj1 varchar2(255):='text 1'; 
 mesaj2 varchar2(255):='text 2'; 
BEGIN 
  DECLARE 
   numar number(3):=1; 
   mesaj1 varchar2(255):='text 2'; 
   mesaj2 varchar2(255):='text 3'; 
   BEGIN 
   numar:=numar+1; 
   DBMS_OUTPUT.PUT_LINE('numar 1 in subbloc' || numar); 
   mesaj2:=mesaj2||' adaugat in sub-bloc'; 
   DBMS_OUTPUT.PUT_LINE(mesaj1); 
   DBMS_OUTPUT.PUT_LINE(mesaj2); 
  END; 
 numar:=numar+1; 
 mesaj1:=mesaj1||' adaugat un blocul principal'; 
 mesaj2:=mesaj2||' adaugat in blocul principal'; 
 DBMS_OUTPUT.PUT_LINE('numar 1 in subbloc' || numar);  
 DBMS_OUTPUT.PUT_LINE(mesaj1); 
 DBMS_OUTPUT.PUT_LINE(mesaj2);
END;


--numar 1 in subbloc2
--text 2
--text 3 adaugat in sub-bloc
--numar 1 in subbloc101
--text 1 adaugat un blocul principal
--text 2 adaugat in blocul principal

--e3
select first_name from member;

DECLARE
    numar NUMBER;
    nume member.FIRST_NAME%TYPE:= '&input_nume';
    v_member_id member.member_id%TYPE;
BEGIN
    SELECT member_id INTO v_member_id
    FROM member
    WHERE UPPER(first_name) = UPPER(nume);
    SELECT COUNT(*) INTO numar
    FROM rental
    WHERE member_id = v_member_id;
    DBMS_OUTPUT.PUT_LINE('Membrul ' || nume || ' a împrumutat ' || numar || ' filme.');
END;
/
