/*
 * Experiment 04: Implementation of Framing Methods – Bit Stuffing
 * Component: Receiver Side (Bit Destuffing)
 * Date: 17-08-2026
 * 
 * Logic: When five consecutive '1's are received followed by a '0',
 * the stuffed '0' is discarded to recover the original frame.
 */

#include <iostream>
using namespace std;

int main() {
    int frame1[80]; // Received stuffed frame
    int frame2[80]; // Destuffed original frame
    int n, counter = 0, j = 0;

    cout << "========================================\n";
    cout << "  BIT DESTUFFING - RECEIVER SIDE\n";
    cout << "========================================\n";
    cout << "Enter the Received Frame Size: ";
    cin >> n;

    cout << "Enter the Received Bits (space-separated 0/1):\n";
    for(int i = 0; i < n; i++) {
        cin >> frame1[i];
    }

    for(int i = 0; i < n; i++) {
        if(frame1[i] == 1) {
            counter++;
            frame2[j++] = frame1[i];
        } else {
            if(counter == 5) {
                // Skip/drop the stuffed 0
                counter = 0;
                continue;
            } else {
                frame2[j++] = frame1[i];
                counter = 0;
            }
        }
    }

    cout << "\nReceived Stuffed Frame: ";
    for(int i = 0; i < n; i++) {
        cout << frame1[i] << " ";
    }

    cout << "\nRecovered Original Frame: ";
    for(int i = 0; i < j; i++) {
        cout << frame2[i] << " ";
    }
    cout << "\nTotal Recovered Bits: " << j << endl;

    return 0;
}
