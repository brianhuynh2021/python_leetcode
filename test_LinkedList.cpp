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
};

void initList(List& l){
    l.pHead = l.pTail = nullptr;
};

void printList(List l) {
    Node* p = l.pHead;
    while(p!=nullptr) {
        cout << p->data << " ";;
        p = p->pNext;
    }
}

void addHead(List& l, Node* p) {
    if(l.pHead == nullptr) {
        l.pHead = l.pTail = p;
    }else {
        p ->pNext = l.pHead;
        l.pHead = p;
    }
}

void addTail(List& l, Node* p) {
    if (l.pHead == nullptr) {
        l.pHead = l.pTail = p;
    }else {
        l.pTail->pNext = p; // old Tail's pNext now move to new Node
        l.pTail = p;
    }
}

// void addHead(List& l, Node* p) {
//     if(l.pHead == nullptr) {
//         l.pHead = l.pTail = p;
//     }else {
//         p->pNext=l.pHead;
//         l.pHead = p;
//     }
// }

// void addTail(List& l, Node* p) {
//     if (l.pHead == nullptr) {
//         l.pHead = l.pTail = p;
//     } else {
//         l.pTail->pNext = p;
//         l.pTail = p;
//     }
// }

// void printList(List l) {
//     Node* p = l.pHead;
//     while(p != nullptr) {
//         cout << p->data << endl;
//         p = p->pNext;
//     }
// }

/*
    Tim gia tri x?
    Input:
        + int: x 
        + List: l
    Output:
        + true neu tim thay
        + false neu khong tim thay
*/

bool Search(List& l, int x){
    Node* p = l.pHead;
    while(p != nullptr) {
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
    cout << "Test cau 1: Them gia tri vao danh sach" << endl;
    addTail(l, initNode(25));
    addTail(l, initNode(58));
    addHead(l, initNode(17));
    addHead(l, initNode(39));

    cout << "Test cau 2: In danh sach" << endl;
    printList(l);
    cout << endl;
    int x = 25;
    if (Search(l, x)) {
        cout << "Tim thay x " << x;
    } else {
        cout << "Khong tim thay x " << x;
    }
    cout << endl;
    return 0;
}