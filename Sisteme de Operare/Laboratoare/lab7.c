// 0 e input, 1 e output, 2 e eroare
#include <stdio.h>
#include <unistd.h>
#include <sys/wait.h>


int main(int argc, char const *argv[])
{
    int fd[2];
    pipe(fd);
    if (fork() == 0) {
 
        close(fd[1]);   //inchidem capatul de scriere
        int sum = 0, num;
        while (read(fd[0], &num, sizeof(int)) > 0) {    //scanf poate citi doar de la tastatura, nu stie file desc
            sum += num;
        }
        printf("Suma: %d\n", sum);
        close(fd[0]); 
    }
    else{
        close(fd[0]);
        int numbers[] = {1, 2, 3, 4, 5};
        for (int i = 0; i < 5; i++) {
            write(fd[1], &numbers[i], sizeof(int));
        }
        close(fd[1]);
        wait(NULL);
    }
    return 0;

}

// rwx rwx rwx -- user group others
// daca nu exista sunt cu linie - (e bad sa le aiba toata lumea)



