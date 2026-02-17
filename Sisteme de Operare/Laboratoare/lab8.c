// 3 sockets - tcp, udp, local
// socketurile pot vorbi intermasina

#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <unistd.h>
#include <arpa/inet.h>
#include <sys/socket.h>
#include <sys/un.h>
#include <netinet/in.h>
#include <errno.h>

int main() {
    
    int sv[2]; // socketi pentru comunicare bidirectională

    if (socketpair(AF_UNIX, SOCK_STREAM, 0, sv) == -1) {
        perror("socketpair");
        exit(EXIT_FAILURE);
    }

    pid_t pid = fork();
    if (pid < 0) {
        perror("fork");
        exit(EXIT_FAILURE);
    }

    if (pid == 0) { 
        close(sv[0]); 

        FILE *file = fopen("mesaj_copil.txt", "r");
        if (!file) {
            perror("fopen copil");
            exit(EXIT_FAILURE);
        }
        char mesaj_copil[256];
        fgets(mesaj_copil, sizeof(mesaj_copil), file);  // un fel de citire linie (citeste si \n)
        fclose(file);

        // trimitem mesajul catre parinte
        write(sv[1], mesaj_copil, strlen(mesaj_copil) + 1);
        close(sv[1]); 
        exit(EXIT_SUCCESS);
    } else { 
        close(sv[1]); 

        char mesaj_prim[256];
        read(sv[0], mesaj_prim, sizeof(mesaj_prim));
        printf("Parinte a primit: %s", mesaj_prim);

        FILE *file = fopen("mesaj_parinte.txt", "r");
        if (!file) {
            perror("fopen parinte");
            exit(EXIT_FAILURE);
        }
        char mesaj_parinte[256];
        fgets(mesaj_parinte, sizeof(mesaj_parinte), file);
        fclose(file);

        printf("Parinte citeste: %s", mesaj_parinte);

        close(sv[0]); 
        wait(NULL);
    }

    return 0;

}