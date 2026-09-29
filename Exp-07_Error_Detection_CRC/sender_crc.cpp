#include <iostream>
#include <string>

using namespace std;

string xorData(string a, string b) {
    string result = "";
    for (int i = 1; i < b.length(); i++) {
        if (a[i] == b[i])
            result += "0";
        else
            result += "1";
    }
    return result;
}

string modulo2Div(string dividend, string divisor) {
    int pick = divisor.length();
    string tmp = dividend.substr(0, pick);
    int n = dividend.length();
    
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
    string data = "1010000";
    string generator = "1011";
    
    cout << "Original Data: " << data << endl;
    cout << "Generator Polynomial: " << generator << endl;
    
    int gen_len = generator.length();
    string padded_data = data + string(gen_len - 1, '0');
    cout << "Padded Data (with zeros): " << padded_data << endl;
    
    string remainder = modulo2Div(padded_data, generator);
    cout << "Calculated CRC Remainder: " << remainder << endl;
    
    string codeword = data + remainder;
    cout << "Final Transmitted Codeword: " << codeword << endl;
    
    return 0;
}
