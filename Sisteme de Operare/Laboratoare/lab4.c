#include <stdio.h>
#include <sys/types.h>
#include <unistd.h>
#include <sys/wait.h>

void fork_simplu()

{
    printf("Inainte de fork: %d\n", getpid());
    pid_t pid = fork();

    if(pid<0)
    perror("Nu a mers fork");
    else if (pid==0)
    {
        char *argv[] = {"/bin/ls", NULL};
        execve("/bin/ls", argv, NULL);
        perror("execve");
    }
    else{
        printf("pid parinte = %d\n", getpid());
        printf("pid copil = %d\n", pid);
        wait(NULL);
        printf("Copchilul ii gata\n");
    }

}

void collatz_calcul(int n)
{
    printf("%d ", n);
    while (n!=1)
    {
        if (n%2 == 0)
        n/=2;
        else
        n = 3*n+1;

        printf("%d ", n);
    }
    printf("\n");
}

void collatz(int argc, char *argv[])
{
    printf("Inainte de fork: %d\n", getpid());

    for (int i = 1; i<argc;i++)
    {
    pid_t pid = fork();

    if(pid<0)   
    perror("Nu a mers fork");
    else if (pid==0)
    {
        int num = atoi(argv[i]);
        collatz_calcul(num);
        printf("Parinte %d Copil %d\n", getppid(), getpid());
        exit(0);
    }
    }
    for (int i = 1; i<argc;i++)
    wait(NULL);
    printf("toti is gata");
}

int main(int argc, char *argv[])
{

    if (argc < 2)
    {
        printf("Utilizare: %s numar1 numar2 ...\n", argv[0]);
        return 1;
    }
    //fork_simplu();
    collatz(argc, argv);

    return 0;

}

//sys_ktest.c
//sys_khello.c