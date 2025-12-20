--EX 4

SELECT 
    T.CATEGORY, 
    COUNT(DISTINCT T.TITLE_ID) AS "NUMAR TITLURI", 
    COUNT(TC.COPY_ID) AS "NUMAR EXEMPLARE" 
FROM RENTAL R 
JOIN TITLE T ON R.TITLE_ID = T.TITLE_ID 
JOIN TITLE_COPY TC ON R.COPY_ID = TC.COPY_ID AND R.TITLE_ID = TC.TITLE_ID 
WHERE T.CATEGORY = (SELECT CATEGORY 
    FROM( 
    SELECT T2.CATEGORY 
    FROM RENTAL R2 
    JOIN TITLE T2 ON R2.TITLE_ID = T2.TITLE_ID 
    GROUP BY T2.CATEGORY 
    ORDER BY COUNT(*) DESC 
    ) 
    WHERE ROWNUM = 1) 
GROUP BY T.CATEGORY; 

-- rezolvare HAVING 

select category, count(*), count(distinct t.title_id) 

from rental r 

join title t on t.title_id = r.title_id 

group by category 

having count(*) = ( 

    select max(count(*)) from rental r 

    join title t on t.title_id = r.title_id 

    group by category 

); 

--EX 5

SELECT TITLE, COUNT(T.TITLE_ID)
FROM TITLE T
JOIN TITLE_COPY TC ON T.TITLE_ID = TC.TITLE_ID
LEFT JOIN RENTAL R ON TC.COPY_ID = R.COPY_ID AND TC.TITLE_ID = R.TITLE_ID
WHERE ACT_RET_DATE IS NULL OR (TC.TITLE_ID, TC.COPY_ID) NOT IN (
        SELECT TITLE_ID, COPY_ID 
        FROM RENTAL)
GROUP BY TITLE;

--EX 6

SELECT T.TITLE, TC.COPY_ID, TC.STATUS, 
            CASE WHEN (TC.TITLE_ID, TC.COPY_ID) NOT IN (
            SELECT TITLE_ID, COPY_ID 
            FROM RENTAL WHERE ACT_RET_DATE IS NULL) 
            THEN 'AVAILABLE'
            ELSE 'RENTED'
            END
AS STATUS_CORECT
FROM TITLE T
JOIN TITLE_COPY TC ON T.TITLE_ID = TC.TITLE_ID;
--LEFT JOIN RENTAL R ON TC.COPY_ID = R.COPY_ID AND TC.TITLE_ID = R.TITLE_ID;

-- Rezolvare  

Select  

    a.title_id,  

    title,  

    copy_id,  

    status status_setat,  

    case  

        when (a.title_id, copy_id) not in ( 

            select title_id, copy_id 

            From   rental 

            Where  act_ret_date is null 

        ) then 'AVAILABLE' 

        else 'RENTED' 

    end status_corect                                         

From  title_copy a 

join title b on a.title_id = b.title_id 

order by 1, 2; 

--tema:ex 7(a:plecam de la 6, punem in subquery si comparam statusul,
-- b: exact ca case, punem caseul in set sau where clauza update),
--8 (subquery + count subquery), 12 ab (pt anumite zile a:putem hardcoda data(2 query cu union)
--b: query clasic cu inner join, group by data imprumut)

--ex 7 a

SELECT 
    CASE WHEN (TC.TITLE_ID, TC.COPY_ID) NOT IN (
        SELECT TITLE_ID, COPY_ID 
        FROM RENTAL WHERE ACT_RET_DATE IS NULL) 
        THEN 'AVAILABLE'
        ELSE 'RENTED'
        END
AS STATUS_CORECT
FROM TITLE T
JOIN TITLE_COPY TC ON T.TITLE_ID = TC.TITLE_ID
WHERE TC.STATUS != CASE 
    WHEN (TC.TITLE_ID, TC.COPY_ID) NOT IN (
        SELECT TITLE_ID, COPY_ID 
        FROM RENTAL 
        WHERE ACT_RET_DATE IS NULL
    ) THEN 'AVAILABLE'
    ELSE 'RENTED'
    END;

--b

CREATE TABLE TITLE_COPY_SRO AS
SELECT * FROM TITLE_COPY;
SELECT * FROM TITLE_COPY_SRO;

UPDATE TITLE_COPY_SRO
SET STATUS = 
    CASE WHEN (TITLE_ID, COPY_ID) NOT IN (
        SELECT TITLE_ID, COPY_ID 
        FROM RENTAL 
        WHERE ACT_RET_DATE IS NULL) 
        THEN 'AVAILABLE'
        ELSE 'RENTED'
        END;

SELECT * FROM TITLE_COPY;
SELECT * FROM TITLE_COPY_SRO;

--8 (nu cred ca am facut bine)

SELECT 
    R.RES_DATE, R.MEMBER_ID, R.TITLE_ID,
    CASE 
        WHEN RT.BOOK_DATE IS NULL THEN 'Nu'
        ELSE 'Da'
    END AS imprumutat_la_data_rezervarii
FROM RESERVATION R
LEFT JOIN RENTAL RT ON R.MEMBER_ID = RT.MEMBER_ID
                    AND R.TITLE_ID = RT.TITLE_ID
                    AND R.RES_DATE = RT.BOOK_DATE
ORDER BY R.RES_DATE;


--12 a

SELECT COUNT(BOOK_DATE)
FROM RENTAL
WHERE BOOK_DATE = TO_DATE('1-09-2025', 'DD-MM-YYYY') OR 
    BOOK_DATE = TO_DATE('2-09-2025', 'DD-MM-YYYY');

--b


SELECT COUNT(RT.BOOK_DATE)
FROM RENTAL RT
JOIN RESERVATION R ON RT.MEMBER_ID = R.MEMBER_ID
                   AND RT.TITLE_ID = R.TITLE_ID
                   AND RT.BOOK_DATE = R.BOOK_DATE;
