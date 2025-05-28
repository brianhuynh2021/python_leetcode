// Gop 2 danh sach lien ket don da sap xep theo thu tu tang dan

#include <iostream>
using namespace std;

// Định nghĩa node
struct ListNode {
    int val;
    ListNode* next;
    ListNode(int x) : val(x), next(nullptr) {}
};

// Hàm gộp 2 danh sách đã sắp xếp
ListNode* mergeTwoLists(ListNode* l1, ListNode* l2) {
    ListNode dummy(0);
    ListNode* current = &dummy;

    while (l1 && l2) {
        if (l1->val < l2->val) {
            current->next = l1;
            l1 = l1->next;
        } else {
            current->next = l2;
            l2 = l2->next;
        }
        current = current->next;
    }

    current->next = (l1 != nullptr) ? l1 : l2;
    return dummy.next;
}

// Hàm in danh sách liên kết
void printList(ListNode* head) {
    while (head != nullptr) {
        cout << head->val << " ";
        head = head->next;
    }
    cout << endl;
}

// Hàm chính
int main() {
    // Tạo danh sách 1: 1 -> 3 -> 5
    ListNode* l1 = new ListNode(1);
    l1->next = new ListNode(3);
    l1->next->next = new ListNode(5);

    // Tạo danh sách 2: 2 -> 4 -> 6
    ListNode* l2 = new ListNode(2);
    l2->next = new ListNode(4);
    l2->next->next = new ListNode(6);

    // Gộp 2 danh sách
    ListNode* merged = mergeTwoLists(l1, l2);

    // In kết quả
    cout << "Merged List: ";
    printList(merged);

    return 0;
}

// Muon test C++ tren Vscode can bien dich sang file execute bang lenh
// g++ ten_file.cpp -o main/ten_file_execute

// Cam on cac ban da theo doi 

