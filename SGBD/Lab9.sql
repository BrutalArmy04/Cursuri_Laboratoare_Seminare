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

CREATE OR REPLACE FUNCTION get_department_top_employees_simple
RETURN dept_employee_list PIPELINED
IS
BEGIN
    FOR dept_rec IN (
        SELECT d.department_id,
               d.department_name,
               e.first_name || ' ' || e.last_name AS manager_name
        FROM departments d
        LEFT JOIN employees e ON d.manager_id = e.employee_id
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
                FROM employees e
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
END get_department_top_employees_simple;
/

SELECT 
    department_id AS "ID Departament",
    department_name AS "Nume Departament",
    manager_name AS "Manager",
    ranking || '. ' || first_name || ' ' || last_name || 
    ' (ID: ' || employee_id || ', Salariu: ' || salary || ')' AS "Angajat"
FROM TABLE(get_department_top_employees_simple())
ORDER BY department_id, ranking;

--tema e7 din lab precedent, e1 a b, e, f