--e4

CREATE OR REPLACE TRIGGER trg_limit_angajati_dept
    AFTER INSERT OR UPDATE OF department_id ON emp_sro
DECLARE
    CURSOR c_dept_violation IS
        SELECT department_id, COUNT(*) as nr_angajati
        FROM emp_sro
        GROUP BY department_id
        HAVING COUNT(*) > 45;
        
    v_dept_id emp_sro.department_id%TYPE;
    v_count   NUMBER;
BEGIN
    FOR rec IN c_dept_violation LOOP
        RAISE_APPLICATION_ERROR(-20001, 
            'Eroare: Departamentul ' || rec.department_id || 
            ' are deja ' || rec.nr_angajati || 
            ' angajati. Limita maxima este de 45.');
    END LOOP;
END;
/


--e5 b


CREATE OR REPLACE TRIGGER trg_cascade_dept_sro
    AFTER DELETE OR UPDATE OF department_id ON dept_test_sro
    FOR EACH ROW
BEGIN
    IF DELETING THEN
        DELETE FROM emp_test_sro
        WHERE department_id = :OLD.department_id;
        
    ELSIF UPDATING('department_id') THEN
        UPDATE emp_test_sro
        SET department_id = :NEW.department_id
        WHERE department_id = :OLD.department_id;
    END IF;
END;
/

