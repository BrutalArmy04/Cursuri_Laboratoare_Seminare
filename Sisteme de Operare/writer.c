#include <stdio.h>
#include <unistd.h>
#include <fcntl.h>
#include <string.h>

int main() {
    int fd = open("myfifo", O_WRONLY);
    if (fd < 0) {
        perror("open");
        return 1;
    }
    
    char msg[] = "Salut de la writer!";
    printf("Trimit: %s\n", msg);
    write(fd, msg, strlen(msg) + 1);
    
    close(fd);
    return 0;
}