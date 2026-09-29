#include<iostream>
using namespace std;

int main() {

int frame1[40];
int frame2[20];

int i, j=0, n;
int counter=0;

cout << "Enter the Frame Size               : ";
cin >>n;

cout<< "Enter the Number od bits for Frame2 : ";
for(i=0; i<n; i++)
{
cin>>frame2[i];
};

for(i=0; i<n; i++)
{

if(frame2[i]==1)
{
counter++;
frame1[j] = frame2[i];
j++;
}

else
{
if(counter == 5)
{
counter = 0;
continue; 
}
else
{
frame1[j] = frame2[i];
j++;
counter = 0;
}
 
}
};
for(j=0; j<n; j++)
{
cout<<"The Reciever bit frame is               : "<<frame1[j]<<"  ";
};

return 0;
}
