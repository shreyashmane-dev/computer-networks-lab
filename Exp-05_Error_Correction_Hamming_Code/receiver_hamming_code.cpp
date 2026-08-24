#include <iostream>
using namespace std;

int main() {
    int c[11];

    cout << "Enter the 11 bits (separated by spaces): ";
    for (int i = 0; i < 11; i++) {
        cin >> c[i];
    }

    int s1 = c[10] ^ c[8] ^ c[6] ^ c[4] ^ c[2] ^ c[0];
    int s2 = c[9] ^ c[8] ^ c[5] ^ c[4] ^ c[1] ^ c[0];
    int s4 = c[7] ^ c[6] ^ c[5] ^ c[4] ^ c[0];
    int s8 = c[10] ^ c[2] ^ c[1] ^ c[0];

    int syndrome = (s8 << 3) | (s4 << 2) | (s2 << 1) | s1;

    if (syndrome >= 1 && syndrome <= 11) {
        int t = 11 - syndrome;
        c[t] = !c[t];
    }

    cout << "The original data is : ";
    cout << c[0] << " " << c[1] << " " << c[2] << " " 
         << c[4] << " " << c[5] << " " << c[6] << " " << c[8] << endl;

    return 0;
}
