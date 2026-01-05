--Lab plsql 1
--10

create table zile_sro
(
    id number(6), data date, nume_zi varchar2(50)
);

--last_day(sysdate) = 30 - nov - 25
-- 30-nov-25 -sysdate = 27 (sau 26)

DECLARE 
  contor  NUMBER(6) := 1; 
  v_data  DATE; 
  maxim   NUMBER(2) := LAST_DAY(SYSDATE)-SYSDATE; 
BEGIN 
  LOOP 
    v_data := sysdate+contor; 
    INSERT INTO zile_sro 
    VALUES (contor,v_data,to_char(v_data,'Day')); 
    contor := contor + 1; 
    EXIT WHEN contor > maxim; 
  END LOOP; 
END; 
/

select * from ZILE_SRO;

--11

DECLARE 
  contor  NUMBER(6) := 1; 
  v_data  DATE; 
  maxim   NUMBER(2) := LAST_DAY(SYSDATE)-SYSDATE;
  BEGIN 
  WHILE contor <= maxim LOOP 
    v_data := sysdate+contor; 
    INSERT INTO zile_sro 
    VALUES (contor,v_data,to_char(v_data,'Day')); 
    contor := contor + 1; 
  END LOOP; 
END; 
/ 

--12

DECLARE 
  v_data  DATE; 
  maxim   NUMBER(2) := LAST_DAY(SYSDATE)-SYSDATE; 
BEGIN 
  FOR contor IN 1..maxim LOOP -- for i in reverse 1..max loop pt for invers
    v_data := sysdate+contor; 
    INSERT INTO zile_sro 
    VALUES (contor,v_data,to_char(v_data,'Day')); 
  END LOOP; 
END; 
/ 

--13

--goto = assembly memories doar ca merge doar in ac bloc begin end

DECLARE 
   i        POSITIVE:=1; 
   max_loop CONSTANT POSITIVE:=10; 
BEGIN 
LOOP 
   i:=i+1; 
   IF i>max_loop THEN -- si nu mai e scrisa asta
     DBMS_OUTPUT.PUT_LINE('in loop i=' || i); 
     GOTO urmator; -- sau EXIT WHEN i>max_loop;
   END IF; 
END LOOP; 
<<urmator>> 
i:=1; 
DBMS_OUTPUT.PUT_LINE('dupa loop i=' || i); 
END; 
/



create table noiembrie_sro( id number(6), data date);

DECLARE
    maxim NUMBER(2) := LAST_DAY(SYSDATE);  
    v_data  DATE := trunc(sysdate, 'month'); 
    vrdate date;
    nr_imprumuturi NUMBER(3);
BEGIN
    for contor in 0..maxim loop -- mai putin performant
        v_data := sysdate+contor;
        insert into noiembrie_sro values (contor, v_data);
        select  count(member_id) into nr_imprumuturi
        from rental R
        where v_data = book_date;
        dbms_output.put_line('Ziua: ' || vrdate || 'Numar imprumuturi: ' || nr_imprumuturi);
    end LOOP;
end;
/

select * from NOIEMBRIE_SRO;

select first_name from member;

--e3

set SERVEROUTPUT on;

DECLARE
    numar NUMBER;
    nume member.LAST_NAME%TYPE:= '&input_nume';
    v_member_id member.member_id%TYPE;
    categorie varchar2(15);
    v_nr_filme_tot TITLE.TITLE_ID%TYPE;

BEGIN
    SELECT member_id INTO v_member_id
    FROM member
    WHERE UPPER(last_name) = UPPER(nume);
    SELECT COUNT(*) INTO numar
    FROM rental
    WHERE member_id = v_member_id;
    select count(*) into v_nr_filme_tot
    from title;
    case 
        when v_nr_filme_tot > (3/4) * numar then categorie := 'Categoria 1';
        when v_nr_filme_tot > (1/2) * numar then categorie := 'Categoria 2';
        when v_nr_filme_tot > (1/4) * numar then categorie := 'Categoria 3';
        else categorie := 'Categoria 4';
    end case;
    DBMS_OUTPUT.PUT_LINE('Membrul ' || nume || ' a împrumutat ' || numar || ' filme cu categoria' || categorie );
END;
/

--e5

create table member_sro as select * from member;
alter table member_sro add discount number(6,2);

DECLARE
    numar NUMBER;
    nume member.LAST_NAME%TYPE;
    v_member_id member.member_id%TYPE;
    categorie varchar2(15);
    v_nr_filme_tot TITLE.TITLE_ID%TYPE;

BEGIN
    SELECT member_id INTO v_member_id    --de aici trb schimbat
    FROM member
    WHERE UPPER(last_name) = UPPER(nume);
    SELECT COUNT(*) INTO numar
    FROM rental
    WHERE member_id = v_member_id;
    select count(*) into v_nr_filme_tot
    from title;         -- pana aici
    case 
        when v_nr_filme_tot > (3/4) * numar then categorie := 'Categoria 1';
        when v_nr_filme_tot > (1/2) * numar then categorie := 'Categoria 2';
        when v_nr_filme_tot > (1/4) * numar then categorie := 'Categoria 3';
        else categorie := 'Categoria 4';
    end case;
    DBMS_OUTPUT.PUT_LINE('Membrul ' || nume || ' a împrumutat ' || numar || ' filme cu categoria' || categorie );
END;
/

--tema ex 6 lab plsql 1(select into, if/elsif/else/case, sql%rowcount)

--de aici incepe tema

DECLARE
    v_player_name VARCHAR2(20);
BEGIN
    SELECT nume_utilizator INTO v_player_name 
    FROM JUCATOR 
    WHERE ROWNUM = 1;
    
    DBMS_OUTPUT.PUT_LINE('Primul jucator ' || v_player_name);
END;
/

DECLARE
    v_game_count NUMBER;
BEGIN
    SELECT COUNT(*) INTO v_game_count FROM JOC;
    
    IF v_game_count > 5 THEN
        DBMS_OUTPUT.PUT_LINE('Multe jocuri: ' || v_game_count);
    ELSIF v_game_count BETWEEN 3 AND 5 THEN
        DBMS_OUTPUT.PUT_LINE('Nr mediu de jocuri: ' || v_game_count);
    ELSE
        DBMS_OUTPUT.PUT_LINE('Putine jocuri: ' || v_game_count);
    END IF;
END;
/

DECLARE
    v_updated_rows NUMBER;
BEGIN
    UPDATE RESURSA 
    SET cantitate = cantitate + 1 
    WHERE tip = 1;
    
    v_updated_rows := SQL%ROWCOUNT;
    
    DBMS_OUTPUT.PUT_LINE('Update ' || v_updated_row);
END;
/