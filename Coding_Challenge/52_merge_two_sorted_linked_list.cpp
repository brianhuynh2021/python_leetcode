// Gop 2 danh sach lien ket don da sap xep theo thu tu tang dan

#include <iostream>
using namespace std;

// Định nghĩa node của danh sách liên kết đơn
struct ListNode {
    int val;            // Giá trị lưu trong node
    ListNode* next;     // Con trỏ trỏ đến node kế tiếp trong danh sách
    // Constructor để khởi tạo node với giá trị x và next mặc định là nullptr
    ListNode(int x) : val(x), next(nullptr) {}
};

// Hàm gộp 2 danh sách đã sắp xếp theo thứ tự tăng dần
ListNode* mergeTwoLists(ListNode* l1, ListNode* l2) {
    // Tạo một node giả (dummy) để làm điểm bắt đầu cho danh sách mới
    // Điều này giúp dễ dàng thao tác mà không cần kiểm tra danh sách rỗng
    ListNode dummy(0);
    // Con trỏ current dùng để duyệt và thêm các node vào danh sách mới
    // Ban đầu current trỏ tới dummy
    ListNode* current = &dummy;

    // Vòng lặp chạy khi cả hai danh sách l1 và l2 đều chưa kết thúc
    while (l1 && l2) {
        // So sánh giá trị của node hiện tại trong l1 và l2
        if (l1->val < l2->val) {
            // Nếu giá trị l1 nhỏ hơn, nối node l1 vào danh sách mới
            current->next = l1;
            // Di chuyển con trỏ l1 tới node kế tiếp trong danh sách l1
            l1 = l1->next;
        } else {
            // Ngược lại, nối node l2 vào danh sách mới
            current->next = l2;
            // Di chuyển con trỏ l2 tới node kế tiếp trong danh sách l2
            l2 = l2->next;
        }
        // Di chuyển current tới node mới được nối vào danh sách
        current = current->next;
    }

    // Sau khi thoát vòng lặp, một trong hai danh sách có thể còn node chưa nối
    // Nối phần còn lại của danh sách đó vào cuối danh sách mới
    current->next = (l1 != nullptr) ? l1 : l2;

    // Trả về danh sách mới, bắt đầu từ node kế tiếp dummy (bỏ qua dummy)
    return dummy.next;
}

// Hàm in danh sách liên kết ra màn hình
void printList(ListNode* head) {
    // Duyệt từng node trong danh sách đến khi gặp nullptr (kết thúc danh sách)
    while (head != nullptr) {
        // In giá trị của node hiện tại, cách nhau bằng dấu cách
        cout << head->val << " ";
        // Di chuyển tới node kế tiếp
        head = head->next;
    }
    // Xuống dòng sau khi in xong danh sách
    cout << endl;
}

// Hàm chính để chạy chương trình
int main() {
    // Tạo danh sách liên kết 1: 1 -> 3 -> 5
    // Khởi tạo node đầu tiên với giá trị 1
    ListNode* l1 = new ListNode(1);
    // Tạo node tiếp theo với giá trị 3 và nối vào sau node đầu
    l1->next = new ListNode(3);
    // Tạo node tiếp theo với giá trị 5 và nối vào sau node thứ hai
    l1->next->next = new ListNode(5);

    // Tạo danh sách liên kết 2: 2 -> 4 -> 6
    // Khởi tạo node đầu tiên với giá trị 2
    ListNode* l2 = new ListNode(2);
    // Tạo node tiếp theo với giá trị 4 và nối vào sau node đầu
    l2->next = new ListNode(4);
    // Tạo node tiếp theo với giá trị 6 và nối vào sau node thứ hai
    l2->next->next = new ListNode(6);

    // Gộp 2 danh sách đã tạo bằng hàm mergeTwoLists
    ListNode* merged = mergeTwoLists(l1, l2);

    // In danh sách đã được gộp ra màn hình
    cout << "Merged List: ";
    printList(merged);

    return 0;
}

// Muon test C++ tren Vscode can bien dich sang file execute bang lenh
// g++ ten_file.cpp -o main/ten_file_execute

// Cam on cac ban da theo doi 
