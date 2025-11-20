#include <stdio.h>
#include <unistd.h>
#include <fcntl.h>
#include <string.h>
#include <stdlib.h>

int main() {
    printf("Ping: Aștept să mă conectez...\n");
    
    int fd = open("myfifo", O_RDWR);
    if (fd < 0) {
        perror("Ping: open");
        return 1;
    }
    
    printf("Ping: M-am conectat! Pong este pornit.\n");
    
    char buf[100];
    
    for (int i = 0; i < 3; i++) {
        printf("Ping: Trimit -> Ping\n");
        write(fd, "Ping", 5);
        
        read(fd, buf, sizeof(buf));
        printf("Ping: Am primit -> %s\n\n", buf);
        
        sleep(1);
    }
    
    write(fd, "exit", 5);
    printf("Ping: Am terminat.\n");
    
    close(fd);
    return 0;
}