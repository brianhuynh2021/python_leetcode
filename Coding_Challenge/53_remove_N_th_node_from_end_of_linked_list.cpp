#include <iostream>

// hom nay minh se lam bai xoa node thu N tu cuoi linkedlist
using namespace std;

// Khai báo cấu trúc Node của danh sách liên kết
struct Node {
    int val;        // Giá trị của node
    Node* next;     // Con trỏ trỏ tới node tiếp theo

    // Constructor để khởi tạo giá trị và trỏ next là nullptr
    Node(int x): val(x), next(nullptr) {};
};

// Hàm xóa node thứ N từ cuối danh sách
Node* removeNthNode(Node* head, int N){
    Node dummy(0);             // Tạo node giả đứng trước head
    dummy.next = head;         // Nối dummy với danh sách gốc
    Node* slow = &dummy;       // Slow bắt đầu từ dummy
    Node* fast = &dummy;       // Fast cũng bắt đầu từ dummy

    // Bước 1: Cho fast đi trước N bước, bước này là dung để cho fast chay trước
    // Ý tưởng là Rùa và Thỏ, cho Thỏ chạy trước N bước, khi Thỏ về đích thì Rùa đang cách Thỏ N bước
    // Rồi ta trừ Node đó đi là được
    for (int i = 0; i < N; ++i){
        fast = fast->next;     // Mỗi lần lặp, fast tiến 1 bước
    }

    // Bước 2: Di chuyển cả fast và slow cho đến khi fast tới node cuối tức là không còn node nào
    while (fast->next != nullptr){
        slow = slow->next;     // slow tiến 1 bước
        fast = fast->next;     // fast tiến 1 bước
    }

    // Bây giờ slow đang đứng ngay trước node cần xóa
    Node* toDelete = slow->next;           // Lưu lại node cần xóa

    slow->next = toDelete->next;           // Bỏ qua node cần xóa khỏi danh sách

    delete toDelete;                       // Giải phóng bộ nhớ cho node bị xóa

    return dummy.next;                     // Trả về head mới (có thể khác nếu node đầu bị xóa)
}

// Hàm in toàn bộ danh sách liên kết
void printListNode(Node* head) {
    while(head!=nullptr){
        cout << head->val << " ";          // In giá trị của mỗi node
        head = head->next;                 // Di chuyển sang node kế tiếp
    }
    cout << endl;
}

int main() {
    // Tạo danh sách: 1 → 2 → 3 → 4 → 5
    Node* head = new Node(1);
    head->next = new Node(2);
    head->next->next = new Node(3);
    head->next->next->next = new Node(4);
    head->next->next->next->next = new Node(5);

    int N = 2; // Xóa node thứ 2 từ cuối (node có giá trị 4)
    head = removeNthNode(head, N);  // Gọi hàm xử lý

    // In danh sách sau khi xóa node
    printListNode(head);

    return 0;
}
