--3.15

UNDEFINE p_clasificare 
  SELECT  
    CASE COUNT(*) 
         WHEN 0  
              THEN  'Nu exista clienti de tipul ' ||  
                     UPPER('&&p_clasificare')  
         WHEN 1  
              THEN  'Exista 1 client de tipul ' ||  
                     UPPER('&&p_clasificare') 
         ELSE 'Exista '|| COUNT(*) || 
              ' clienti de tipul ' ||  
               UPPER('&&p_clasificare') 
         END "INFO CLIENTI" 
  FROM   clasific_clienti 
  WHERE  clasificare = UPPER('&p_clasificare') 
  AND    id_categorie = 1; 

--3.16

UNDEFINE p_clasificare
DECLARE
    v_nr NATURAL;
    v_clasificare CHAR(1) := UPPER('&p_clasificare');
    mesaj VARCHAR2(100);
BEGIN
    SELECT COUNT(*) INTO v_nr
    FROM CLASIFIC_CLIENTI
    WHERE clasificare = v_clasificare
    AND id_categorie = 1;
    mesaj := CASE
        when v_nr = 0 THEN
            'Nu exista clienti de tipul' || v_clasificare
        when v_nr = 1 THEN
            'Exista 1 client de tipul' || v_clasificare
        ELSE
            'Exista' || v_nr || 'clienti de tipul' || v_clasificare
        END;
    DBMS.DBMS_OUTPUT.PUT_LINE(mesaj);
END;



select * from emp_sro;

-- exceptie pt cand nu avem date


DECLARE
    v_salary emp_sro.salary%TYPE;
    v_employee_name emp_sro.first_name%TYPE;
BEGIN
    SELECT salary, first_name INTO v_salary, v_employee_name
    FROM emp_sro 
    WHERE employee_id = 999;  
    
    DBMS_OUTPUT.PUT_LINE('Salariu: ' || v_salary);
    
EXCEPTION
    WHEN NO_DATA_FOUND THEN
        DBMS_OUTPUT.PUT_LINE('Nu exista angajatul ');
    WHEN OTHERS THEN
        DBMS_OUTPUT.PUT_LINE('Alta eroare ' || SQLERRM);
END;
/

--too many rows

DECLARE
    nr_angajati NUMBER;
BEGIN
    SELECT COUNT(*) INTO nr_angajati
    FROM emp.sro
    WHERE first_name = 'Peter'; 
    
    DBMS_OUTPUT.PUT_LINE('Oameni cu numele Peter ' || v_first_name);
    
EXCEPTION
    WHEN TOO_MANY_ROWS THEN
        DBMS_OUTPUT.PUT_LINE('Mai multi cu numele Peter ');
    WHEN NO_DATA_FOUND THEN
        DBMS_OUTPUT.PUT_LINE('Nu are nimeni numele Peter ');
    WHEN OTHERS THEN
        DBMS_OUTPUT.PUT_LINE('Alta eroare ' || SQLERRM);
END;
/

DECLARE
    v_first_name employees.first_name%TYPE;
BEGIN
    SELECT first_name into v_first_name
    FROM employees 
    WHERE first_name = 'Peter'; 
    
    DBMS_OUTPUT.PUT_LINE('Gasit un ' || v_first_name);
    
EXCEPTION
    WHEN TOO_MANY_ROWS THEN
        DBMS_OUTPUT.PUT_LINE('Mai multi cu numele Peter ');
    WHEN NO_DATA_FOUND THEN
        DBMS_OUTPUT.PUT_LINE('Nu are nimeni numele Peter ');
    WHEN OTHERS THEN
        DBMS_OUTPUT.PUT_LINE('Alta eroare ' || SQLERRM);
END;
/