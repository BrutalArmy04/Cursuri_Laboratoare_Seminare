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

--E6
-- voi rezolva cerinta
--pentru fiecare dintre jocurile 1, 2, 3 și 4, obtineti status-ul precum si lista jucatorilor care participa în cadrul acestora.


--cursor clasic

DECLARE
    CURSOR c_jocuri IS
        SELECT id_joc, status
        FROM JOC
        WHERE id_joc IN (1, 2, 3, 4)
        ORDER BY id_joc;
    
    CURSOR c_jucatori(p_joc_id NUMBER) IS
        SELECT DISTINCT j.nume_utilizator
        FROM JUCATOR j
        INNER JOIN RES_JOC_JOC rjj ON j.nume_utilizator = rjj.nume_utilizator
        WHERE rjj.id_joc = p_joc_id
        ORDER BY j.nume_utilizator;
    
    v_joc_id JOC.id_joc%TYPE;
    v_status JOC.status%TYPE;
    v_jucator VARCHAR2(20);
    v_jucator_count NUMBER;
    
BEGIN
    DBMS_OUTPUT.PUT_LINE('=== JOCURI ȘI JUCATORI PARTICIPANTI ===');
    DBMS_OUTPUT.PUT_LINE('');
    
    -- Parcurgem jocurile
    FOR joc_rec IN c_jocuri LOOP
        DBMS_OUTPUT.PUT_LINE('--- JOCUL ' || joc_rec.id_joc || ' ---');
        DBMS_OUTPUT.PUT_LINE('Status: ' || joc_rec.status);
        DBMS_OUTPUT.PUT_LINE('Jucatori participanti:');
        
        v_jucator_count := 0;
        
        OPEN c_jucatori(joc_rec.id_joc);
        LOOP
            FETCH c_jucatori INTO v_jucator;
            EXIT WHEN c_jucatori%NOTFOUND;
            
            v_jucator_count := v_jucator_count + 1;
            DBMS_OUTPUT.PUT_LINE('   ' || v_jucator_count || '. ' || v_jucator);
        END LOOP;
        CLOSE c_jucatori;
        
        IF v_jucator_count = 0 THEN
            DBMS_OUTPUT.PUT_LINE('   *** Niciun jucator ***');
        ELSE
            DBMS_OUTPUT.PUT_LINE('   Total jucatori: ' || v_jucator_count);
        END IF;
        
        DBMS_OUTPUT.PUT_LINE('');
    END LOOP;
END;
/

--cursor cu parametru (la asta am pus sa adauge si resurse)

DECLARE
    CURSOR c_jocuri_detaliat(p_joc_ids VARCHAR2) IS
        SELECT j.id_joc, j.status,
               (SELECT COUNT(DISTINCT rjj.nume_utilizator) 
                FROM RES_JOC_JOC rjj 
                WHERE rjj.id_joc = j.id_joc) as nr_jucatori
        FROM JOC j
        WHERE j.id_joc IN (
            SELECT TO_NUMBER(REGEXP_SUBSTR(p_joc_ids, '[^,]+', 1, LEVEL))
            FROM dual
            CONNECT BY REGEXP_SUBSTR(p_joc_ids, '[^,]+', 1, LEVEL) IS NOT NULL
        )
        ORDER BY j.id_joc;
    
    v_joc_list VARCHAR2(50) := '1,2,3,4';
    
BEGIN
    DBMS_OUTPUT.PUT_LINE('=== JOCURI ȘI JUCATORI PARTICIPANTI ===');
    DBMS_OUTPUT.PUT_LINE('');
    
    FOR joc_rec IN c_jocuri_detaliat(v_joc_list) LOOP
        DBMS_OUTPUT.PUT_LINE('--- JOCUL ' || joc_rec.id_joc || ' ---');
        DBMS_OUTPUT.PUT_LINE('Status: ' || joc_rec.status);
        
        IF joc_rec.nr_jucatori = 0 THEN
            DBMS_OUTPUT.PUT_LINE('Jucatori: *** Niciun jucator ***');
        ELSE
            DBMS_OUTPUT.PUT_LINE('Jucatori participanti:');
            
            FOR juc_rec IN (
                SELECT DISTINCT j.nume_utilizator,
                       (SELECT COUNT(*) 
                        FROM RES_JOC_JOC rjj2 
                        WHERE rjj2.nume_utilizator = j.nume_utilizator 
                        AND rjj2.id_joc = joc_rec.id_joc) as resurse_detinate
                FROM JUCATOR j
                INNER JOIN RES_JOC_JOC rjj ON j.nume_utilizator = rjj.nume_utilizator
                WHERE rjj.id_joc = joc_rec.id_joc
                ORDER BY j.nume_utilizator
            ) LOOP
                DBMS_OUTPUT.PUT_LINE('   - ' || juc_rec.nume_utilizator || 
                                   ' (Resurse detinute in acest joc: ' || 
                                   juc_rec.resurse_detinate || ')');
            END LOOP;
            
            DBMS_OUTPUT.PUT_LINE('   Total: ' || joc_rec.nr_jucatori || ' jucatori');
        END IF;
        
        DBMS_OUTPUT.PUT_LINE('');
    END LOOP;
END;
/

--expresii cursor

DECLARE
    CURSOR c_jocuri_complet IS
        SELECT j.id_joc,
               j.status,
               CURSOR(
                   SELECT DISTINCT ju.nume_utilizator,
                          c.email
                   FROM JUCATOR ju
                   INNER JOIN RES_JOC_JOC rjj ON ju.nume_utilizator = rjj.nume_utilizator
                   INNER JOIN CONT c ON ju.id_cont = c.id_cont
                   WHERE rjj.id_joc = j.id_joc
                   ORDER BY ju.nume_utilizator
               ) as cursor_jucatori
        FROM JOC j
        WHERE j.id_joc IN (1, 2, 3, 4)
        ORDER BY j.id_joc;
    
    v_joc_id JOC.id_joc%TYPE;
    v_status JOC.status%TYPE;
    v_cursor_jucatori SYS_REFCURSOR;
    
    v_nume_jucator JUCATOR.nume_utilizator%TYPE;
    v_email CONT.email%TYPE;
    v_counter NUMBER;
    
BEGIN
    DBMS_OUTPUT.PUT_LINE('=== JOCURI ȘI JUCATORI PARTICIPANTI ===');
    DBMS_OUTPUT.PUT_LINE('');
    
    OPEN c_jocuri_complet;
    
    LOOP
        FETCH c_jocuri_complet INTO v_joc_id, v_status, v_cursor_jucatori;
        EXIT WHEN c_jocuri_complet%NOTFOUND;
        
        DBMS_OUTPUT.PUT_LINE('=== JOCUL ' || v_joc_id || ' ===');
        DBMS_OUTPUT.PUT_LINE('Status: ' || v_status);
        DBMS_OUTPUT.PUT_LINE('---------------------------------');
        
        v_counter := 0;
        
        LOOP
            FETCH v_cursor_jucatori INTO v_nume_jucator, v_email;
            EXIT WHEN v_cursor_jucatori%NOTFOUND;
            
            v_counter := v_counter + 1;
            DBMS_OUTPUT.PUT_LINE(v_counter || '. ' || v_nume_jucator || 
                               ' | Email: ' || v_email);
        END LOOP;
        
        CLOSE v_cursor_jucatori;
        
        IF v_counter = 0 THEN
            DBMS_OUTPUT.PUT_LINE('*** Joc fara jucatori ***');
        ELSE
            DBMS_OUTPUT.PUT_LINE('---------------------------------');
            DBMS_OUTPUT.PUT_LINE('Total jucatori: ' || v_counter);
        END IF;
        
        DBMS_OUTPUT.PUT_LINE('');
    END LOOP;
    
    CLOSE c_jocuri_complet;
    
END;
/

--PS : voi face mici modificari la baza de date