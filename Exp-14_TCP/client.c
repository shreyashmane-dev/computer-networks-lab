// TCP Client (Windows)
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
    struct sockaddr_in stSockAddr; 
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
    stSockAddr.sin_addr.s_addr = inet_addr("127.0.0.1"); 
    int xyz = connect(SocketFD, (struct sockaddr*)&stSockAddr, sizeof(stSockAddr)); 
    if (xyz == SOCKET_ERROR) 
    { 
        perror("can not connect"); 
        closesocket(SocketFD); 
        WSACleanup();
        exit(EXIT_FAILURE); 
    } 
    while (1) 
    { 
        printf("\nenter data to be sent: "); 
        //scanf("%s",buff); 
        gets(buff); 
        send(SocketFD, buff, 512, 0); 
        if (strcmp(buff, "x") == 0) 
            break;
        printf("\n Receiving data from Server....."); 
        memset(buff, 0, sizeof(buff));
        recv(SocketFD, buff, 512, 0); 
        if (strcmp(buff, "x") == 0) 
            break; 
        printf("\n data is:%s", buff); 
    } 
    printf("\n"); 
    closesocket(SocketFD); 
    WSACleanup();
    return EXIT_SUCCESS; 
}

