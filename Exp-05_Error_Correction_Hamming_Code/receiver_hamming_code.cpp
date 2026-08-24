/*
 * Experiment 05: Implementation of Error Correction Code (Hamming Code)
 * Component: Receiver Side (Error Detection & Correction)
 * Date: 24-08-2026
 * 
 * Logic: Calculates syndrome bits from received codeword. If syndrome != 0,
 * identifies exact bit in error, inverts it to correct, and recovers original data.
 */

#include <iostream>
using namespace std;

void process7Bit() {
    int c[8] = {0};
    cout << "Enter the 7-bit received codeword (bits at pos 1 to 7):\n";
    for (int i = 1; i <= 7; i++) {
        cin >> c[i];
    }

    // Parity check equations for (7,4)
    int s1 = c[1] ^ c[3] ^ c[5] ^ c[7];
    int s2 = c[2] ^ c[3] ^ c[6] ^ c[7];
    int s4 = c[4] ^ c[5] ^ c[6] ^ c[7];

    int error_pos = (s4 * 4) + (s2 * 2) + s1;

    cout << "\nSyndrome Bits (S4 S2 S1): " << s4 << " " << s2 << " " << s1 << endl;
    if (error_pos == 0) {
        cout << "Status: No error detected in transmission!\n";
    } else {
        cout << "Status: Single-bit error detected at position: " << error_pos << endl;
        c[error_pos] ^= 1; // Correct error
        cout << "Corrected Codeword: ";
        for (int i = 1; i <= 7; i++) cout << c[i] << " ";
        cout << endl;
    }

    cout << "Recovered Original 4 Data Bits: " 
         << c[3] << " " << c[5] << " " << c[6] << " " << c[7] << endl;
}

void process11Bit() {
    int c[12] = {0};
    cout << "Enter the 11-bit received codeword (bits at pos 1 to 11):\n";
    for (int i = 1; i <= 11; i++) {
        cin >> c[i];
    }

    // Parity check equations for (11,7)
    int s1 = c[1] ^ c[3] ^ c[5] ^ c[7] ^ c[9] ^ c[11];
    int s2 = c[2] ^ c[3] ^ c[6] ^ c[7] ^ c[10] ^ c[11];
    int s4 = c[4] ^ c[5] ^ c[6] ^ c[7];
    int s8 = c[8] ^ c[9] ^ c[10] ^ c[11];

    int error_pos = (s8 * 8) + (s4 * 4) + (s2 * 2) + s1;

    cout << "\nSyndrome Bits (S8 S4 S2 S1): " << s8 << " " << s4 << " " << s2 << " " << s1 << endl;
    if (error_pos == 0) {
        cout << "Status: No error detected in transmission!\n";
    } else {
        cout << "Status: Single-bit error detected at position: " << error_pos << endl;
        c[error_pos] ^= 1; // Correct error
        cout << "Corrected Codeword: ";
        for (int i = 1; i <= 11; i++) cout << c[i] << " ";
        cout << endl;
    }

    cout << "Recovered Original 7 Data Bits: " 
         << c[3] << " " << c[5] << " " << c[6] << " " << c[7] << " "
         << c[9] << " " << c[10] << " " << c[11] << endl;
}

int main() {
    int choice;
    cout << "========================================\n";
    cout << "  HAMMING CODE - RECEIVER SIDE\n";
    cout << "========================================\n";
    cout << "Select Codeword Size:\n";
    cout << "1. 7-bit codeword  (4 data bits)\n";
    cout << "2. 11-bit codeword (7 data bits)\n";
    cout << "Enter choice (1 or 2): ";
    cin >> choice;

    if (choice == 1) {
        process7Bit();
    } else if (choice == 2) {
        process11Bit();
    } else {
        cout << "Invalid choice!\n";
    }

    return 0;
}
