#include <stdio.h>
#include <unistd.h>
#include <fcntl.h>
#include <string.h>
#include <stdlib.h>

int main() {
    printf("Pong: Mă conectez...\n");
    
    int fd = open("myfifo", O_RDWR);
    if (fd < 0) {
        perror("Pong: open");
        return 1;
    }
    
    printf("Pong: M-am conectat! Ascult...\n");
    
    char buf[100];
    
    while (1) {
        read(fd, buf, sizeof(buf));
        printf("Pong: Am primit -> %s\n", buf);
        
        if (strcmp(buf, "exit") == 0) {
            printf("Pong: Mesaj de ieșire. Mă închid.\n");
            break;
        }
        
        printf("Pong: Trimit -> Pong\n");
        write(fd, "Pong", 5);
    }
    
    close(fd);
    return 0;
}