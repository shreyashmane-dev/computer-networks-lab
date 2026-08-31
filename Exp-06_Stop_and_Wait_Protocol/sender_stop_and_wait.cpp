/*
 * Experiment 06: Implementation of Stop-and-Wait Protocol
 * Component: Sender Side
 * Date: 31-08-2026
 * 
 * Logic: Stop-and-Wait ARQ Protocol:
 * 1. Transmit frame with alternating sequence number `seq` (0 or 1).
 * 2. Start a timer.
 * 3. Wait for acknowledgement (ACK) from receiver.
 * 4. If correct ACK received, toggle sequence number and send next frame.
 * 5. If timeout / corrupted ACK, retransmit current frame.
 */

#include <iostream>
#include <cstdlib>
#include <ctime>
#include <string>
using namespace std;

struct Frame {
    int seq_no;
    string data;
};

int main() {
    srand(time(0));
    int total_frames;

    cout << "========================================\n";
    cout << "  STOP-AND-WAIT PROTOCOL - SENDER\n";
    cout << "========================================\n";
    cout << "Enter total number of frames to send: ";
    cin >> total_frames;

    int seq = 0;
    for (int i = 1; i <= total_frames; i++) {
        string msg;
        cout << "\nEnter data for Frame " << i << ": ";
        cin >> msg;

        Frame f = {seq, msg};
        bool ack_received = false;
        int attempts = 0;

        while (!ack_received) {
            attempts++;
            cout << "\n[Sender] Transmitting Frame " << i << " (Seq: " << f.seq_no << ", Data: '" << f.data << "')... Attempt " << attempts << endl;

            // Simulate network behavior (80% success, 20% timeout/loss)
            int event = rand() % 5;
            if (event == 0) {
                cout << "[Sender] ⚠️ Timeout! Frame lost in network transit. Retransmitting...\n";
            } else if (event == 1) {
                cout << "[Sender] ⚠️ ACK lost in return path. Retransmitting...\n";
            } else {
                cout << "[Sender] ✅ Received ACK: " << (1 - f.seq_no) << " (Frame " << i << " acknowledged!)\n";
                ack_received = true;
                seq = 1 - seq; // Toggle sequence number (0 -> 1 -> 0)
            }
        }
    }

    cout << "\n========================================\n";
    cout << "All " << total_frames << " frames sent and acknowledged successfully!\n";
    return 0;
}
