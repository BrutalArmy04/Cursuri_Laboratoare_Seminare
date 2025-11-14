#include <stdio.h>
#include <unistd.h>
#include <stdlib.h>
#include <signal.h>
#include <string.h>
#include <sys/wait.h>


void sigint_handler(int signum) {
    printf("\nA primit SIGINT (%d), dar nu se opreste\n", signum);
    printf("Folosesc 'kill -9 %d' \n", getpid());   //doar asta merge
}

void sigchld_handler(int signum) {
    int status;
    pid_t pid;
    while ((pid = waitpid(-1, &status, WNOHANG)) > 0) {     // termina copiii
        if (WIFEXITED(status)) {
            printf("Copilul %d s-a terminat cu codul: %d\n", pid, WEXITSTATUS(status));
        } else if (WIFSIGNALED(status)) {
            printf("Copilul %d a fost terminat de semnalul: %d\n", pid, WTERMSIG(status));
        }
    }
}

void prob1()
{
    printf("Pid proces: %d\n", getpid());
    printf("Omor procesul intr-un alt terminal cu kill -9 nr proces");     
    while (1)
    sleep(1);
}


void prob2()
{
    printf("PID-ul procesului: %d\n", getpid());
    signal(SIGINT, sigint_handler);
    printf("Ctrl-C!\n");    // nu merge sa omoare procesul cu ctrl-c
    while (1) {
        sleep(1);
    }
}

void prob3()
{
    int num_children = 30;
    pid_t pid;
    signal(SIGCHLD, sigchld_handler);
    printf("Parinte - PID: %d\n", getpid());
    
    for (int i = 0; i < num_children; i++) {
        pid = fork();
        
        if (pid == 0) {
            printf("Copil %d (PID: %d) a inceput...\n", i, getpid());
            sleep(2 + i); 
            printf("Copil %d (PID: %d) se termina.\n", i, getpid());
            exit(i); 
        } else if (pid < 0) {
            perror("fork");
            exit(1);
        }
    }
    printf("Parintele asteapta\n");
    while (1) {
        sleep(1);
    }
}
int main()
{

    //prob1();    
    //prob2();
    prob3();
    return 0;

}
