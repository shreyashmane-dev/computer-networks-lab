#include <iostream>
#include <cstdlib>
#include <ctime>
#include <string>
using namespace std;

int main() {
    srand(time(0));
    int n;
    cout << "Enter total number of frames: ";
    cin >> n;

    int seq = 0;
    for (int i = 1; i <= n; i++) {
        string data;
        cout << "Enter data for frame " << i << ": ";
        cin >> data;

        bool ack = false;
        while (!ack) {
            cout << "Sending Frame " << i << " with Seq " << seq << endl;
            int r = rand() % 4;
            if (r == 0) {
                cout << "Timeout! Frame lost. Resending..." << endl;
            } else {
                cout << "ACK " << (1 - seq) << " received." << endl;
                ack = true;
                seq = 1 - seq;
            }
        }
    }
    cout << "All frames sent successfully." << endl;
    return 0;
}
