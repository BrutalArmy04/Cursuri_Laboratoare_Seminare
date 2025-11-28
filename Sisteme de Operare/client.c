// client.c - TCP echo client
// Compile: gcc client.c -o client
// Run: ./client

#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <unistd.h>
#include <errno.h>
#include <arpa/inet.h>
#include <netinet/in.h>
#include <sys/socket.h>

#define SERVER_IP "127.0.0.1"
#define PORT 5000
#define BUF_SIZE 1024

int main(void) {
    int client_fd;
    struct sockaddr_in server_addr;
    char buffer[BUF_SIZE];
    
    // 1. Create socket
    client_fd = socket(AF_INET, SOCK_STREAM, 0);
    if (client_fd < 0) {
        perror("socket");
        exit(EXIT_FAILURE);
    }
    
    // 2. Set up server address
    memset(&server_addr, 0, sizeof(server_addr));
    server_addr.sin_family = AF_INET;
    server_addr.sin_port = htons(PORT);
    
    if (inet_pton(AF_INET, SERVER_IP, &server_addr.sin_addr) <= 0) {    // Convert IP address from text to binary form
        perror("inet_pton");
        close(client_fd);
        exit(EXIT_FAILURE);
    }
    
    // 3. Connect to server
    if (connect(client_fd, (struct sockaddr *)&server_addr, sizeof(server_addr)) < 0) {
        perror("connect");
        close(client_fd);
        exit(EXIT_FAILURE);
    }
    
    printf("Connected to server %s:%d\n", SERVER_IP, PORT);
    printf("Type messages to send to server (Ctrl+C to exit):\n");
    
    // Main communication loop
    while (1) {
        // Read from stdin
        printf("> ");
        fflush(stdout);
        
        if (fgets(buffer, BUF_SIZE, stdin) == NULL) {
            if (feof(stdin)) {
                printf("\nEOF detected. Closing connection.\n");
                break;
            } else {
                perror("fgets");
                break;
            }
        }
        
        // Send to server
        ssize_t bytes_sent = send(client_fd, buffer, strlen(buffer), 0);
        if (bytes_sent < 0) {
            perror("send");
            break;
        }
        
        // Receive echo from server
        ssize_t bytes_received = recv(client_fd, buffer, BUF_SIZE - 1, 0);
        if (bytes_received < 0) {
            perror("recv");
            break;
        } else if (bytes_received == 0) {
            printf("Server closed the connection.\n");
            break;
        }
        
        // Null-terminate and display the received data
        buffer[bytes_received] = '\0';
        printf("Echo: %s", buffer);
    }
    
    // Close socket
    close(client_fd);
    printf("Connection closed.\n");
    
    return 0;
}
