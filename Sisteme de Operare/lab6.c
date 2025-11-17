#include <stdio.h>
#include <stdlib.h>
#include <sys/mman.h>
#include <sys/stat.h>
#include <fcntl.h>
#include <unistd.h>
#include <sys/wait.h>
#include <string.h>
#include <errno.h>

#define MAX_SIZE 4096


void Collatz (int n, char* buffer){
    int pos = 0; 
    pos = pos + sprintf(buffer + pos, "%d: ", n);

    while ( n != 1 ){
        pos = pos + sprintf(buffer + pos, "%d ", n);
        if ( n % 2 == 0 )
            n = n / 2;
        else
            n = 3 * n + 1;
    }
    
    sprintf(buffer + pos, "1.");
}


int main(int argc, char* argv[]){

    if (argc < 2){
        printf("Nu s-a introdus niciun numar\n");
        return 0;
    }


    int count = argc - 1;
    printf("Starting parent %d\n", getpid());

    size_t shm_size = count * MAX_SIZE;
    const char *shm_name = "shm_collatz";

     int shm_fd = shm_open(shm_name, O_CREAT|O_RDWR,  S_IRUSR | S_IWUSR);
     if (shm_fd < 0){
        printf("Memoria partajata nu a putut fi creata\n");
        return errno;
     }

     if ( ftruncate ( shm_fd , count * MAX_SIZE ) == -1) {
        perror ( NULL );
        shm_unlink ( "shm_collatz" );
        return errno ;
    }


     char *shared = mmap(NULL, shm_size, PROT_READ | PROT_WRITE, MAP_SHARED, shm_fd, 0);
     if (shared == MAP_FAILED) {
        perror("Nu pot mapa memoria partajata");
        shm_unlink(shm_name);
        return errno;
    }


     for (int i = 0; i < count; i++) {
        pid_t pid = fork();

        if (pid < 0) {
            perror("Eroare la fork");
            return errno;
        }

        if (pid == 0) { // copil
            int n = atoi(argv[i + 1]);
            char *my_zone = shared + i * MAX_SIZE; // fiecare copil scrie în zona lui
            Collatz(n, my_zone);
            printf("Done Parent %d Me %d\n", getppid(), getpid());
            return 0; 
        }
    }
        for (int i = 0 ; i < count ; i++)
            wait(NULL);

        for (int i = 0; i < count; i++) // afisez rezultatele fiecarui copil
            printf("%s\n", shared + i * MAX_SIZE);  
            
        printf("Done Parent %d Me %d\n", getppid(), getpid());

    
        munmap(shared, shm_size);
        close(shm_fd);
        shm_unlink(shm_name);    
        
}
