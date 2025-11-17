#include <stdio.h>
#include <unistd.h>
#include <fcntl.h>
#include <string.h>
#include <errno.h>
#include <stdlib.h>

int main() {
    
    int fd = open("myfifo", O_RDWR);
    if (fd < 0) {
        perror("open");
        printf("Rulează mai întâi ./writer\n");
        return errno;
    }
    
    char buf[100];
    char reply[] = "Pong";
    
    printf("Procesul 2 (Reader) a pornit...\n");
    
    while (1) {
        // Așteptăm mesaj
        read(fd, buf, sizeof(buf));
        printf("Proces2 a primit: %s\n", buf);
        
        if (strcmp(buf, "exit") == 0) {
            break;
        }
        
        // Trimitem răspuns
        write(fd, reply, strlen(reply) + 1);
        printf("Proces2 a trimis: %s\n\n", reply);
    }
    
    close(fd);
    
    return 0;
}