/*
 * Experiment 07: Implementation of Error Detection Code (CRC)
 * Component: Sender Side (Cyclic Redundancy Check)
 * Date: 07-09-2026
 * 
 * Logic: Appends (k-1) zeros to data where k is generator divisor length,
 * performs binary modulo-2 division (XOR), and appends remainder to form codeword.
 */

#include <iostream>
#include <string>
using namespace std;

string xorData(string a, string b) {
    string result = "";
    for (size_t i = 1; i < b.length(); i++) {
        result += (a[i] == b[i]) ? "0" : "1";
    }
    return result;
}

string modulo2Div(string dividend, string divisor) {
    size_t pick = divisor.length();
    string tmp = dividend.substr(0, pick);
    size_t n = dividend.length();
    
    while (pick < n) {
        if (tmp[0] == '1') {
            tmp = xorData(divisor, tmp) + dividend[pick];
        } else {
            string zeros = string(pick, '0');
            tmp = xorData(zeros, tmp) + dividend[pick];
        }
        pick++;
    }
    
    if (tmp[0] == '1') {
        tmp = xorData(divisor, tmp);
    } else {
        string zeros = string(pick, '0');
        tmp = xorData(zeros, tmp);
    }
    
    return tmp;
}

int main() {
    string data, generator;
    
    cout << "========================================\n";
    cout << "  CRC ERROR DETECTION - SENDER\n";
    cout << "========================================\n";
    cout << "Enter Data Bits (e.g. 1010000): ";
    cin >> data;
    cout << "Enter Generator Polynomial (e.g. 1011): ";
    cin >> generator;
    
    size_t gen_len = generator.length();
    string padded_data = data + string(gen_len - 1, '0');
    
    string remainder = modulo2Div(padded_data, generator);
    string codeword = data + remainder;
    
    cout << "\nOriginal Data           : " << data << endl;
    cout << "Generator Polynomial    : " << generator << endl;
    cout << "Padded Data (with zeros): " << padded_data << endl;
    cout << "Calculated CRC Checksum : " << remainder << endl;
    cout << "Transmitted Codeword    : " << codeword << endl;
    
    return 0;
}
