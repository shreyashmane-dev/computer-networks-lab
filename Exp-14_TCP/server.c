// TCP Server (Windows)
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <winsock2.h>
#include <ws2tcpip.h>

#pragma comment(lib, "ws2_32.lib")

int main() 
{ 
    WSADATA wsa;
    if (WSAStartup(MAKEWORD(2, 2), &wsa) != 0) 
    {
        perror("WSAStartup failed");
        exit(EXIT_FAILURE);
    }

    char buff[512]; 
    SOCKET SocketFD; 
    struct sockaddr_in stSockAddr, cli_addr; 
    SocketFD = socket(AF_INET, SOCK_STREAM, 0); 
    if (SocketFD == INVALID_SOCKET) 
    { 
        perror("can not creat socket"); 
        WSACleanup();
        exit(EXIT_FAILURE); 
    } 
    memset(&stSockAddr, 0, sizeof(stSockAddr)); 
    stSockAddr.sin_family = AF_INET; 
    stSockAddr.sin_port = htons(1109); 
    stSockAddr.sin_addr.s_addr = INADDR_ANY; 
    if (bind(SocketFD, (struct sockaddr*)&stSockAddr, sizeof(stSockAddr)) == SOCKET_ERROR) 
    { 
        perror("can not bind"); 
        closesocket(SocketFD); 
        WSACleanup();
        exit(EXIT_FAILURE); 
    } 
    int a = sizeof(cli_addr); 
    listen(SocketFD, 2); 
  
    printf("Server listening on port 1109...\n");
    SOCKET connectFD = accept(SocketFD, (struct sockaddr*)&cli_addr, &a); 
    if (connectFD == INVALID_SOCKET) 
    { 
        perror("can not connect"); 
        closesocket(SocketFD); 
        WSACleanup();
        exit(EXIT_FAILURE); 
    } 
  
    while (1) 
    { 
        printf("\n Receiving data from client....."); 
        memset(buff, 0, sizeof(buff));
        recv(connectFD, buff, 512, 0); 
   
        if (strcmp(buff, "x") == 0) 
            break; 
        printf("\n data is:%s", buff); 
 
        printf("\nenter data to be sent: "); 
        //scanf("%s",buff); 
        gets(buff); 
        send(connectFD, buff, 512, 0); 
    } 
    closesocket(connectFD); 
    closesocket(SocketFD); 
    WSACleanup();
    printf("\n"); 
    return EXIT_SUCCESS; 
}

