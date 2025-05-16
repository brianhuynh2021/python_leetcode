
/*Problem:

Given a list of numbers, return whether any two sums to k. For example, given
[10, 15, 3, 7] and k of 17, return true since 10 + 7 is 17.

 Bonus: Can you do this in one pass?*/

 #include <iostream>
 #include <unordered_set>
 using namespace std;
 
 bool isTarget(int a[], int size, int k) {
     unordered_set<int> seen;
     for (int i = 0; i < size; i++) {
         int complement = k - a[i];
         if (seen.count(complement)) {
             return true;
         }
         seen.insert(a[i]);
     }
     return false;
 }
 
 int main() {
     int arr1[] = {};
     int arr2[] = {10, 15, 3, 7};
     int arr3[] = {10, 15, 3, 4};
 
     cout << boolalpha;  // Print "true"/"false" instead of 1/0
     cout << isTarget(arr1, 0, 17) << endl;       // false
     cout << isTarget(arr2, 4, 17) << endl;       // true
     cout << isTarget(arr3, 4, 17) << endl;       // false
 
     return 0;
 }