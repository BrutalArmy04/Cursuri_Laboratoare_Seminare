set serveroutput on;

DECLARE 
  v_nr    number(4); 
  v_nume  departments.department_name%TYPE; 
  CURSOR c IS 
    SELECT department_name nume, COUNT(employee_id) nr   
    FROM   departments d, employees e 
    WHERE  d.department_id=e.department_id(+)  
    GROUP BY department_name;  
BEGIN 
  OPEN c; 
  LOOP 
      FETCH c INTO v_nume,v_nr; 
      EXIT WHEN c%NOTFOUND; 
      IF v_nr=0 THEN 
         DBMS_OUTPUT.PUT_LINE('In departamentul '|| v_nume|| 
                           ' nu lucreaza angajati'); 
      ELSIF v_nr=1 THEN 
           DBMS_OUTPUT.PUT_LINE('In departamentul '|| v_nume|| 
                           ' lucreaza un angajat'); 
      ELSE 
         DBMS_OUTPUT.PUT_LINE('In departamentul '|| v_nume|| 
                           ' lucreaza '|| v_nr||' angajati'); 
     END IF; 
 END LOOP; 
 CLOSE c; 
END;
/

--pt fiecare job id-ul, nr de angajati, sal mediu si sal total platit pt jobul respectiv


SET SERVEROUTPUT ON;
DECLARE
    CURSOR c_jobs IS
        SELECT job_id, COUNT(employee_id) AS nr_angajati,
               AVG(salary) AS sal_med, SUM(salary) AS sal_total
        FROM employees
        GROUP BY job_id;
    
    v_job_id employees.job_id%TYPE;
    v_nr_angajati NUMBER;
    v_sal_med NUMBER(10,2);
    v_sal_total NUMBER(10,2);
BEGIN
    OPEN c_jobs;
    LOOP
        FETCH c_jobs INTO v_job_id, v_nr_angajati, v_sal_med, v_sal_total;
        EXIT WHEN c_jobs%NOTFOUND;
        
        DBMS_OUTPUT.PUT_LINE('Job ID: ' || v_job_id || 
                             ', Nr Angajati: ' || v_nr_angajati || 
                             ', Salariu Mediu: ' || TO_CHAR(v_sal_med, '99999.99') || 
                             ', Salariu Total: ' || TO_CHAR(v_sal_total, '9999999.99'));
    END LOOP;
    CLOSE c_jobs;
END;
/
--cu ciclu cursor cu for si bulk collect, aceiasi cerinta de mai sus
DECLARE
    TYPE job_rec_type IS RECORD (
        job_id employees.job_id%TYPE,
        nr_angajati NUMBER,
        sal_med NUMBER(10,2),
        sal_total NUMBER(10,2)
    );
    
    TYPE job_table_type IS TABLE OF job_rec_type;
    v_jobs job_table_type;
BEGIN
    SELECT job_id, COUNT(employee_id) AS nr_angajati,
              AVG(salary) AS sal_med, SUM(salary) AS sal_total
    BULK COLLECT INTO v_jobs
    FROM employees
    GROUP BY job_id;
    FOR i IN 1..v_jobs.COUNT LOOP
        DBMS_OUTPUT.PUT_LINE('Job ID: ' || v_jobs(i).job_id || 
                             ', Nr Angajati: ' || v_jobs(i).nr_angajati || 
                             ', Salariu Mediu: ' || TO_CHAR(v_jobs(i).sal_med, '99999.99') || 
                             ', Salariu Total: ' || TO_CHAR(v_jobs(i).sal_total, '9999999.99'));
    END LOOP;
end;
/
--ciclu cursor cu subcerere (for i in select ... )
DECLARE
    v_job_id employees.job_id%TYPE;
    v_nr_angajati NUMBER;
    v_sal_med NUMBER(10,2);
    v_sal_total NUMBER(10,2);
BEGIN
    FOR rec IN (SELECT job_id, COUNT(employee_id) AS nr_angajati,
                          AVG(salary) AS sal_med, SUM(salary) AS sal_total
                 FROM employees
                 GROUP BY job_id) 
     LOOP
          v_job_id := rec.job_id;
          v_nr_angajati := rec.nr_angajati;
          v_sal_med := rec.sal_med;
          v_sal_total := rec.sal_total;
    
          DBMS_OUTPUT.PUT_LINE('Job ID: ' || v_job_id || 
                              ', Nr Angajati: ' || v_nr_angajati || 
                              ', Salariu Mediu: ' || TO_CHAR(v_sal_med, '99999.99') || 
                              ', Salariu Total: ' || TO_CHAR(v_sal_total, '9999999.99'));
     END LOOP;  
END;
/


--folosim rowcount pt cursor explicit si ciclu cursor standard


--tema e4 

--modif 9 (nu sunt sigur ca am facut ce trebuia)

CREATE OR REPLACE TYPE lista_jucatori_t AS VARRAY(10) OF VARCHAR2(20);
CREATE TABLE manageri_joc (
    cod_mgr NUMBER(10),
    nume VARCHAR2(20),
    lista_jucatori lista_jucatori_t
);


DECLARE
    v_jucatori lista_jucatori_t := lista_jucatori_t('lupul_alb', 'pisica_verde', 'corb_negru');
    v_lista manageri_joc.lista_jucatori%TYPE;
BEGIN
    INSERT INTO manageri_joc VALUES (1, 'Manager 1', v_jucatori);
    INSERT INTO manageri_joc VALUES (2, 'Manager 2', NULL);
    INSERT INTO manageri_joc VALUES (3, 'Manager 3', lista_jucatori_t('vulpe_isteata', 'ursul_cenusiu'));

    SELECT lista_jucatori INTO v_lista FROM manageri_joc WHERE cod_mgr = 1;
    
    DBMS_OUTPUT.PUT_LINE('Jucatorii managerului 1:');
    FOR j IN v_lista.FIRST..v_lista.LAST LOOP
        DBMS_OUTPUT.PUT_LINE(v_lista(j));
    END LOOP;
    
    COMMIT;
END;
/

SELECT * FROM manageri_joc;
DROP TABLE manageri_joc;
DROP TYPE lista_jucatori_t;



-- modif 10

CREATE TABLE jucatori_test AS
SELECT nume_utilizator, id_cont 
FROM JUCATOR 
WHERE ROWNUM <= 3;


CREATE OR REPLACE TYPE tip_resurse_t IS TABLE OF VARCHAR2(20);
/

ALTER TABLE jucatori_test 
ADD (resurse tip_resurse_t)
NESTED TABLE resurse STORE AS tabel_resurse;

DECLARE
BEGIN
    INSERT INTO jucatori_test 
    VALUES ('jucator_nou', 100, tip_resurse_t('Aur', 'Lemn', 'Piatra'));
    
    UPDATE jucatori_test 
    SET resurse = tip_resurse_t('Fier', 'Tesatura')
    WHERE nume_utilizator = 'lupul_alb';
    
    COMMIT;

    DBMS_OUTPUT.PUT_LINE('Jucatori si resursele lor:');
    FOR rec IN (SELECT j.nume_utilizator, r.* 
                FROM jucatori_test j, TABLE(j.resurse) r) LOOP
        DBMS_OUTPUT.PUT_LINE(rec.nume_utilizator || ' - ' || rec.COLUMN_VALUE);
    END LOOP;
end;
/


SELECT * FROM jucatori_test;
DROP TABLE jucatori_test;
DROP TYPE tip_resurse_t;

--e2


DECLARE
    CURSOR c_joburi_detaliate IS
        SELECT j.job_id, 
               j.job_title,
               COUNT(e.employee_id) as nr_angajati,
               NVL(SUM(e.salary), 0) as venit_total,
               NVL(AVG(e.salary), 0) as venit_mediu
        FROM jobs j
        LEFT JOIN employees e ON j.job_id = e.job_id
        GROUP BY j.job_id, j.job_title
        ORDER BY j.job_title;
    
    CURSOR c_angajati (p_job_id VARCHAR2) IS
        SELECT first_name, last_name, salary
        FROM employees
        WHERE job_id = p_job_id
        ORDER BY last_name, first_name;
    
    v_nr_ordine NUMBER;
    v_nr_total_angajati NUMBER := 0;
    v_venit_total_global NUMBER := 0;

BEGIN
    SELECT COUNT(*), NVL(SUM(salary), 0)
    INTO v_nr_total_angajati, v_venit_total_global
    FROM employees;
    
    
    FOR job_rec IN c_joburi_detaliate LOOP
        DBMS_OUTPUT.PUT_LINE('Job: ' || job_rec.job_title);
        
        v_nr_ordine := 0;
        
        IF job_rec.nr_angajati > 0 THEN
            FOR angajat_rec IN c_angajati(job_rec.job_id) LOOP
                v_nr_ordine := v_nr_ordine + 1;
                DBMS_OUTPUT.PUT_LINE(
                    RPAD(v_nr_ordine || '.', 4) || 
                    RPAD(angajat_rec.first_name || ' ' || angajat_rec.last_name, 30) ||
                    TO_CHAR(angajat_rec.salary, '999,999.00')
                );
            END LOOP;
        ELSE
            DBMS_OUTPUT.PUT_LINE('*** Niciun angajat pe acest job ***');
        END IF;
        
        DBMS_OUTPUT.PUT_LINE('Statistici job:');
        DBMS_OUTPUT.PUT_LINE('- Numar angajati: ' || job_rec.nr_angajati);
        DBMS_OUTPUT.PUT_LINE('- Venit total lunar: ' || TO_CHAR(job_rec.venit_total, '999,999,999.00'));
        DBMS_OUTPUT.PUT_LINE('- Venit mediu lunar: ' || TO_CHAR(job_rec.venit_mediu, '999,999.00'));
        
        DBMS_OUTPUT.PUT_LINE('');
        DBMS_OUTPUT.PUT_LINE('');
        
    END LOOP;
    
    DBMS_OUTPUT.PUT_LINE('Total general angajati: ' || v_nr_total_angajati);
    DBMS_OUTPUT.PUT_LINE('Venit total lunar general: ' || TO_CHAR(v_venit_total_global, '999,999,999.00'));
    DBMS_OUTPUT.PUT_LINE('Venit mediu lunar general: ' || TO_CHAR(v_venit_total_global/NULLIF(v_nr_total_angajati,0), '999,999.00'));
    
END;
/