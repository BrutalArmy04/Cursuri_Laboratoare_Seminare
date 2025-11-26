-- e1 d din plsql 3

set SERVEROUTPUT ON;

DECLARE
    TYPE ref_cursor IS REF CURSOR;
    v_cursor_angajati ref_cursor;
    
    v_job_title   jobs.job_title%TYPE; 
    v_nume        employees.last_name%TYPE; 
    v_salariu     employees.salary%TYPE; 
    sem       BOOLEAN;
    
    CURSOR c_jobs IS 
        SELECT j.job_title,
               CURSOR(SELECT e.last_name, e.salary 
                      FROM employees e 
                      WHERE e.job_id = j.job_id) 
        FROM jobs j;
BEGIN
    OPEN c_jobs;
    LOOP
        FETCH c_jobs INTO v_job_title, v_cursor_angajati;
        EXIT WHEN c_jobs%NOTFOUND;
        
        DBMS_OUTPUT.PUT_LINE('Job: ' || v_job_title);
        sem := FALSE;
        
        LOOP
            FETCH v_cursor_angajati INTO v_nume, v_salariu;
            EXIT WHEN v_cursor_angajati%NOTFOUND;
            
            sem := TRUE;
            DBMS_OUTPUT.PUT_LINE('   Angajat: ' || v_nume || ', Salariu: ' || v_salariu);
        END LOOP;
        
        IF NOT sem THEN
            DBMS_OUTPUT.PUT_LINE('   Nu exista angajati');
        END IF;
        
        DBMS_OUTPUT.PUT_LINE(''); 
    END LOOP;
    
    CLOSE c_jobs;
END;
/

--12 

DECLARE 
  TYPE empref IS REF CURSOR;  
  v_emp empref;
  v_nr INTEGER := &n;
BEGIN 
  OPEN v_emp FOR  
    'SELECT last_name, salary, commission_pct ' || 
    'FROM employees WHERE salary > :bind_var' 
     USING v_nr;
  
  DECLARE
    v_nume employees.last_name%TYPE;
    v_salariu employees.salary%TYPE;
    v_comision employees.commission_pct%TYPE;
  BEGIN
    LOOP
      FETCH v_emp INTO v_nume, v_salariu, v_comision;
      EXIT WHEN v_emp%NOTFOUND;
      
      IF v_comision IS NULL THEN
        DBMS_OUTPUT.PUT_LINE('Nume: ' || v_nume || ', Salariu: ' || v_salariu);
      ELSE
        DBMS_OUTPUT.PUT_LINE('Nume: ' || v_nume || ', Salariu: ' || v_salariu || 
                            ', Comision: ' || v_comision);
      END IF;
    END LOOP;
  END;
  
  CLOSE v_emp;
END;
/


--exercitiu functie stocata
-- definiti o functie stocata salariu_mediu_sro care primeste ca parametru un job_id
-- si returneaza salariul mediu pentru angajatii cu job_id-ul respectiv

create or replace function salariu_mediu_sro (p_job_id IN jobs.job_id%TYPE)
  RETURN NUMBER IS
    v_salariu_mediu NUMBER;
    BEGIN
        SELECT AVG(salary)
        INTO v_salariu_mediu
        FROM employees
        WHERE job_id = p_job_id;
        
        RETURN v_salariu_mediu;

        EXCEPTION
            WHEN NO_DATA_FOUND THEN
            raise_aplication_error(-20001, 'Nu exista angajati cu job_id-ul specificat');
        END salariu_mediu_sro;


--tema e3 (fara tabel info), e4 (putem face doar pt cei condusi direct), e7