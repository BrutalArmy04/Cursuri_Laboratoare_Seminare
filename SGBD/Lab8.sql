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


--tema e3 (fara tabel info), e4 (putem face doar pt cei condusi direct)


--e3

set SERVEROUTPUT on;

CREATE OR REPLACE FUNCTION numar_angajati_joburi_sro (
    p_city IN locations.city%TYPE
)
RETURN NUMBER
IS
    v_numar_angajati NUMBER := 0;
    v_dummy_location locations.location_id%TYPE;
    
    oras_inexistent EXCEPTION;
    PRAGMA EXCEPTION_INIT(oras_inexistent, -20003); 
    
BEGIN
    SELECT location_id
    INTO v_dummy_location
    FROM locations
    WHERE city = p_city;
    
    SELECT COUNT(e.employee_id)
    INTO v_numar_angajati
    FROM employees e
    JOIN departments d ON e.department_id = d.department_id
    JOIN locations l ON d.location_id = l.location_id
    WHERE l.city = p_city 
      AND e.employee_id IN (
          SELECT employee_id
          FROM job_history
          GROUP BY employee_id
          HAVING COUNT(DISTINCT job_id) >= 2
      );
    
    IF v_numar_angajati = 0 THEN
        RAISE_APPLICATION_ERROR(-20004, 'Nu lucrează niciun angajat care îndeplinește condiția în orașul ' || p_city);
        NULL; 
    END IF;

    RETURN v_numar_angajati;

EXCEPTION
    WHEN NO_DATA_FOUND THEN
        RAISE_APPLICATION_ERROR(-20003, 'Nu exista orasul ' || p_city || ' in baza de date.');
    WHEN OTHERS THEN
        RAISE_APPLICATION_ERROR(-20005, 'Alta eroare: ' || SQLERRM);
END numar_angajati_joburi_sro;
/

--e4

CREATE OR REPLACE PROCEDURE mareste_salarii_manager_sro (
    p_manager_id IN employees.employee_id%TYPE
)
IS
    CURSOR c_subordonati IS
        SELECT employee_id, last_name, salary
        FROM employees
        START WITH employee_id = p_manager_id
        CONNECT BY PRIOR employee_id = manager_id
        AND employee_id != p_manager_id; 
        
    v_contor_actualizari NUMBER := 0;
    
    manager_inexistent EXCEPTION;
    PRAGMA EXCEPTION_INIT(manager_inexistent, -20006);
    
    v_dummy_manager_id employees.employee_id%TYPE;

BEGIN
    SELECT employee_id INTO v_dummy_manager_id
    FROM employees
    WHERE employee_id = p_manager_id;
    
    FOR r_subordonat IN c_subordonati LOOP
        UPDATE employees
        SET salary = salary * 1.10
        WHERE employee_id = r_subordonat.employee_id;
        
        v_contor_actualizari := v_contor_actualizari + 1;
        
        DBMS_OUTPUT.PUT_LINE('Salariul angajatului ' || r_subordonat.last_name || 
                             ' (ID: ' || r_subordonat.employee_id || ') a fost marit la ' || 
                             r_subordonat.salary * 1.10);
    END LOOP;
    
    IF v_contor_actualizari = 0 THEN
        DBMS_OUTPUT.PUT_LINE('Managerul ' || p_manager_id || ' nu conduce direct sau indirect alti angajati (sau nu au fost modificati).');
    ELSE
        DBMS_OUTPUT.PUT_LINE('Au fost actualizate ' || v_contor_actualizari || ' salarii.');
    END IF;
    
    COMMIT; 

EXCEPTION
    WHEN NO_DATA_FOUND THEN
        RAISE_APPLICATION_ERROR(-20006, 'Nu exista manager cu codul ' || p_manager_id || '.');
    WHEN OTHERS THEN
        ROLLBACK; 
        RAISE_APPLICATION_ERROR(-20007, 'Alta eroare: ' || SQLERRM);
END mareste_salarii_manager_sro;
/