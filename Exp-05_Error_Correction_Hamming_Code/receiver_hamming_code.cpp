#include <iostream>
using namespace std;

void process7Bit() {
    int c[7];
    cout << "Enter the 7-bit received codeword: ";
    for (int i = 0; i < 7; i++) {
        cin >> c[i];
    }

    int s1 = c[6] ^ c[4] ^ c[2] ^ c[0];
    int s2 = c[5] ^ c[4] ^ c[1] ^ c[0];
    int s4 = c[3] ^ c[2] ^ c[1] ^ c[0];

    int t = -1;
    if (s4 == 0 && s2 == 0 && s1 == 1) t = 6;
    if (s4 == 0 && s2 == 1 && s1 == 0) t = 5;
    if (s4 == 0 && s2 == 1 && s1 == 1) t = 4;
    if (s4 == 1 && s2 == 0 && s1 == 0) t = 3;
    if (s4 == 1 && s2 == 0 && s1 == 1) t = 2;
    if (s4 == 1 && s2 == 1 && s1 == 0) t = 1;
    if (s4 == 1 && s2 == 1 && s1 == 1) t = 0;

    if (t != -1) {
        c[t] = !c[t];
    }

    cout << "Checker bits (R1 R2 R3): " << s4 << " " << s2 << " " << s1 << endl;
    cout << "The original 4 data bits: " << c[0] << " " << c[1] << " " << c[2] << " " << c[4] << endl;
}

void process11Bit() {
    int c[11];
    cout << "Enter the 11-bit received codeword: ";
    for (int i = 0; i < 11; i++) {
        cin >> c[i];
    }

    int s1 = c[10] ^ c[8] ^ c[6] ^ c[4] ^ c[2] ^ c[0];
    int s2 = c[9] ^ c[8] ^ c[5] ^ c[4] ^ c[1] ^ c[0];
    int s4 = c[7] ^ c[6] ^ c[5] ^ c[4] ^ c[0];
    int s8 = c[10] ^ c[2] ^ c[1] ^ c[0];

    int t = -1;
    if (s8 == 0 && s4 == 0 && s2 == 0 && s1 == 1) t = 10;
    if (s8 == 0 && s4 == 0 && s2 == 1 && s1 == 0) t = 9;
    if (s8 == 0 && s4 == 0 && s2 == 1 && s1 == 1) t = 8;
    if (s8 == 0 && s4 == 1 && s2 == 0 && s1 == 0) t = 7;
    if (s8 == 0 && s4 == 1 && s2 == 0 && s1 == 1) t = 6;
    if (s8 == 0 && s4 == 1 && s2 == 1 && s1 == 0) t = 5;
    if (s8 == 0 && s4 == 1 && s2 == 1 && s1 == 1) t = 4;
    if (s8 == 1 && s4 == 0 && s2 == 0 && s1 == 0) t = 3;
    if (s8 == 1 && s4 == 0 && s2 == 0 && s1 == 1) t = 2;
    if (s8 == 1 && s4 == 0 && s2 == 1 && s1 == 0) t = 1;
    if (s8 == 1 && s4 == 0 && s2 == 1 && s1 == 1) t = 0;

    if (t != -1) {
        c[t] = !c[t];
    }

    cout << "Checker bits (R1 R2 R3 R4): " << s8 << " " << s4 << " " << s2 << " " << s1 << endl;
    cout << "The original 7 data bits: " << c[0] << " " << c[1] << " " << c[2] << " " << c[4] << " " << c[5] << " " << c[6] << " " << c[8] << endl;
}

int main() {
    int choice;
    cout << "Select Hamming Code size:\n1. 7-bit codeword\n2. 11-bit codeword\nEnter choice (1 or 2): ";
    cin >> choice;

    if (choice == 1) {
        process7Bit();
    } else if (choice == 2) {
        process11Bit();
    } else {
        cout << "Invalid choice" << endl;
    }

    return 0;
}
