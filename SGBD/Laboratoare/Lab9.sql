CREATE OR REPLACE TYPE dept_employee_result AS OBJECT (
    department_id   NUMBER(4),
    department_name VARCHAR2(30),
    manager_name    VARCHAR2(50),
    employee_id     NUMBER(6),
    first_name      VARCHAR2(20),
    last_name       VARCHAR2(25),
    salary          NUMBER(8,2),
    ranking         NUMBER
);
/

CREATE OR REPLACE TYPE dept_employee_list AS TABLE OF dept_employee_result;
/

CREATE OR REPLACE FUNCTION get_department_top_emp_sro_simple
RETURN dept_employee_list PIPELINED
IS
BEGIN
    FOR dept_rec IN (
        SELECT d.department_id,
               d.department_name,
               e.first_name || ' ' || e.last_name AS manager_name
        FROM departments d
        LEFT JOIN emp_sro e ON d.manager_id = e.employee_id
        ORDER BY d.department_id
    ) LOOP
        FOR emp_rec IN (
            SELECT employee_id,
                   first_name,
                   last_name,
                   salary,
                   ranking
            FROM (
                SELECT e.employee_id,
                       e.first_name,
                       e.last_name,
                       e.salary,
                       DENSE_RANK() OVER (ORDER BY e.salary DESC) as ranking
                FROM emp_sro e
                WHERE e.department_id = dept_rec.department_id
            )
            WHERE ranking <= 5
            ORDER BY ranking, last_name, first_name
        ) LOOP
            PIPE ROW(dept_employee_result(
                dept_rec.department_id,
                dept_rec.department_name,
                dept_rec.manager_name,
                emp_rec.employee_id,
                emp_rec.first_name,
                emp_rec.last_name,
                emp_rec.salary,
                emp_rec.ranking
            ));
        END LOOP;
    END LOOP;
    
    RETURN;
END get_department_top_emp_sro_simple;
/

SELECT 
    department_id AS "ID Departament",
    department_name AS "Nume Departament",
    manager_name AS "Manager",
    ranking || '. ' || first_name || ' ' || last_name || 
    ' (ID: ' || employee_id || ', Salariu: ' || salary || ')' AS "Angajat"
FROM TABLE(get_department_top_emp_sro_simple())
ORDER BY department_id, ranking;

--tema e7 din lab precedent, e1 a b, e, f

--e7

CREATE OR REPLACE FUNCTION get_jucator_by_cont (
    p_id_cont IN CONT.id_cont%TYPE
)
RETURN JUCATOR.nume_utilizator%TYPE
IS
    v_nume_utilizator JUCATOR.nume_utilizator%TYPE;
BEGIN
    SELECT nume_utilizator
    INTO v_nume_utilizator
    FROM JUCATOR
    WHERE id_cont = p_id_cont;

    RETURN v_nume_utilizator;

EXCEPTION
    WHEN NO_DATA_FOUND THEN
        RAISE_APPLICATION_ERROR(-20000, 'Nu exista jucator pentru ID-ul de cont ' || p_id_cont);
    WHEN TOO_MANY_ROWS THEN
        RAISE_APPLICATION_ERROR(-20001, 'Exista mai multi jucatori pentru ID-ul de cont ' || p_id_cont);
    WHEN OTHERS THEN
        RAISE_APPLICATION_ERROR(-20002, 'Eroare la functia get_jucator_by_cont: ' || SQLERRM);
END get_jucator_by_cont;
/

SET SERVEROUTPUT ON;
BEGIN
    DBMS_OUTPUT.PUT_LINE('Jucatorul cu ID-ul cont 1 este: ' || get_jucator_by_cont(1));
    DBMS_OUTPUT.PUT_LINE('Jucatorul cu ID-ul cont 2 este: ' || get_jucator_by_cont(2));
    
END;
/

SELECT get_jucator_by_cont(3) FROM DUAL;
SELECT get_jucator_by_cont(4) FROM DUAL;


CREATE OR REPLACE PROCEDURE get_jucator_p (
    p_id_cont IN CONT.id_cont%TYPE,
    p_nume_utilizator OUT JUCATOR.nume_utilizator%TYPE
)
IS
BEGIN
    SELECT nume_utilizator
    INTO p_nume_utilizator
    FROM JUCATOR
    WHERE id_cont = p_id_cont;

EXCEPTION
    WHEN NO_DATA_FOUND THEN
        RAISE_APPLICATION_ERROR(-20000, 'Nu exista jucator pentru ID-ul de cont ' || p_id_cont);
    WHEN TOO_MANY_ROWS THEN
        RAISE_APPLICATION_ERROR(-20001, 'Exista mai multi jucatori pentru ID-ul de cont ' || p_id_cont);
    WHEN OTHERS THEN
        RAISE_APPLICATION_ERROR(-20002, 'Eroare la procedura get_jucator_p: ' || SQLERRM);
END get_jucator_p;
/

DECLARE
    v_nume JUCATOR.nume_utilizator%TYPE;
BEGIN
    get_jucator_p(5, v_nume);
    DBMS_OUTPUT.PUT_LINE('Jucatorul cu ID-ul cont 5 este: ' || v_nume);
    
    get_jucator_p(7, v_nume);
    DBMS_OUTPUT.PUT_LINE('Jucatorul cu ID-ul cont 7 este: ' || v_nume);
END;
/



--e1

CREATE SEQUENCE emp_sro_seq
START WITH 207
INCREMENT BY 1
NOCACHE
NOCYCLE;

CREATE OR REPLACE PACKAGE BODY pachet_gestiune_angajati AS

    CURSOR c_toate_joburile RETURN jobs%ROWTYPE
    IS
        SELECT *
        FROM jobs
        ORDER BY job_title;
    
    CURSOR c_angajati_pe_job (p_job_id emp_sro.job_id%TYPE) RETURN emp_sro%ROWTYPE
    IS
        SELECT *
        FROM emp_sro
        WHERE job_id = p_job_id
        ORDER BY last_name;

    FUNCTION f_get_job_id (p_nume_job jobs.job_title%TYPE)
    RETURN jobs.job_id%TYPE
    IS
        v_job_id jobs.job_id%TYPE;
    BEGIN
        SELECT job_id INTO v_job_id FROM jobs WHERE UPPER(job_title) = UPPER(p_nume_job);
        RETURN v_job_id;
    EXCEPTION
        WHEN NO_DATA_FOUND THEN RAISE_APPLICATION_ERROR(-20110, 'Job-ul specificat nu exista: ' || p_nume_job);
    END f_get_job_id;

    FUNCTION f_get_department_id (p_nume_dept departments.department_name%TYPE)
    RETURN departments.department_id%TYPE
    IS
        v_dept_id departments.department_id%TYPE;
    BEGIN
        SELECT department_id INTO v_dept_id FROM departments WHERE UPPER(department_name) = UPPER(p_nume_dept);
        RETURN v_dept_id;
    EXCEPTION
        WHEN NO_DATA_FOUND THEN RAISE_APPLICATION_ERROR(-20111, 'Departamentul specificat nu exista: ' || p_nume_dept);
    END f_get_department_id;

    FUNCTION f_get_manager_id (p_nume_manager emp_sro.last_name%TYPE, p_prenume_manager emp_sro.first_name%TYPE)
    RETURN emp_sro.manager_id%TYPE
    IS
        v_manager_id emp_sro.manager_id%TYPE;
    BEGIN
        SELECT employee_id INTO v_manager_id
        FROM emp_sro
        WHERE UPPER(last_name) = UPPER(p_nume_manager) AND UPPER(first_name) = UPPER(p_prenume_manager);
        RETURN v_manager_id;
    EXCEPTION
        WHEN NO_DATA_FOUND THEN RAISE_APPLICATION_ERROR(-20112, 'Managerul specificat nu exista.');
        WHEN TOO_MANY_ROWS THEN RAISE_APPLICATION_ERROR(-20113, 'Sunt mai multi angajati cu acelasi nume de manager.');
    END f_get_manager_id;
    
    FUNCTION f_min_salariu (p_id_dept emp_sro.department_id%TYPE, p_id_job emp_sro.job_id%TYPE)
    RETURN NUMBER
    IS
        v_min_salariu emp_sro.salary%TYPE;
    BEGIN
        SELECT NVL(MIN(salary), 0) INTO v_min_salariu FROM emp_sro
        WHERE department_id = p_id_dept AND job_id = p_id_job;
        
        IF v_min_salariu = 0 THEN
            SELECT min_salary INTO v_min_salariu FROM jobs WHERE job_id = p_id_job;
        END IF;
        RETURN v_min_salariu;
    EXCEPTION
        WHEN OTHERS THEN RETURN 0;
    END f_min_salariu;
    
    FUNCTION f_min_comision (p_id_dept emp_sro.department_id%TYPE, p_id_job emp_sro.job_id%TYPE)
    RETURN NUMBER
    IS
        v_min_commission_pct emp_sro.commission_pct%TYPE;
    BEGIN
        SELECT MIN(commission_pct) INTO v_min_commission_pct
        FROM emp_sro
        WHERE department_id = p_id_dept AND job_id = p_id_job AND commission_pct IS NOT NULL;
        
        RETURN v_min_commission_pct; 
    EXCEPTION
        WHEN OTHERS THEN RETURN NULL;
    END f_min_comision;

--a

    PROCEDURE p_adauga_angajat (
        p_nume emp_sro.last_name%TYPE, p_prenume emp_sro.first_name%TYPE,
        p_telefon emp_sro.phone_number%TYPE, p_email emp_sro.email%TYPE,
        p_nume_job jobs.job_title%TYPE, p_nume_dept departments.department_name%TYPE,
        p_nume_manager emp_sro.last_name%TYPE, p_prenume_manager emp_sro.first_name%TYPE
    )
    IS
        v_job_id emp_sro.job_id%TYPE := f_get_job_id(p_nume_job);
        v_dept_id emp_sro.department_id%TYPE := f_get_department_id(p_nume_dept);
        v_manager_id emp_sro.manager_id%TYPE := f_get_manager_id(p_nume_manager, p_prenume_manager);
        v_min_salariu emp_sro.salary%TYPE := f_min_salariu(v_dept_id, v_job_id);
    BEGIN
        INSERT INTO emp_sro (
            employee_id, first_name, last_name, email, phone_number,
            hire_date, job_id, salary, commission_pct, manager_id, department_id
        )
        VALUES (
            emp_sro_seq.NEXTVAL, p_prenume, p_nume, p_email, p_telefon,
            SYSDATE, v_job_id, v_min_salariu, NULL, v_manager_id, v_dept_id
        );
    EXCEPTION
        WHEN OTHERS THEN RAISE_APPLICATION_ERROR(-20100, 'Eroare la adaugarea angajatului: ' || SQLERRM);
    END p_adauga_angajat;

--b
    PROCEDURE p_muta_angajat (
        p_nume_angajat emp_sro.last_name%TYPE, p_prenume_angajat emp_sro.first_name%TYPE,
        p_nume_dept_nou departments.department_name%TYPE, p_nume_job_nou jobs.job_title%TYPE,
        p_nume_manager_nou emp_sro.last_name%TYPE, p_prenume_manager_nou emp_sro.first_name%TYPE
    )
    IS
        v_id_angajat emp_sro.employee_id%TYPE;
        v_salariu_curent emp_sro.salary%TYPE;
        v_job_id_vechi emp_sro.job_id%TYPE;
        v_dept_id_vechi emp_sro.department_id%TYPE;
        
        v_job_id_nou emp_sro.job_id%TYPE := f_get_job_id(p_nume_job_nou);
        v_dept_id_nou emp_sro.department_id%TYPE := f_get_department_id(p_nume_dept_nou);
        v_manager_id_nou emp_sro.manager_id%TYPE := f_get_manager_id(p_nume_manager_nou, p_prenume_manager_nou);
        v_salariu_min_nou emp_sro.salary%TYPE := f_min_salariu(v_dept_id_nou, v_job_id_nou);
        v_comision_min_nou emp_sro.commission_pct%TYPE := f_min_comision(v_dept_id_nou, v_job_id_nou);
    BEGIN
        SELECT employee_id, salary, job_id, department_id INTO v_id_angajat, v_salariu_curent, v_job_id_vechi, v_dept_id_vechi
        FROM emp_sro
        WHERE last_name = p_nume_angajat AND first_name = p_prenume_angajat;
        
        DECLARE
            v_hire_date emp_sro.hire_date%TYPE;
        BEGIN
            SELECT hire_date INTO v_hire_date FROM emp_sro WHERE employee_id = v_id_angajat;
            
            INSERT INTO job_history (employee_id, start_date, end_date, job_id, department_id)
            VALUES (v_id_angajat, v_hire_date, SYSDATE - 1, v_job_id_vechi, v_dept_id_vechi);
        END;
        
        UPDATE emp_sro
        SET department_id = v_dept_id_nou,
            job_id = v_job_id_nou,
            manager_id = v_manager_id_nou,
            hire_date = SYSDATE, 
            salary = CASE WHEN v_salariu_min_nou > v_salariu_curent THEN v_salariu_min_nou ELSE v_salariu_curent END,
            commission_pct = v_comision_min_nou
        WHERE employee_id = v_id_angajat;

    EXCEPTION
        WHEN NO_DATA_FOUND THEN RAISE_APPLICATION_ERROR(-20101, 'Angajatul specificat nu exista.');
        WHEN TOO_MANY_ROWS THEN RAISE_APPLICATION_ERROR(-20102, 'Sunt mai multi angajati cu acelasi nume si prenume.');
        WHEN OTHERS THEN RAISE_APPLICATION_ERROR(-20103, 'Eroare la mutarea angajatului: ' || SQLERRM);
    END p_muta_angajat;

--c
    FUNCTION f_numar_subalterni (p_nume emp_sro.last_name%TYPE, p_prenume emp_sro.first_name%TYPE) 
    RETURN NUMBER
    IS
        v_id_sef emp_sro.employee_id%TYPE;
        v_numar_subalterni NUMBER := 0;
    BEGIN
        SELECT employee_id INTO v_id_sef
        FROM emp_sro
        WHERE UPPER(last_name) = UPPER(p_nume) AND UPPER(first_name) = UPPER(p_prenume);

        SELECT COUNT(employee_id) INTO v_numar_subalterni
        FROM emp_sro
        START WITH employee_id = v_id_sef
        CONNECT BY PRIOR employee_id = manager_id;
        
        RETURN v_numar_subalterni - 1;

    EXCEPTION
        WHEN NO_DATA_FOUND THEN RAISE_APPLICATION_ERROR(-20114, 'Angajatul specificat nu exista.');
        WHEN TOO_MANY_ROWS THEN RAISE_APPLICATION_ERROR(-20115, 'Sunt mai multi angajati cu acelasi nume si prenume.');
        WHEN OTHERS THEN RAISE_APPLICATION_ERROR(-20116, 'Eroare la calculul subalternilor: ' || SQLERRM);
    END f_numar_subalterni;
    

--d
    PROCEDURE p_promoveaza_angajat (
        p_nume_angajat emp_sro.last_name%TYPE,
        p_prenume_angajat emp_sro.first_name%TYPE
    )
    IS
        v_id_angajat emp_sro.employee_id%TYPE;
        v_job_id_curent emp_sro.job_id%TYPE;
        v_dept_id_curent emp_sro.department_id%TYPE;
        v_min_sal_curent jobs.min_salary%TYPE;
        v_hire_date_curent emp_sro.hire_date%TYPE;
        
        v_job_id_nou jobs.job_id%TYPE;
        v_salariu_nou emp_sro.salary%TYPE;
        
        e_fara_job_superior EXCEPTION;
        PRAGMA EXCEPTION_INIT(e_fara_job_superior, -20121);
    BEGIN
        SELECT e.employee_id, e.job_id, e.department_id, e.hire_date, j.min_salary
        INTO v_id_angajat, v_job_id_curent, v_dept_id_curent, v_hire_date_curent, v_min_sal_curent
        FROM emp_sro e, jobs j  
        WHERE e.job_id = j.job_id 
          AND UPPER(e.last_name) = UPPER(p_nume_angajat) AND UPPER(e.first_name) = UPPER(p_prenume_angajat);
        
        BEGIN
            SELECT job_id, min_salary INTO v_job_id_nou, v_salariu_nou
            FROM (
                SELECT job_id, min_salary, 
                       RANK() OVER (ORDER BY min_salary ASC) AS rank_sal
                FROM jobs
                WHERE min_salary > v_min_sal_curent
            )
            WHERE rank_sal = 1 AND ROWNUM = 1;
        EXCEPTION
            WHEN NO_DATA_FOUND THEN
                RAISE_APPLICATION_ERROR(-20121, 'Nu exista o treapta imediat superioara pentru jobul curent.');
        END;

        INSERT INTO job_history (employee_id, start_date, end_date, job_id, department_id)
        VALUES (v_id_angajat, v_hire_date_curent, SYSDATE - 1, v_job_id_curent, v_dept_id_curent);

        UPDATE emp_sro
        SET job_id = v_job_id_nou,
            salary = v_salariu_nou,
            hire_date = SYSDATE 
        WHERE employee_id = v_id_angajat;

    EXCEPTION
        WHEN NO_DATA_FOUND THEN RAISE_APPLICATION_ERROR(-20117, 'Angajatul specificat nu exista.');
        WHEN TOO_MANY_ROWS THEN RAISE_APPLICATION_ERROR(-20118, 'Sunt mai multi angajati cu acelasi nume.');
        WHEN OTHERS THEN RAISE_APPLICATION_ERROR(-20119, 'Eroare la promovarea angajatului: ' || SQLERRM);
    END p_promoveaza_angajat;
    
--e

    PROCEDURE p_actualizeaza_salariu (
        p_nume_angajat emp_sro.last_name%TYPE,
        p_salariu_nou emp_sro.salary%TYPE
    )
    IS
        CURSOR c_angajati IS
            SELECT e.employee_id, e.job_id, j.min_salary, j.max_salary
            FROM emp_sro e, jobs j
            WHERE e.job_id = j.job_id
              AND e.last_name = p_nume_angajat;

        v_angajati_gasiti c_angajati%ROWTYPE;
        v_nr_angajati NUMBER;
    BEGIN
        SELECT COUNT(*) INTO v_nr_angajati FROM emp_sro WHERE last_name = p_nume_angajat;

        IF v_nr_angajati = 0 THEN
            DBMS_OUTPUT.PUT_LINE('Nu exista angajati cu numele dat: ' || p_nume_angajat);
        ELSIF v_nr_angajati > 1 THEN
            DBMS_OUTPUT.PUT_LINE('Sunt mai multi angajati cu numele ' || p_nume_angajat || '. Lista:'); 
            FOR rec IN c_angajati LOOP
                DBMS_OUTPUT.PUT_LINE('- ID: ' || rec.employee_id || ', Job: ' || rec.job_id || ', Salariu min/max: ' || rec.min_salary || '/' || rec.max_salary);
            END LOOP;
        ELSE
            OPEN c_angajati;
            FETCH c_angajati INTO v_angajati_gasiti;
            CLOSE c_angajati;

            IF p_salariu_nou BETWEEN v_angajati_gasiti.min_salary AND v_angajati_gasiti.max_salary THEN 
                UPDATE emp_sro
                SET salary = p_salariu_nou
                WHERE employee_id = v_angajati_gasiti.employee_id;
                DBMS_OUTPUT.PUT_LINE('Salariu actualizat cu succes pentru ' || p_nume_angajat);
            ELSE
                RAISE_APPLICATION_ERROR(-20104, 'Salariul ' || p_salariu_nou || ' nu respecta limitele jobului (' || v_angajati_gasiti.min_salary || '-' || v_angajati_gasiti.max_salary || ')');
            END IF;
        END IF;
    EXCEPTION
        WHEN OTHERS THEN RAISE_APPLICATION_ERROR(-20105, 'Eroare la actualizarea salariului: ' || SQLERRM);
    END p_actualizeaza_salariu;

--h
    
    PROCEDURE p_afiseaza_angajati_pe_job
    IS
        v_istoric BOOLEAN;
        v_count_job_history NUMBER;
    BEGIN
        DBMS_OUTPUT.PUT_LINE(RPAD('Nume Job', 30) || 'Angajat (ID | Istoric Job)');
        DBMS_OUTPUT.PUT_LINE(RPAD('-', 70, '-'));

        FOR v_job IN c_toate_joburile LOOP
            DBMS_OUTPUT.PUT_LINE('Job: ' || v_job.job_title || ' (' || v_job.job_id || ')');

            FOR v_angajat IN c_angajati_pe_job(v_job.job_id) LOOP
                SELECT COUNT(*) INTO v_count_job_history
                FROM job_history
                WHERE employee_id = v_angajat.employee_id
                  AND job_id = v_job.job_id;
                
                v_istoric := (v_count_job_history > 0);
                
                DBMS_OUTPUT.PUT_LINE(
                    RPAD(' ', 3) || v_angajat.last_name || ', ' || v_angajat.first_name || 
                    ' (' || v_angajat.employee_id || ') ' ||
                    CASE WHEN v_istoric THEN ' (A avut jobul in trecut)' ELSE ' (Nu a avut jobul in trecut)' END
                );
            END LOOP;
        END LOOP;
    EXCEPTION
        WHEN OTHERS THEN RAISE_APPLICATION_ERROR(-20120, 'Eroare la afisarea angajatilor pe joburi: ' || SQLERRM);
    END p_afiseaza_angajati_pe_job;


END pachet_gestiune_angajati;
/