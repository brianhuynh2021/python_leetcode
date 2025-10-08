#include <iostream>
using namespace std;

struct ListNode {
    int value;
    ListNode* next;

    ListNode(int x) : value(x), next(nullptr) {}
};

ListNode* findKthToLast(ListNode* head, int k) {
    ListNode* fast = head;
    ListNode* slow = head;

    // Move the fast pointer k steps ahead
    for (int i = 0; i < k; ++i) {
        if (!fast) {
            return nullptr;  // If k is larger than the list length
        }
        fast = fast->next;
    }

    // Move both pointers until fast reaches the end
    while (fast) {
        fast = fast->next;
        slow = slow->next;
    }

    return slow;  // slow now points to the kth to last element
}

int main() {
    // Creating a linked list: 1 -> 2 -> 3 -> 4 -> 5
    ListNode* head = new ListNode(1);
    head->next = new ListNode(2);
    head->next->next = new ListNode(3);
    head->next->next->next = new ListNode(4);
    head->next->next->next->next = new ListNode(5);

    int k = 2;
    ListNode* result = findKthToLast(head, k);

    if (result) {
        cout << "The " << k << "th to last element is: " << result->value << endl;
    } else {
        cout << "List is too short." << endl;
    }

    return 0;
}
