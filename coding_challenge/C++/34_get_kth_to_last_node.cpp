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

void initList(List& l) {
    l.pHead = nullptr;
    l.pTail = nullptr;
};

Node* initNode(int x){
    Node* p = new Node();
    p->data = x;
    p->pNext = nullptr;
    return p;
}

void printList(List& l){
    Node* p = l.pHead;
    while (p != nullptr) {
        cout << p->data << " ";
        p = p->pNext;
    }
}

void addHead(List& l, Node* p) {
    if (l.pHead == nullptr){
        l.pHead = l.pTail = p;
    } else {
        p->pNext = l.pHead;
        l.pHead = p;
    }
}

void addTail(List& l, Node* p) {
    if (l.pHead == nullptr){
        l.pHead = l.pTail = p;
    } else {
        l.pTail -> pNext = p;
        l.pTail = p;
    }
}
/*
    Tim gia tri X
      Input:
        + List l
        + int x
      Output:
        + Return true if tim duoc
        + Else return false
*/

bool timGiaTri(List& l, int x){
    Node* p = l.pHead;
    while(p != nullptr) {
        if (p->data == x) {
            return true;
        }
        p = p->pNext;
    }
    return false;
};

int getListNodes(List& l){
    int nodes = 0;
    Node* p = l.pHead;
    while (p != nullptr){
        nodes += 1;
        p = p->pNext;
    }
    return nodes;
}

int valueOfNthNode(List l, int n, int nodes){
    Node* p = l.pHead;
    int indexFromHead = nodes - n;
    for (int i = 0; i < indexFromHead; i++) {
        p = p->pNext;
    }
    return p->data;
}

int main(){
    List l;
    initList(l);
    addHead(l, initNode(5));
    addHead(l, initNode(18));
    addHead(l, initNode(29));
    addHead(l, initNode(50));
    addTail(l, initNode(78));
    printList(l);
    int nodes = getListNodes(l);
    cout << "\nTong so node la: " << nodes << "\n";
    int value = valueOfNthNode(l, 4, nodes);
    cout << value << endl;
    return 0;
}