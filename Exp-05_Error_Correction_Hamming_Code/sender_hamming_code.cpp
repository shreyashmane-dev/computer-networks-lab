#include<iostream>
using namespace std;

int main() 
{

int d[7];
int c[11];
int i;
cout<<"Enter the Bit : ";
for(i=0; i<7; i++)
{
cin>>d[i];
}

c[0]=d[0];
c[1]=d[1];
c[2]=d[2];
c[4]=d[3];
c[5]=d[4];
c[6]=d[5];
c[8]=d[6];

c[10]=c[8]^c[6]^c[4]^c[2]^c[0];
c[9]=c[8]^c[5]^c[4]^c[1]^c[0];
c[7]=c[6]^c[5]^c[4]^c[0];
c[10]=c[2]^c[1]^c[0];
cout<<"The codeword is : ";

for(i=0; i<11; i++)
{
cout<<c[i]<<" ";
}

return 0;
}
