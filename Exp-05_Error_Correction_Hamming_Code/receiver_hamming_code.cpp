#include<iostream>
using namespace std;
int main() {
    int c[11];
    int i;
    cout<<"Enter the Bit : ";
    for(i=0; i<11; i++) {
        cin>>c[i];
    }
    int s1 = c[10] ^ c[8] ^ c[6] ^ c[4] ^ c[2] ^ c[0];
    int s2 = c[9]  ^ c[8] ^ c[5] ^ c[4] ^ c[1] ^ c[0];
    int s4 = c[7]  ^ c[6] ^ c[5] ^ c[4] ^ c[0];
    int s8 = c[10] ^ c[2] ^ c[1] ^ c[0];
    int t = -1;
    if (s8==0 && s4==0 && s2==0 && s1==1) t = 10;
    if (s8==0 && s4==0 && s2==1 && s1==0) t = 9;
    if (s8==0 && s4==0 && s2==1 && s1==1) t = 8;
    if (s8==0 && s4==1 && s2==0 && s1==0) t = 7;
    if (s8==0 && s4==1 && s2==0 && s1==1) t = 6;
    if (s8==0 && s4==1 && s2==1 && s1==0) t = 5;
    if (s8==0 && s4==1 && s2==1 && s1==1) t = 4;
    if (s8==1 && s4==0 && s2==0 && s1==0) t = 3;
    if (s8==1 && s4==0 && s2==0 && s1==1) t = 2;
    if (s8==1 && s4==0 && s2==1 && s1==0) t = 1;
    if (s8==1 && s4==0 && s2==1 && s1==1) t = 0;
    if (t != -1) {
        c[t] = !c[t];
    }
    cout<<"The original data is : ";
    cout<<c[0]<<" "<<c[1]<<" "<<c[2]<<" "<<c[4]<<" "<<c[5]<<" "<<c[6]<<" "<<c[8]<<" ";
    return 0;
}
