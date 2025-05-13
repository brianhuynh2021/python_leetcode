#include <iostream>

using namespace std;

struct Node {
    int data;
    Node* pNext;
};

struct List{
    Node* pHead;
    Node* pTail;
};

Node* initNode (int value){
    Node* p = new Node;
    p->data = value;
    p->pNext = nullptr;
    return p;
}

void initList(List& l){
    l.pHead = nullptr;
    l.pTail = nullptr;
}

void addTail(List& l, Node* p) {
    if (l.pHead == nullptr) {
        l.pHead = p;
        l.pTail = p;
    } else {
        l.pTail ->pNext = p;
        l.pTail = p;
    }
}
void addHead(List& l, Node* p){
    if (l.pHead == nullptr) {
        l.pHead = p;
        l.pTail = p;
    } else {
        p->pNext = l.pHead;
        l.pHead = p;
    }
}

void printList(List l) {
    Node* p = l.pHead;
    while(p!=nullptr) {
        cout << p->data << '\t';
        p=p->pNext;
    }
    cout << endl;
}

void reverseList(List l, List& result){
    initList(result);
    Node* p = l.pHead;
    while(p!=nullptr){
        Node* newNode = initNode(p->data);
        addHead(result, newNode);
        p = p->pNext;
    }
}

// Main to test
int main() {
    List l;
    initList(l);
    addHead(l, initNode(30));
    addHead(l, initNode(20));
    addHead(l, initNode(10));

    cout << "Original list:\n";
    printList(l); // 10 20 30

    List reversed;
    reverseList(l, reversed);

    cout << "Reversed cloned list:\n";
    printList(reversed); // 30 20 10

    return 0;
}