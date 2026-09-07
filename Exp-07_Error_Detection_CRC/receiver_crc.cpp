/*
 * Experiment 07: Implementation of Error Detection Code (CRC)
 * Component: Receiver Side (Codeword Verification)
 * Date: 07-09-2026
 * 
 * Logic: Divides received codeword by generator polynomial using modulo-2 division.
 * If remainder is all zeros, no error occurred. Otherwise, an error is detected.
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
    string recv_codeword, generator;
    
    cout << "========================================\n";
    cout << "  CRC ERROR DETECTION - RECEIVER\n";
    cout << "========================================\n";
    cout << "Enter Received Codeword : ";
    cin >> recv_codeword;
    cout << "Enter Generator Divisor : ";
    cin >> generator;
    
    string remainder = modulo2Div(recv_codeword, generator);
    
    bool has_error = false;
    for (char c : remainder) {
        if (c != '0') {
            has_error = true;
            break;
        }
    }
    
    cout << "\nCalculated Syndrome / Remainder: " << remainder << endl;
    if (has_error) {
        cout << "Result: ❌ Error detected in received data transmission!\n";
    } else {
        cout << "Result: ✅ No error detected. Data received correctly!\n";
        size_t gen_len = generator.length();
        string data = recv_codeword.substr(0, recv_codeword.length() - (gen_len - 1));
        cout << "Extracted Original Data: " << data << endl;
    }
    
    return 0;
}
