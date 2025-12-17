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

