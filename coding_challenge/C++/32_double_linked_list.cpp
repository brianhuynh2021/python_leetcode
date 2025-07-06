#include <iostream>

using namespace std;

struct Node {
    int data;
    Node* pPre;
    Node* pNext;
};

struct List {
    Node* pHead;
    Node* pTail;
};

void initList(List& l) {
    l.pHead = nullptr;
    l.pTail = nullptr;
};

Node* initNode(int x) {
    Node* p = new Node;
    p->data = x;
    p->pNext = nullptr;
    p->pPre = nullptr;
    return p;
}