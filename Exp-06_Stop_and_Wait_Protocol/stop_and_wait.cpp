#include<iostream>
#include<cstdlib>
#include<ctime>
using namespace std;

int main()
{
    int n, delay;
    int timeout = 5;
    srand(time(0));
    
    cout << "Enter the NO . of frames : ";
    cin >> n;

    int frames[n];
    cout << "Enter the value for " << n << " Frame : ";
    for(int i = 0; i < n; i++)
    {
        cin >> frames[i];
    }
    
    for(int i = 0; i < n; i++)
    {
        while(1)
        {
            delay = rand() % 10;
            cout << "\nSending Frame with value: " << frames[i] << endl;
            cout << "Delay : " << delay << endl;
            
            if(timeout < delay)
            {
                cout << "Timeout" << endl;
                
                for(int j = 0; j < (delay - timeout); j++)
                {
                    cout << "Waiting....." << endl;
                }
                
                cout << "Retransmitting frame with value: " << frames[i] << endl;
            }
            else
            {
                cout << "\nThe frame with value: " << frames[i] << " received" << endl;
                
                if(i + 1 < n) {
                    cout << "The ACK for the next frame with the value : " << frames[i+1] << endl;
                } else {
                    cout << "The final ACK received successfully!" << endl;
                }
                break;
            }
        }
    }
    cout << "\nAll frames have successfully been sent!!!" << endl;
    cout << "------End of the program------" << endl;
}
