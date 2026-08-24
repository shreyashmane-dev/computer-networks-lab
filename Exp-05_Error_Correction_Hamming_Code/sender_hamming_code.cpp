/*
 * Experiment 05: Implementation of Error Correction Code (Hamming Code)
 * Component: Sender Side (Codeword Generator)
 * Date: 24-08-2026
 * 
 * Logic: Calculates redundant parity bits (r1, r2, r4, r8) at bit positions 
 * that are powers of 2 (1, 2, 4, 8) using even parity XOR.
 */

#include <iostream>
using namespace std;

int main() {
    int d[7];
    int c[16] = {0};
    int m, r, i;

    cout << "========================================\n";
    cout << "  HAMMING CODE (7,4 / 11,7) - SENDER\n";
    cout << "========================================\n";
    cout << "Enter number of data bits (4 or 7): ";
    cin >> m;

    if (m != 4 && m != 7) {
        cout << "Invalid input! Please enter either 4 or 7.\n";
        return 1;
    }

    cout << "Enter the " << m << " data bits (space-separated):\n";
    for(i = 0; i < m; i++) {
        cin >> d[i];
    }

    if (m == 4) {
        r = 3;
        // Data bits at positions 3, 5, 6, 7
        c[3] = d[0]; c[5] = d[1]; c[6] = d[2]; c[7] = d[3];
    } else {
        r = 4;
        // Data bits at positions 3, 5, 6, 7, 9, 10, 11
        c[3] = d[0]; c[5] = d[1]; c[6] = d[2]; c[7] = d[3];
        c[9] = d[4]; c[10] = d[5]; c[11] = d[6];
    }

    int total = m + r;

    // Calculate parity bits at 1, 2, 4, 8 using even parity XOR
    c[1] = c[2] = c[4] = c[8] = 0;
    for (i = 1; i <= total; i++) {
        if (i != 1 && i != 2 && i != 4 && i != 8) {
            if (c[i] == 1) {
                if ((i & 1) != 0) c[1] ^= 1;
                if ((i & 2) != 0) c[2] ^= 1;
                if ((i & 4) != 0) c[4] ^= 1;
                if ((i & 8) != 0) c[8] ^= 1;
            }
        }
    }

    cout << "\nGenerated Codeword (Positions 1 to " << total << "): ";
    for(i = 1; i <= total; i++) {
        cout << c[i] << " ";
    }
    cout << endl;

    return 0;
}
