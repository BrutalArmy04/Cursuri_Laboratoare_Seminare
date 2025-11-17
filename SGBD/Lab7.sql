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