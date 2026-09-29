#include <iostream>
#include <string>
using namespace std;

int main() {
    int n;
    cout << "Enter number of frames: ";
    cin >> n;

    int expected_seq = 0;
    int count = 0;

    while (count < n) {
        int seq;
        string data;
        cout << "Enter received seq (0 or 1): ";
        cin >> seq;
        cout << "Enter received data: ";
        cin >> data;

        if (seq == expected_seq) {
            cout << "Frame accepted: " << data << endl;
            expected_seq = 1 - expected_seq;
            count++;
            cout << "Sent ACK " << expected_seq << endl;
        } else {
            cout << "Duplicate frame. Discarded." << endl;
            cout << "Resent ACK " << expected_seq << endl;
        }
    }
    cout << "All frames received." << endl;
    return 0;
}
