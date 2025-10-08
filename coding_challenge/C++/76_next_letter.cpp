#include <iostream>   // for std::cout, std::endl
#include <cstdint>    // for INT32_MAX

/*
Input: a positive integer n
Output: the number of 1 bits in the binary representation of n
*/
int countOne(int n) {
    int count = 0;

    while (n != 0) {
        if (n & 1) {
            count++;
        }
        n = n >> 1; // Shift right to check next bit
    }

    return count;
}

/*
Input: a positive integer n
Output: the next greater integer with the same number of 1 bits in binary
If not found, return -1
*/
int getNextBrute(int n) {
    int count = countOne(n);
    int m = n + 1;

    while (m > 0 && m < INT32_MAX) {
        if (countOne(m) == count) {
            return m;
        }
        m++;
    }

    return -1; // No valid next number found
}

/*
Input: a positive integer n
Output: the previous smaller integer with the same number of 1 bits in binary
If not found, return -1
*/
int getPrevBrute(int n) {
    int count = countOne(n);
    int m = n - 1;

    while (m > 0) {
        if (countOne(m) == count) {
            return m;
        }
        m--;
    }

    return -1; // No valid previous number found
}

int main() {
    std::cout << "Test: Find next and prev number with same number of 1s in binary" << std::endl;

    // Input
    int n = 13948;
    // Binary of 13948 = 11011001111100 → has 8 bits of 1

    // Output
    int next = getNextBrute(n);  // Expect 13967
    int prev = getPrevBrute(n);  // Expect 13946

    std::cout << "Original number: " << n << std::endl;
    std::cout << "Next number with same 1s: " << next << std::endl;
    std::cout << "Prev number with same 1s: " << prev << std::endl;

    return 0;
}
