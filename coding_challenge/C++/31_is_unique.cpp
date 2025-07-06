#include <iostream>
#include <string>

using namespace std;

// bool isUniqueChars(const string& str) {
//     if (str.length() > 128) return false;

//     bool char_set[128] = {false};
//     for (char c : str) {
//         if (char_set[c]) return false ;
//         char_set[c] = true;
//     }
//     return true;
// }

bool isUniqueChars(const string& str) {
    if (str.length() > 128) {
        return false;
    }
    bool char_set[128] = {false};
    for (char c : str) {
        if (char_set[c]) return false;
        char_set[c] = true;
    }
    return true;
}