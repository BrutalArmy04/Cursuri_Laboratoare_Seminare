#include <stdio.h>
//#include <unistd.h>
int main()
{
    //printf("Hello, World\n");
    //return 0;
    const char* msg = "Hello, World\n";
    write(1, msg, 15);
}
