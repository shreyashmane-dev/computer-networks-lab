/*
 * Experiment 08: Implementation of C Program for IP Address Calculation
 * Date: 22-09-2026
 * 
 * Logic: Analyzes IPv4 addresses, determines class (A, B, C, D, E),
 * default subnet mask, network address (first address), broadcast address (last address), 
 * and total number of assignable host addresses.
 */

#include <iostream>
#include <cmath>
#include <iomanip>
using namespace std;

int main() {
    int a, b, c, d;
    char dot1, dot2, dot3;

    cout << "========================================\n";
    cout << "  IPV4 CLASS & ADDRESS CALCULATION\n";
    cout << "========================================\n";
    cout << "Enter IP Address (e.g. 192.168.1.10): ";
    if (!(cin >> a >> dot1 >> b >> dot2 >> c >> dot3 >> d)) {
        cin.clear();
        cin >> a >> b >> c >> d;
    }

    if (a < 0 || a > 255 || b < 0 || b > 255 || c < 0 || c > 255 || d < 0 || d > 255) {
        cout << "Error: Invalid IP address range! Octets must be between 0 and 255.\n";
        return 1;
    }

    cout << "\nIP Address Entered: " << a << "." << b << "." << c << "." << d << endl;

    int mask[4] = {0, 0, 0, 0};
    int n = 0;
    char ip_class;

    if (a >= 0 && a <= 127) {
        ip_class = 'A';
        mask[0] = 255; mask[1] = 0; mask[2] = 0; mask[3] = 0;
        n = 8;
    } else if (a >= 128 && a <= 191) {
        ip_class = 'B';
        mask[0] = 255; mask[1] = 255; mask[2] = 0; mask[3] = 0;
        n = 16;
    } else if (a >= 192 && a <= 223) {
        ip_class = 'C';
        mask[0] = 255; mask[1] = 255; mask[2] = 255; mask[3] = 0;
        n = 24;
    } else if (a >= 224 && a <= 239) {
        cout << "Class               : Class D (Multicast Addressing)\n";
        cout << "Note                : Class D is reserved for multicast groups; no subnet mask.\n";
        return 0;
    } else {
        cout << "Class               : Class E (Experimental / Reserved)\n";
        return 0;
    }

    int ip[4] = {a, b, c, d};
    int first_addr[4];
    int last_addr[4];

    for (int i = 0; i < 4; i++) {
        first_addr[i] = ip[i] & mask[i];
        last_addr[i]  = ip[i] | (255 ^ mask[i]);
    }

    long long total_addresses = pow(2, 32 - n);
    long long usable_hosts = (total_addresses > 2) ? total_addresses - 2 : 0;

    cout << "Class               : Class " << ip_class << endl;
    cout << "Default Subnet Mask : " << mask[0] << "." << mask[1] << "." << mask[2] << "." << mask[3] << endl;
    cout << "Network Address     : " << first_addr[0] << "." << first_addr[1] << "." << first_addr[2] << "." << first_addr[3] << endl;
    cout << "Broadcast Address   : " << last_addr[0] << "." << last_addr[1] << "." << last_addr[2] << "." << last_addr[3] << endl;
    cout << "Total IP Addresses  : " << total_addresses << endl;
    cout << "Usable Host IP Range: " << first_addr[0] << "." << first_addr[1] << "." << first_addr[2] << "." << (first_addr[3] + 1)
         << " - " << last_addr[0] << "." << last_addr[1] << "." << last_addr[2] << "." << (last_addr[3] - 1) << endl;
    cout << "Usable Hosts Count  : " << usable_hosts << endl;

    return 0;
}
