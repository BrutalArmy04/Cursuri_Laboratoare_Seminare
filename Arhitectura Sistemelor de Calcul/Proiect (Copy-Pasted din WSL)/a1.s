.data

    
    sp: .long 1024  ;// spatiul maxim al vectorului
    nr_op: .space 8 ;// numarul operatiilor date de la tastatura
    nr_fis: .space 8 ;// numarul fisierelor ce urmeaza sa fie adaugate
    formatScanf: .asciz "%ld" ;// formatul de citire
    var_cit: .space 8 ;// buffer la citire
    desc: .space 8 ;// descriptorul fisierului
    dim : .space 8 ;// dimensiunea fisierului
    sp_liber: .space 16 ;// cat spatiu liber mai am
    start: .space 8 ;// de unde porneste numararea 
    ct_op: .space 8 ;// contorizeaza cate op s-au facut
    indice_d: .space 8 ;// %ecx din afisarea delete / dfrag
    i_fis_curent: .space 8 ;// indicele fisierului curentet
    v: .space 4097  ;// vectorul
    formatPrintf_1: .asciz "%d: (%d, %d)\n" ;// formatul afisarii din add, delete, defrag
    formatPrintf_0 : .asciz "%d: (0, 0)\n" ;// format afisare 0
    formatPrintf_2: .asciz "(%d, %d)\n" ;// formatul afisarii din get

.text

read: ;// functie citire
    push $var_cit
    push $formatScanf
    call scanf
    add $8, %esp
    mov var_cit, %eax
    ret

caut_spatiu:

    push %eax
    xor %ecx, %ecx
    xor %edx, %edx  ;// numara 0-uri consecutive

    et_loop_spatiu:

        cmp %eax, %edx  ;// eax = pentru cate elem am nevoie spatiu 
        je out_caut_spatiu
        cmp %eax, sp_liber  ;// daca nu am spatiu liber suficient
        jl out_nu_am_spatiu

        cmpl $1024, %ecx	;// vedem daca indicele curent a ajuns la 1024
        je out_nu_am_spatiu	;//caz in care nu mai e spatiu, altfel ar continua in reload_loop_spatiu



        cmpl $0, (%edi, %ecx, 4)
        jne bx_0
        add $1, %edx

        reload_loop_spatiu:

            add $1, %ecx
            jmp et_loop_spatiu

        bx_0:
            xor %edx, %edx      ;// daca am gasit un 0 inseamna ca nu are loc, iau numerotarea de la inceput
            jmp reload_loop_spatiu

    out_caut_spatiu:

        ;// edx = pentru cate elem am nev spatiul = eax inainte de aceste atribuiri
        sub %edx, sp_liber
        mov %ecx, %edx
        sub %eax, %edx  ;// edx aici va fi startul
        pop %ebx
        ret

    out_nu_am_spatiu:
            push desc
            push $formatPrintf_0
            call printf
            pop %ebx ;// afisez (0, 0)
            push $0
            call fflush
            pop %ebx
            pop %ebx
            pop %ebx
            xor %eax, %eax
            ret

adaugare: 
    ;//lea v, %edi
    call read
    mov %eax, nr_fis ;// citesc numarul de fisiere
    xor %ecx, %ecx

    et_cit_fis:

        cmp nr_fis, %ecx
        je et_out_add
        add $1, %ecx
        mov %ecx, i_fis_curent
        call read
        mov %eax, desc        ;// citesc descriptorul si dimensiunea
        call read
        mov %eax, dim
        mov $8, %ebx
        xor %edx, %edx
        div %ebx

        cmp $0, %edx    ;// vad de cate sloturi din v am nevoie; daca nr se div la 8 am nev de catul impartirii, aftfel cat+1
        je etnotplus
        add $1, %eax
        etnotplus:

        call caut_spatiu ;// edx = start, eax = cate elemente am de pus, ecx = final
        cmp $0, %eax
        je reload
        mov %edx, %ecx  ;// ecx va incepe de la start (edx), iar eax va fi start + cate vr sa adaug = final
        add %edx, %eax
        movl desc, %ebx

        etadd:

            cmp %ecx, %eax
            je afis_start_stop

            cmpl $0, (%edi, %ecx, 4)    ;// daca e 0 in vector adaug, nu se va incurca cu un eventual delete pt ca spatiu gasit garanteaza asta
            je adauga

            am_adaugat:
            add $1, %ecx
            jmp etadd

            adauga:

            mov %ebx, (%edi, %ecx, 4)
            jmp am_adaugat

        afis_start_stop:

            sub $1, %ecx    ;// ecx va fi, daca nu e scazut, cu 1 mai mult pt ca am facut verificarea la inceput
            push %ecx
            push %edx
            push desc ;// desc: (start, stop = %ecx)
            push $formatPrintf_1  
            call printf
            add $16, %esp
            push $0
            call fflush
            add $4, %esp

        reload:
            mov i_fis_curent, %ecx
            jmp et_cit_fis

        et_out_add:
        ret


get:        

    call read ;// desc pe care il caut, salvat in %eax
    ;//lea v, %edi
    xor %ecx, %ecx
    mov $1025, %edx ;// o valoare care nu poate fi atinsa de %ecx
    xor %ebx, %ebx

    loop_get: ;// caut eax in v, edx tine minte startul, ecx tine minte finalul
    
    cmp sp, %ecx
    je afis_0_get

    cmp %eax, (%edi, %ecx, 4)
    je este_primul

    cmpl $1025, %edx
    jne afis_get

    reload_get:

        addl $1, %ecx
        jmp loop_get

   
    este_primul:

    add $1, %ebx
    cmp $1025, %edx ;// daca nu este primul ma intorc la loop direct
    je prim 

    jmp reload_get

    prim:

        mov %ecx, %edx
        jmp reload_get

    afis_get:
            sub $1, %ecx
            push %ecx
            push %edx
            push $formatPrintf_2 ;// (start, stop)
            call printf
            add $12, %esp
            push $0
            call fflush
            add $4, %esp
            ret

    afis_0_get:

            cmp $0, %ebx
            jne afis_get
            mov $1, %ecx
            mov $0, %edx
            jmp afis_get

delete:         

    call read ;// desc care trb sters va fi in eax
    xor %ecx, %ecx
    xor %ebx, %ebx ;// sa updatez spatiul liber

    stergere:

    cmp %ecx, sp
    je am_sters
    cmp %eax, (%edi, %ecx, 4)
    je sterg

    reload_stergere:

        add $1, %ecx
        jmp stergere


    sterg:

    movl $0, (%edi, %ecx, 4)
    add $1, %ebx
    jmp reload_stergere


    am_sters:
    
    xor %ecx, %ecx

    ;//verific_full_0:

    ;//cmp %ecx, sp
    ;//je et_out_del
    ;//cmp $0, (%edi, %ecx, 4)
    ;//jne afis_delete
    ;//add $1, %ecx
    ;//jmp verific_full_0


    addl %ebx, sp_liber ;// adaug spatiului liber ce am eliberat
    xor %ecx, %ecx
    xor %ebx, %ebx
    xor %edx, %edx

    afis_delete:

    movl %ecx, indice_d
    cmpl %ecx, sp
    je verific_ultimul_elem

    cmpl $0, (%edi, %ecx, 4) ;// verific daca am element pe pozitie
    jne am_element

    cmpl $0, %ebx        ;// verific daca elementul de pe poz curenta e diferit de 0, daca este afisez pt ca este ultimul
    jne afis_desc_del

    reload_afis_delete: ;// trec la urmatorul element

    addl $1, %ecx
    jmp afis_delete

    am_element:         

    cmp %ebx, (%edi, %ecx, 4)   ;// verific daca este primul element din sir
    jne afis_daca_pot
    jmp reload_afis_delete


    afis_daca_pot:    

    cmp $0, %ebx
    jne afis_desc_del

    initializez:

    mov indice_d, %ecx
    mov %ecx, %edx
    mov (%edi, %ecx, 4), %ebx
    jmp reload_afis_delete

    afis_desc_del:

    mov %ecx, %eax
    sub $1, %eax
    push %eax
    push %edx
    push %ebx ;// desc: (start, stop = %ecx)
    push $formatPrintf_1  
    call printf
    add $16, %esp
    push $0
    call fflush
    add $4, %esp
    jmp initializez         


    verific_ultimul_elem:

    sub $1, %ecx
    cmpl $0, (%edi, %ecx, 4)
    jne afis_ultim_elem
    jmp et_out_del

    afis_ultim_elem:

    push %ecx
    push %edx
    push %ebx ;// desc: (start, stop = %ecx)
    push $formatPrintf_1  
    call printf
    add $16, %esp
    push $0
    call fflush
    add $4, %esp
    jmp et_out_del
   
   et_out_del:
    ret

defragmentation:    

    ;// v, %edi
    xor %ecx, %ecx 

    dfrag:

        cmpl sp_liber, %ecx ;// compar cu cate nr efective am, nu am (sper) nevoie de mai multe verificari
        je gata_dfrag
        cmpl $0, (%edi, %ecx, 4) ;// daca v[ecx]!=0 doar incrementez si trec la urmatorul element 
        jne nu_add_0
        mov %ecx, %edx  ;// edx va fi un j din algoritmul de sortare cu complex O(n^2)
        add $1, %edx    ;// i + 1 = j

            search_not_0:

            cmpl sp, %edx    ;// caut in tot vectorul nr diferit de 0
            je nu_add_0
            cmpl $0, (%edi, %edx, 4)     ;// gasesc un nr diferit de 0
            jne swap
            add $1, %edx
            jmp search_not_0

                swap:

                movl (%edi, %edx, 4), %eax
                mov %eax, (%edi, %ecx, 4)       
                movl $0, (%edi, %edx, 4)

        nu_add_0:

        add $1, %ecx
        jmp dfrag

    gata_dfrag:

    xor %ecx, %ecx

    parcurgere_2:

            cmp %ecx, sp_liber
            je et_out_dfrag
            cmpl $0, %eax ;// vad daca am deja descriptor  ;//a1.s:289: Error: operand type mismatch for `cmp'
            jne am_desc_2
            mov (%edi, %ecx, 4), %eax
            mov %ecx, start ;// start
            
            am_desc_2:

                cmp (%edi, %edx, 4), %eax   ;// verific daca desc precedent == desc curent, daca nu afisez
                jne afis_desc_2
                mov %ecx, %edx ;// stop
                
                back_parcurgere_2:
                add $1, %ecx
                jmp parcurgere_2

        afis_desc_2:  
            push %edx
            push $start
            push %eax ;// desc: (start, stop)
            push $formatPrintf_1  
            call printf
            ;//add $16, %esp
            pop %ebx
            pop %ebx
            pop %ebx
            pop %ebx
            push $0
            call fflush
            ;//add $4, %esp
            mov $0, %eax ;// nu mai am descriptor
            jmp back_parcurgere_2

et_out_dfrag:
    ret

.global main

main:

    lea v, %edi
    ;// initializez vector 
    xor %ecx, %ecx
    mov $1024, %eax
    mov %eax, sp_liber

    golesc:

    cmp %ecx, sp
    je am_golit

    movl $0, (%edi, %ecx, 4)
    add $1, %ecx
    jmp golesc

    am_golit:

    ;// citesc numarul operatiilor
    call read    
    mov %eax, nr_op
    xor %ecx, %ecx
    
    ;// citesc operatia si ma duc la op
    etcinop:
        
        xor %eax, %eax
        cmp nr_op, %ecx
        je etexit
        add $1, %ecx
        mov %ecx, ct_op ;// ct_op salveaza indicele urmator
        call read
        mov ct_op, %ecx ;// aici ii revine lui ecx indicele la care sunt
        cmpl $1, %eax ;// eax = codul operatiei
        je apel_add
        cmpl $2, %eax
        je apel_get
        cmpl $3, %eax
        je apel_delete
        cmpl $4, %eax
        je apel_dfrag



    etexit: ;//return 0

    pushl $0
    call fflush
    popl %eax
    mov $1, %eax
    mov $0, %ebx
    int $0x80
    

    apel_add:

        call adaugare
        jmp reload_verif_op

    apel_get:

        call get
        jmp reload_verif_op

    apel_delete:

        call delete
        jmp reload_verif_op

    apel_dfrag:

    reload_verif_op:

        xor %eax, %eax
        mov ct_op, %ecx ;// aici ii revine lui ecx indicele la care sunt
        jmp etcinop

