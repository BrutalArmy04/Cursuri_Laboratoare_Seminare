set serveroutput on;
CREATE OR REPLACE TYPE adrese_email_sro AS VARRAY(10) OF VARCHAR2(50);
/

CREATE TABLE client (
    id_client NUMBER,
    nume_client VARCHAR2(100),
    adrese_email adrese_email_sro
);
/

DECLARE
    adrese adrese_email_sro;
BEGIN
    adrese := adrese_email_sro('test1@a.com', 'test2@a.com');
    
    INSERT INTO client (id_client, nume_client, adrese_email)
    VALUES (1, 'Client Test', adrese);
    COMMIT;
END;
/

--E2


CREATE OR REPLACE TYPE tip_orase_sro AS VARRAY(20) OF VARCHAR2(30);
/

CREATE TABLE excursie_sro (
    cod_excursie NUMBER(4),
    denumire VARCHAR2(20),
    orase tip_orase_sro,
    status VARCHAR2(10) CHECK (status IN ('disponibila', 'anulata'))
);
/

BEGIN
    INSERT INTO excursie_sro VALUES (
        1001, 'Tur Europe', 
        tip_orase_sro('Paris', 'Roma', 'Berlin', 'Amsterdam'),
        'disponibila'
    );
    
    INSERT INTO excursie_sro VALUES (
        1002, 'Balcani Tour', 
        tip_orase_sro('Bucuresti', 'Sofia', 'Belgrad'),
        'disponibila'
    );
    
    INSERT INTO excursie_sro VALUES (
        1003, 'Capital Europe', 
        tip_orase_sro('Londra', 'Paris', 'Berlin', 'Viena', 'Budapesta'),
        'disponibila'
    );
    
    INSERT INTO excursie_sro VALUES (
        1004, 'Mediterana', 
        tip_orase_sro('Atena', 'Roma', 'Madrid'),
        'anulata'
    );
    
    INSERT INTO excursie_sro VALUES (
        1005, 'Scandinavia', 
        tip_orase_sro('Stockholm', 'Oslo', 'Copenhaga'),
        'disponibila'
    );
    
    COMMIT;
END;
/

DECLARE
    v_orase tip_orase_sro;
    v_temp VARCHAR2(30);
    v_index1 NUMBER;
    v_index2 NUMBER;
BEGIN
    
    SELECT orase INTO v_orase FROM excursie_sro WHERE cod_excursie = 1001;
    v_orase.EXTEND;
    v_orase(v_orase.COUNT) := 'Praga';
    UPDATE excursie_sro SET orase = v_orase WHERE cod_excursie = 1001;
    
    SELECT orase INTO v_orase FROM excursie_sro WHERE cod_excursie = 1001;
    v_orase := tip_orase_sro(
        v_orase(1), 
        'Bruxelles',  
        v_orase(2),
        v_orase(3),
        v_orase(4),
        v_orase(5)
    );
    UPDATE excursie_sro SET orase = v_orase WHERE cod_excursie = 1001;
    
    SELECT orase INTO v_orase FROM excursie_sro WHERE cod_excursie = 1001;
    
    FOR i IN 1..v_orase.COUNT LOOP
        IF v_orase(i) = 'Berlin' THEN
            v_index1 := i;
        ELSIF v_orase(i) = 'Amsterdam' THEN
            v_index2 := i;
        END IF;
    END LOOP;
    
    IF v_index1 IS NOT NULL AND v_index2 IS NOT NULL THEN
        v_temp := v_orase(v_index1);
        v_orase(v_index1) := v_orase(v_index2);
        v_orase(v_index2) := v_temp;
        
        UPDATE excursie_sro SET orase = v_orase WHERE cod_excursie = 1001;
    END IF;
    
    SELECT orase INTO v_orase FROM excursie_sro WHERE cod_excursie = 1001;
    
    DECLARE
        v_new_orase tip_orase_sro := tip_orase_sro();
    BEGIN
        FOR i IN 1..v_orase.COUNT LOOP
            IF v_orase(i) != 'Roma' THEN
                v_new_orase.EXTEND;
                v_new_orase(v_new_orase.COUNT) := v_orase(i);
            END IF;
        END LOOP;
        
        UPDATE excursie_sro SET orase = v_new_orase WHERE cod_excursie = 1001;
    END;   
    COMMIT;
END;
/