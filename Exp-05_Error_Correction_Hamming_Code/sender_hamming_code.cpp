#include <iostream>
using namespace std;

int main() {
    int d[7];
    int c[12];
    int m, r, i;

    cout << "Enter number of data bits (4 or 7): ";
    cin >> m;

    cout << "Enter the Bits : ";
    for(i = 0; i < m; i++) {
        cin >> d[i];
    }

    if (m == 4) {
        r = 3;
        c[3] = d[0]; c[5] = d[1]; c[6] = d[2]; c[7] = d[3];
    } else {
        r = 4;
        c[3] = d[0]; c[5] = d[1]; c[6] = d[2]; c[7] = d[3];
        c[9] = d[4]; c[10] = d[5]; c[11] = d[6];
    }

    int total = m + r;

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

    cout << "The codeword is : ";
    for(i = 1; i <= total; i++) {
        cout << c[i] << " ";
    }
    cout << endl;

    return 0;
}
