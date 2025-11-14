#include <stdio.h>
//#include <unistd.h>
#include <fcntl.h>

int main() //int argc, char const *argv[] = 3
{
    int fd = open("foo", O_RDONLY);
    int fr = open("bar", O_WRONLY);
    char buffer[128];
    int n;
    while(n = read(fd, buffer, sizeof(char))>0)
        write(fr, buffer, n);
    close("foo");
    close("bar");
    
}