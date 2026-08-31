/*
 * Experiment 06: Implementation of Stop-and-Wait Protocol
 * Component: Receiver Side
 * Date: 31-08-2026
 * 
 * Logic: Receives frame from sender:
 * 1. If sequence number == expected_seq: accepts frame and sends ACK with next expected sequence number.
 * 2. If duplicate frame: discards duplicate data and resends ACK for next expected sequence number.
 */

#include <iostream>
#include <string>
using namespace std;

int main() {
    int total_frames;
    cout << "========================================\n";
    cout << "  STOP-AND-WAIT PROTOCOL - RECEIVER\n";
    cout << "========================================\n";
    cout << "Enter number of frames to receive: ";
    cin >> total_frames;

    int expected_seq = 0;
    int received_count = 0;

    while (received_count < total_frames) {
        int seq;
        string data;
        cout << "\n[Receiver] Enter incoming Frame sequence number (0 or 1): ";
        cin >> seq;
        cout << "[Receiver] Enter incoming Frame data: ";
        cin >> data;

        if (seq == expected_seq) {
            cout << "[Receiver] ✅ Frame accepted: '" << data << "' (Seq: " << seq << ")\n";
            expected_seq = 1 - expected_seq; // Expect next sequence number
            received_count++;
            cout << "[Receiver] 📤 Sending ACK: " << expected_seq << endl;
        } else {
            cout << "[Receiver] ⚠️ Duplicate Frame detected! (Expected Seq: " << expected_seq << ", got " << seq << "). Discarding redundant data.\n";
            cout << "[Receiver] 📤 Resending ACK: " << expected_seq << endl;
        }
    }

    cout << "\n========================================\n";
    cout << "All " << total_frames << " frames received successfully!\n";
    return 0;
}
