#include<iostream>
using namespace std;

int main() {

int frame1[20];
int frame2[40];

int i, j=0, n;
int counter=0;

cout << "Enter the Frame Size               : ";
cin >>n;

cout<< "Enter the Number od bits for Frame1 : ";
for(i=0; i<n; i++)
{
cin>>frame1[i];
};

for(i=0; i<n; i++)
{

if(frame1[i]==1)
{
counter++;
frame2[j] = frame1[i];
j++;
}

else 
{
counter=0;
frame2[j]=frame1[i];
j++;
}

if (counter==5)
{
counter=0;
frame2[j]=0;
j++;
}
};
for(j=0; j<n; j++)
{
cout<<"The stuffed bit frame is               : "<<frame2[j]<<" ";
};

return 0;
}
