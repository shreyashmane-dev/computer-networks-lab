#include <iostream>
using namespace std;

int main() {
    int k, n, i, j;
    
    cout << "Enter the Number of Bits in Received Codeword : ";
    cin >> k;
    cout << "Enter the number of the divisor : ";
    cin >> n;
    
    int recv[k];
    int divisor[n];
    
    cout << "Enter the Received Codeword : ";
    for(i = 0; i < k; i++) {
        cin >> recv[i];
    }
    
    cout << "Enter the Divisor : ";
    for(j = 0; j < n; j++) {
        cin >> divisor[j];
    }
    
    for(i = 0; i <= k - n; i++) {
        if(recv[i] == 1) {
            for(j = 0; j < n; j++) {
                recv[i + j] = recv[i + j] ^ divisor[j];
            }
        }
    }
    
    int error = 0;
    int original_msg_size = k - n + 1;
    
    for(i = original_msg_size; i < k; i++) {
        if(recv[i] != 0) {
            error = 1;
            break;
        }
    }
    
    if(error == 1) {
        cout << "Error is found in transmission!" << endl;
    } else {
        cout << "No error found. Data is correct." << endl;
    }
    
    return 0;
}
