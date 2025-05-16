#include <iostream>
using namespace std;

struct Node {
    int data;
    Node* pNext;
};

struct List {
    Node* pHead;
    Node* pTail;
};

Node* initNode(int x) {
    Node* p = new Node;
    p->data = x;
    p->pNext = nullptr;
    return p;
}



void initList(List& l) {
    l.pHead = nullptr;
    l.pTail = nullptr;
}

void addTail(List& l, Node* p) {
    if (l.pHead == nullptr) {
        l.pHead = l.pTail = p;
    }else {
        l.pTail->pNext = p;
        l.pTail = p;
    }
}

void addHead(List& l, Node* p) {
    if (l.pHead == nullptr) {
        l.pHead = l.pTail = nullptr;
    }else {
        l.pHead->pNext = p;
        l.pHead = p;
    }
}

void printList(List l) {
    Node* p = l.pHead;
    while(p != nullptr) {
        cout << p->data << " " << endl;
        p = p->pNext;
    }
}

void printList(List l) {
    Node* p = l.pHead;
    while(p != nullptr) {
      cout << p->data << " " << endl;
      p = p->pNext;  
    }
}
/*
    Tim gia tri x?
    Input:
        + Tree t
        + int x

    Output:
        + true nếu tìm thấy
        + false nếu không tìm thấy
*/

bool Search(List l, int x) {
    Node* p = l.pHead;
    while(p!=nullptr) {
        if (p->data == x) {
            return true;
        }
        p = p->pNext;

    }
    cout << "Khong tim thay x" << endl;
    return false;
}

/*
    Tim gia tri x
    input:
      x: int gia tri can tim
      l: List 
*/

bool Search(List l,int x) {
    Node* p = l.pHead;
    while (p != nullptr) {
        if (p->data == x) {
            return true;
        }
        p = p->pNext;
    }
    return false;
}

int main() {
    List l;
    initList(l);
    int n;
    cout << "Nhap so Node cua Linked List: " << endl;
    cin >> n;
    for (int i = 0;i < n; ++i) {
        int x;
        cout << "Node " << i+1 << ":" << endl;
        cin >> x;

        Node* p = initNode(x);
        addTail(l, p);
    }
    cout << "Danh sach lien ket doi: ";
    printList(l);
    return 0;
}