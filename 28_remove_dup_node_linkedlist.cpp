#include <iostream>
#include <unordered_set>

struct Node {
    int data;
    Node* next;
    Node(int d) : data(d), next(nullptr) {}
};

void removeDuplicates(Node* head) {
    if (!head) return;

    std::unordered_set<int> seen;
    Node* current = head;
    Node* prev = nullptr;

    while (current) {
        if (seen.find(current->data) != seen.end()) {
            // Duplicate found, remove it
            prev->next = current->next;
            delete current;
        } else {
            // First occurrence, add to the set
            seen.insert(current->data);
            prev = current;
        }
        current = prev->next;
    }
}

// Helper function to print the linked list
void printList(Node* head) {
    while (head) {
        std::cout << head->data << " ";
        head = head->next;
    }
    std::cout << std::endl;
}

int main() {
    Node* head = new Node(10);
    head->next = new Node(12);
    head->next->next = new Node(11);
    head->next->next->next = new Node(12);
    head->next->next->next->next = new Node(10);

    std::cout << "Original List: ";
    printList(head);

    removeDuplicates(head);

    std::cout << "List after removing duplicates: ";
    printList(head);

    return 0;
}



// void removeDuplicatesNoBuffer(Node* head) {
//     if (!head) return;

//     Node* current = head;

//     while (current) {
//         Node* runner = current;
//         while (runner->next) {
//             if (runner->next->data == current->data) {
//                 // Duplicate found, remove it
//                 Node* temp = runner->next;
//                 runner->next = runner->next->next;
//                 delete temp;
//             } else {
//                 runner = runner->next;
//             }
//         }
//         current = current->next;
//     }
// }