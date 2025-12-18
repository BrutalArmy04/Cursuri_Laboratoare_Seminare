-- ex de trigger lmd

-- create or replace trigger 
--     trig1_sro
-- before INSERT or update or delete 
--     on emp_sro
-- begin
--     if .... then
--         raise_application_error();
--         end if;
-- end;
-- /

-- create or replace trigger 
--     trig1_sro
-- before INSERT or update or delete 
--     on emp_sro
--     when ......  sau for each row (cand afecteaza fiecare linie, se declanseaza de m ori)
-- begin
--     raise_application_error
-- end;
-- /


create or replace trigger trig1_sro before update of salary on emp_sro for each row
begin   
    if :new.salary < :old.salary
--sunt declarate intern, asa ca trb pusa rezolutia de scope
        then raise_application_error(-20000, 'Eroare');
        end if;
    end;
    /

create or replace trigger trig1_sro before update of salary on emp_sro for each row when
     (new.salary < old.salary)
        begin
         raise_application_error(-20000, 'Eroare');     
        end;
    /


create table job_grades_sro as select * from job_grades;
create or replace trigger trig3_sro before update of lowest_sal, highest_sal on job_grades_sro
for each ROW
DECLARE
    exceptie EXCEPTION;
   -- min_salary_high EXCEPTION;
begin

IF (:OLD.grade_level=1) AND (:old.lowest_sal< :NEW.lowest_sal)
THEN RAISE exceptie;
end if;

EXCEPTION
WHEN exceptie THEN
RAISE_APPLICATION_ERROR (-20003, 'Exista salarii care se gasesc in afara intervalului');

end;
/


--create or replace trigger trig_sro instead of update on .....ALTER
--create view view.tmp

--in general doar pe viewuri

--ex 1

CREATE OR REPLACE TRIGGER trig_block_insert_18
BEFORE INSERT ON emp_sro
FOR EACH ROW
BEGIN
    IF TO_CHAR(SYSDATE, 'HH24') >= '18' THEN
        RAISE_APPLICATION_ERROR(-20001, 'Eroare: Inserarea de noi angajati este interzisa dupa ora 18:00.');
    END IF;
END;
/

--ex 2

CREATE OR REPLACE TRIGGER trig_check_commision_negativ
BEFORE UPDATE OF commission_pct ON emp_sro
FOR EACH ROW
BEGIN
    IF :NEW.commission_pct < 0 THEN
        RAISE_APPLICATION_ERROR(-20002, 'Eroare: Valoarea comisionului nu poate fi negativa.');
    END IF;
END;
/

--ex 3

CREATE OR REPLACE TRIGGER trg_check_salary_range
BEFORE INSERT OR UPDATE OF salary ON emp_sro
FOR EACH ROW
DECLARE
    v_min_sal jobs.min_salary%TYPE;
    v_max_sal jobs.max_salary%TYPE;
BEGIN
    SELECT min_salary, max_salary
    INTO v_min_sal, v_max_sal
    FROM jobs
    WHERE job_id = :NEW.job_id;

    IF :NEW.salary < v_min_sal THEN
        RAISE_APPLICATION_ERROR(-20003, 
            'Eroare: Salariul (' || :NEW.salary || ') este mai mic decat minimul admis (' || v_min_sal || ') pentru jobul ' || :NEW.job_id);
            
    ELSIF :NEW.salary > v_max_sal THEN
        RAISE_APPLICATION_ERROR(-20004, 
            'Eroare: Salariul (' || :NEW.salary || ') depaseste maximul admis (' || v_max_sal || ') pentru jobul ' || :NEW.job_id);
    END IF;
END;
/

 
--trigger ldd 

-- create or replace trigger trig7_sro AFTER
-- create or drop or alter on SCHEMA
-- BEGIN
--     insert...........

-- end;
-- /

--tema e2, e3 a,b

--e2 lab cu pachete

-- Definiti un pachet PL/SQL care sa permita analiza valorii cladirilor construite in orasele jucatorilor. 
-- Pachetul va contine un cursor si o functie


CREATE OR REPLACE PACKAGE pachet_cladiri_oras AS

    TYPE r_cladire_info IS RECORD (
        nume_carte CARTE.nume%TYPE,
        tip_carte  CARTE.tip_carte%TYPE,
        cost       CARTE.cost%TYPE
    );


    CURSOR c_cladiri (p_id_oras ORAS.id_oras%TYPE, p_cost_min NUMBER) 
        RETURN r_cladire_info;

    FUNCTION f_max_cost (v_id_oras ORAS.id_oras%TYPE) RETURN NUMBER;

END pachet_cladiri_oras;
/

CREATE OR REPLACE PACKAGE BODY pachet_cladiri_oras AS

    CURSOR c_cladiri (p_id_oras ORAS.id_oras%TYPE, p_cost_min NUMBER) 
        RETURN r_cladire_info IS
        SELECT c.nume, c.tip_carte, c.cost
        FROM CLADIRE cl
        JOIN CARTE c ON cl.id_carte = c.id_carte
        WHERE cl.id_oras = p_id_oras
          AND c.cost >= p_cost_min;

    FUNCTION f_max_cost (v_id_oras ORAS.id_oras%TYPE) RETURN NUMBER IS
        v_maxim NUMBER := 0;
    BEGIN
        SELECT MAX(c.cost)
        INTO v_maxim
        FROM CLADIRE cl
        JOIN CARTE c ON cl.id_carte = c.id_carte
        WHERE cl.id_oras = v_id_oras;

        IF v_maxim IS NULL THEN
            v_maxim := 0;
        END IF;

        RETURN v_maxim;
    EXCEPTION
        WHEN NO_DATA_FOUND THEN
            RETURN 0;
    END f_max_cost;

END pachet_cladiri_oras;
/

SET SERVEROUTPUT ON;

DECLARE
    v_oras_target ORAS.id_oras%TYPE := 1; -- aleg orasul cu id 1 pt test
    v_cost_max    NUMBER;
    v_rec_cladire pachet_cladiri_oras.c_cladiri%ROWTYPE; 
BEGIN
    v_cost_max := pachet_cladiri_oras.f_max_cost(v_oras_target);
    
    DBMS_OUTPUT.PUT_LINE('In orasul cu ID ' || v_oras_target || 
                         ', costul maxim al unei cladiri este: ' || v_cost_max);
    
    DBMS_OUTPUT.PUT_LINE('Lista cladirilor cu acest cost:');

    OPEN pachet_cladiri_oras.c_cladiri(v_oras_target, v_cost_max);
    
    LOOP
        FETCH pachet_cladiri_oras.c_cladiri INTO v_rec_cladire;
        EXIT WHEN pachet_cladiri_oras.c_cladiri%NOTFOUND;
        
        DBMS_OUTPUT.PUT_LINE('Cladire: ' || v_rec_cladire.nume_carte || 
                             ' | Tip: ' || v_rec_cladire.tip_carte || 
                             ' | Cost: ' || v_rec_cladire.cost);
    END LOOP;
    
    CLOSE pachet_cladiri_oras.c_cladiri;
END;
/


--e2 lab plsql6

CREATE OR REPLACE TRIGGER trig_e2_sro
BEFORE UPDATE OF commission_pct ON emp_sro
FOR EACH ROW
BEGIN
    IF :NEW.commission_pct > 0.5 THEN
        RAISE_APPLICATION_ERROR(-20001, 'Eroare: Comisionul nu poate depasi 50% din valoarea salariului!');
    END IF;
END;
/

--e3 a

CREATE TABLE info_dept_sro AS
SELECT DISTINCT department_id as id, 
       'Departament ' || department_id as nume_dept, 
       0 as plati 
FROM emp_sro
WHERE department_id IS NOT NULL;

ALTER TABLE info_dept_sro ADD numar NUMBER(4);

UPDATE info_dept_sro d
SET numar = (SELECT COUNT(*) 
             FROM emp_sro e 
             WHERE e.department_id = d.id);
COMMIT;

--e3 b

CREATE OR REPLACE TRIGGER trig_e3_sro
AFTER INSERT OR DELETE OR UPDATE OF department_id ON emp_sro
FOR EACH ROW
BEGIN
    IF INSERTING THEN
        UPDATE info_dept_sro
        SET numar = NVL(numar, 0) + 1
        WHERE id = :NEW.department_id;
        
    ELSIF DELETING THEN
        UPDATE info_dept_sro
        SET numar = numar - 1
        WHERE id = :OLD.department_id;
        
    ELSIF UPDATING THEN
        UPDATE info_dept_sro
        SET numar = numar - 1
        WHERE id = :OLD.department_id;
        
        UPDATE info_dept_sro
        SET numar = NVL(numar, 0) + 1
        WHERE id = :NEW.department_id;
    END IF;
END;
/