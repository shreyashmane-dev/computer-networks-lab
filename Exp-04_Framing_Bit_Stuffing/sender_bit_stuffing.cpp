/*
 * Experiment 04: Implementation of Framing Methods – Bit Stuffing
 * Component: Sender Side (Bit Stuffing)
 * Date: 17-08-2026
 * 
 * Logic: Whenever five consecutive '1's appear in the data stream, 
 * a '0' bit is stuffed (inserted) to distinguish data from framing flags.
 */

#include <iostream>
using namespace std;

int main() {
    int frame1[40];
    int frame2[80];
    int n, counter = 0, j = 0;

    cout << "========================================\n";
    cout << "  BIT STUFFING - SENDER SIDE\n";
    cout << "========================================\n";
    cout << "Enter the Frame Size: ";
    cin >> n;

    cout << "Enter the bits of the Frame (space-separated 0/1):\n";
    for(int i = 0; i < n; i++) {
        cin >> frame1[i];
    }

    for(int i = 0; i < n; i++) {
        if(frame1[i] == 1) {
            counter++;
            frame2[j++] = frame1[i];
        } else {
            counter = 0;
            frame2[j++] = frame1[i];
        }

        // Stuff a 0 bit after five consecutive 1s
        if(counter == 5) {
            counter = 0;
            frame2[j++] = 0;
        }
    }

    cout << "\nOriginal Frame: ";
    for(int i = 0; i < n; i++) {
        cout << frame1[i] << " ";
    }

    cout << "\nStuffed Bit Frame (to transmit): ";
    for(int i = 0; i < j; i++) {
        cout << frame2[i] << " ";
    }
    cout << "\nTotal Transmitted Bits: " << j << endl;

    return 0;
}
