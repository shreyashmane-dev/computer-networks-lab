// TCP Server - Reverse String (Windows)
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <winsock2.h>
#include <ws2tcpip.h>

#pragma comment(lib, "ws2_32.lib")

int main() 
{
    WSADATA wsa;
    char buff[512], str1[512], c;
    SOCKET SocketFD, connectFD;
    int len, i, k, a;
    struct sockaddr_in stSockAddr, cli_addr;

    if (WSAStartup(MAKEWORD(2, 2), &wsa) != 0) 
    {
        perror("WSAStartup failed");
        exit(EXIT_FAILURE);
    }

    SocketFD = socket(AF_INET, SOCK_STREAM, 0);
    if (SocketFD == INVALID_SOCKET) 
    {
        perror("can not creat socket");
        WSACleanup();
        exit(EXIT_FAILURE);
    }

    memset(&stSockAddr, 0, sizeof(stSockAddr));
    stSockAddr.sin_family = AF_INET;
    stSockAddr.sin_port = htons(1504);
    stSockAddr.sin_addr.s_addr = INADDR_ANY;

    if (bind(SocketFD, (struct sockaddr*)&stSockAddr, sizeof(stSockAddr)) == SOCKET_ERROR) 
    {
        perror("can not bind");
        closesocket(SocketFD);
        WSACleanup();
        exit(EXIT_FAILURE);
    }

    listen(SocketFD, 2);
    printf("Server listening on port 1504...\n");

    a = sizeof(cli_addr);
    connectFD = accept(SocketFD, (struct sockaddr*)&cli_addr, &a);
    if (connectFD == INVALID_SOCKET) 
    {
        perror("can not connect");
        closesocket(SocketFD);
        WSACleanup();
        exit(EXIT_FAILURE);
    }

    printf("\n Received String: ");
    memset(buff, 0, sizeof(buff));
    recv(connectFD, buff, 512, 0);
    printf("%s", buff);

    len = strlen(buff);
    for (i = len - 1, k = 0; i >= 0; i--, k++) 
    {
        c = buff[i];
        str1[k] = c;
    }
    str1[k] = '\0';

    printf("\n Reversed String: %s\n", str1);
    send(connectFD, str1, 512, 0);

    closesocket(connectFD);
    closesocket(SocketFD);
    WSACleanup();
    return EXIT_SUCCESS;
}

