Câu hỏi: Viết chương trình tìm phần tử lớn hơn kế tiếp (Next Greater Element) cho mỗi phần tử trong một mảng số nguyên (mỗi phần tử, tìm số đầu tiên lớn hơn nó ở phía bên phải). (Độ khó: Mid)

Giải thích: Đây là bài toán “Next Greater Element” thường gặp trên LeetCode và đã xuất hiện trong vòng coding test của EPAM ￼. Ví dụ: với mảng [2, 5, 1, 6] thì kết quả Next Greater Element cho từng phần tử lần lượt là [5, 6, 6, -1] (-1 nghĩa là không có phần tử lớn hơn phía sau).

Hướng giải: Có thể giải bằng hai vòng lặp lồng nhau (duyệt mọi cặp phần tử) với độ phức tạp O(n^2), nhưng cách hiệu quả hơn là sử dụng ngăn xếp (stack) để đạt độ phức tạp O(n). Ý tưởng: duyệt mảng từ phải sang trái, dùng stack lưu các phần tử đã duyệt (theo thứ tự giảm dần). Với mỗi phần tử, loại bỏ (pop) khỏi stack tất cả các phần tử nhỏ hơn hoặc bằng nó (vì chúng không thể là “lớn hơn kế tiếp” của phần tử hiện tại). Phần tử trên đỉnh stack lúc đó (nếu có) chính là phần tử lớn hơn kế tiếp. Sau đó đẩy phần tử hiện tại vào stack trước khi tiếp tục duyệt phần tử bên trái tiếp theo ￼. Cách làm này đảm bảo mỗi phần tử vào stack một lần và ra stack một lần, nên tổng thể chỉ O(n).

Ví dụ minh họa:
Giả sử mảng đầu vào arr = [2, 5, 1, 6]. Ta sẽ duyệt từ phải qua:
	•	Khởi đầu stack rỗng.
	•	Xét 6: stack rỗng ⇒ NGE(6) = -1. Đẩy 6 vào stack. (Stack: [6])
	•	Xét 1: pop khỏi stack các phần tử ≤ 1. Stack hiện có 6 (>1) nên không pop. Đỉnh stack là 6 ⇒ NGE(1) = 6. Đẩy 1 vào stack. (Stack: [6, 1])
	•	Xét 5: pop các phần tử ≤ 5. Pop 1 (vì 1 ≤ 5). Đỉnh stack sau pop là 6 (>5) ⇒ NGE(5) = 6. Đẩy 5. (Stack: [6, 5])
	•	Xét 2: pop các phần tử ≤ 2. Pop 5 và 6? Thực tế 5 > 2 nên dừng ngay – không pop 5. Đỉnh stack lúc này là 5 ⇒ NGE(2) = 5. Đẩy 2. (Stack: [6, 5, 2])
Kết quả cuối cùng: [5, 6, 6, -1], khớp với trực giác của chúng ta.

Đoạn code mẫu (Python): sử dụng stack để tìm Next Greater Element cho từng phần tử:
def next_greater_elements(arr):
    n = len(arr)
    result = [-1] * n
    stack = []  # stack lưu các phần tử đã duyệt (theo thứ tự giảm dần)

    # Duyệt từ phải sang trái
    for i in range(n-1, -1, -1):
        # Loại bỏ các phần tử nhỏ hơn hoặc bằng arr[i]
        while stack and stack[-1] <= arr[i]:
            stack.pop()
        # Phần tử trên đỉnh stack bây giờ (nếu có) chính là NGE
        if stack:
            result[i] = stack[-1]
        # Đẩy phần tử hiện tại vào stack
        stack.append(arr[i])
    return result

# Kiểm tra với ví dụ:
print(next_greater_elements([2, 5, 1, 6]))  # Output: [5, 6, 6, -1]


Câu hỏi: Kiểm tra chuỗi ngoặc hợp lệ – Cho một chuỗi chỉ gồm các ký tự ngoặc (), [], {}, hãy xác định xem chuỗi có hợp lệ (các ngoặc mở – ngoặc đóng khớp nhau, đúng thứ tự) hay không. (Độ khó: Junior)

Giải thích: Đây là bài toán kinh điển “Valid Parentheses”. EPAM thường sử dụng bài này để kiểm tra kỹ năng xử lý stack cơ bản của ứng viên ￼. Chuỗi hợp lệ nghĩa là mỗi ngoặc mở phải được đóng đúng loại và đúng thứ tự (LIFO). Ví dụ: "([{}])" là hợp lệ, còn "(][)" không hợp lệ (đóng sai thứ tự).

Hướng giải: Dùng ngăn xếp để duyệt qua chuỗi ký tự: khi gặp ký tự ngoặc mở ((, [ hoặc {), đưa vào stack; khi gặp ngoặc đóng, kiểm tra đỉnh stack có ngoặc mở tương ứng không. Nếu không khớp hoặc stack rỗng khi gặp ngoặc đóng, chuỗi không hợp lệ. Sau khi duyệt hết, nếu stack vẫn còn phần tử thì cũng không hợp lệ (thiếu đóng ngoặc).

Cụ thể: tạo một bảng ánh xạ ngoặc đóng sang ngoặc mở tương ứng, ví dụ { ')' : '(', ']' : '[', '}' : '{' }. Duyệt từng ký tự ch trong chuỗi:
	•	Nếu ch là ngoặc mở, đẩy vào stack.
	•	Nếu ch là ngoặc đóng, kiểm tra nếu stack rỗng (tức không có ngoặc mở chờ đóng) thì trả về False. Nếu không, pop phần tử trên đỉnh stack và so sánh xem có khớp với ngoặc mở tương ứng của ch không (dựa theo bảng ánh xạ). Nếu không khớp, chuỗi không hợp lệ.
Tiếp tục đến hết chuỗi. Cuối cùng, nếu stack vẫn còn phần tử (vẫn còn ngoặc mở chưa được đóng) thì cũng trả về False. Ngược lại, trả về True.
def is_valid_parentheses(s: str) -> bool:
    matching = { ')':'(', ']':'[', '}':'{' }
    stack = []
    for ch in s:
        if ch in '([{':
            stack.append(ch)
        elif ch in ')]}':
            if not stack or stack.pop() != matching[ch]:
                return False
    return len(stack) == 0

# Ví dụ:
print(is_valid_parentheses("([{}])"))   # True
print(is_valid_parentheses("(][)"))     # False

Cách làm này có độ phức tạp O(n) theo độ dài chuỗi (duyệt một lần) và sử dụng ngăn xếp O(n). Đây là cách giải thông dụng và hiệu quả cho bài kiểm tra ngoặc hợp lệ.

Câu hỏi: Diện tích hình chữ nhật lớn nhất trong biểu đồ histogram – Cho một mảng số nguyên biểu thị chiều cao các cột của biểu đồ histogram, hãy tìm diện tích lớn nhất của hình chữ nhật nằm gọn trong biểu đồ đó. (Độ khó: Senior)

Giải thích: Bài toán “Largest Rectangle in Histogram” (LeetCode #84) thường được xem là khó, dùng để phân loại ứng viên Senior. Theo báo cáo phỏng vấn, EPAM từng đưa ra bài này trong vòng test đối với ứng viên cấp cao ￼. Ví dụ: Với các cột cao [2, 1, 5, 6, 2, 3] (như hình minh họa), hình chữ nhật lớn nhất có diện tích 10 (ứng với chiều cao 5 hoặc 6 và bề rộng 2 cột liền kề).

Hướng giải: Bài toán này cũng có thể giải bằng ngăn xếp đơn điệu để đạt O(n). Ý tưởng chung: dùng stack lưu chỉ số các cột theo thứ tự tăng dần chiều cao. Duyệt qua các cột (thêm một cột cao 0 ở cuối để xử lý nốt tất cả các cột):
	•	Khi chiều cao cột hiện tại lớn hơn hoặc bằng cột trên đỉnh stack, đẩy chỉ số cột hiện tại vào stack (tức vẫn đảm bảo dãy chiều cao trong stack tăng dần).
	•	Khi gặp một cột thấp hơn cột trên đỉnh stack, điều đó nghĩa là cột trên đỉnh không thể “mở rộng” thêm sang phải nữa. Pop cột trên đỉnh stack ra, tính diện tích hình chữ nhật với chiều cao = chiều cao cột vừa pop, bề rộng = khoảng cách giữa hai cột thấp hơn hai bên nó (bên phải là cột hiện tại, bên trái là cột mới trên đỉnh stack sau khi pop) ￼. Cập nhật diện tích lớn nhất. Lặp lại cho đến khi các cột trong stack có chiều cao không lớn hơn chiều cao cột hiện tại, rồi đẩy cột hiện tại vào stack.
	•	Tiếp tục cho đến hết mảng (bao gồm cột 0 giả ở cuối giúp giải phóng các cột còn lại trong stack).

Ví dụ minh họa ngắn: Với mảng [2,1,5,6,2,3]:
	•	Ban đầu stack rỗng, duyệt từng cột:
	•	Chiều cao 2: stack trống, đẩy chỉ số 0.
	•	Chiều cao 1: thấp hơn 2 (đỉnh stack), pop 2 tính diện tích = 2*1=2. Đẩy chỉ số 1.
	•	Chiều cao 5: >1, đẩy chỉ số 2.
	•	Chiều cao 6: >5, đẩy chỉ số 3.
	•	Chiều cao 2: thấp hơn 6 và 5, pop 6 (diện tích =61=6), pop 5 (diện tích =52=10) – cập nhật max=10. Đẩy chỉ số 4.
	•	Chiều cao 3: >2, đẩy chỉ số 5.
	•	Cuối cùng thêm cột 0: pop 3 (diện tích =31=3), pop 2 (diện tích =24=8), pop 1 (diện tích =1*6=6). Max vẫn = 10.

Nhận xét: Bài này phức tạp hơn, nhưng giải pháp stack giúp giảm thời gian xuống O(n). Ứng viên cần trình bày được ý tưởng sử dụng stack và tính toán diện tích khi pop, không nhất thiết viết lại toàn bộ mã do code khá dài. Quan trọng là giải thích đúng trường hợp xấu nhất có độ phức tạp tuyến tính (mỗi phần tử push/pop tối đa một lần). Đa số ứng viên Senior được kỳ vọng nắm vững kỹ thuật này.

Vòng Technical Interview 1

Trong buổi phỏng vấn kỹ thuật đầu tiên, các câu hỏi thường tập trung vào kiến thức nền tảng về ngôn ngữ Python, lập trình hướng đối tượng, cấu trúc dữ liệu cơ bản, cơ sở dữ liệu SQL, cũng như công nghệ web mà ứng viên đã sử dụng. Dưới đây là các chủ đề chính và câu hỏi tiêu biểu kèm câu trả lời chi tiết:

Python Core (Kiến thức nền tảng Python)

Câu hỏi: Sự khác biệt giữa list và tuple trong Python là gì? Khi nào nên dùng tuple thay vì list? (Độ khó: Junior)

Trả lời: Trong Python, list và tuple đều là cấu trúc dữ liệu dạng sequence dùng để chứa một danh sách các phần tử. Khác biệt chính là list có thể thay đổi (mutable) còn tuple bất biến (immutable) ￼. Điều này dẫn đến một số hệ quả quan trọng:
	•	Chỉnh sửa: Bạn có thể thêm, xóa, sửa phần tử trong list sau khi khởi tạo, trong khi tuple thì không cho phép thay đổi nội dung sau khi đã tạo. Ví dụ:

	•	Hiệu năng: Do tính bất biến, Python có thể quản lý bộ nhớ tuple hiệu quả hơn trong một số trường hợp. Việc lặp (iter) qua các phần tử tuple thường nhanh hơn list một chút ￼. Ngoài ra, Python có thể tối ưu tuple do biết trước nó không đổi – ví dụ tuple có thể được lưu trong các vùng nhớ chỉ đọc.
	•	Hashable (băm được): Các đối tượng bất biến như tuple (nếu bên trong nó chỉ chứa các phần tử hashable) có thể dùng làm key trong dictionary hoặc phần tử của set. Ngược lại, list do có thể thay đổi nên không hashable và không thể làm khóa trong dict ￼.
	•	Ngữ cảnh sử dụng: Thường dùng tuple cho dữ liệu cố định, khác loại (heterogeneous, ví dụ một record gồm nhiều trường khác nhau) hoặc khi cần bảo đảm tính toàn vẹn (read-only). Ngược lại, dùng list cho danh sách đồng chất, có thể thay đổi (homogeneous collection) hoặc khi cần thêm/xóa phần tử thường xuyên ￼. Ví dụ: một danh sách sinh viên nên dùng list (có thể thêm/xóa), còn tọa độ (x, y) hoặc các hằng số cấu hình có thể dùng tuple để tránh bị thay đổi ngoài ý muốn.

Tóm lại, list linh hoạt hơn cho dữ liệu biến động, còn tuple an toàn và tối ưu hơn cho dữ liệu cố định. Việc chọn cấu trúc nào tùy tình huống cụ thể, nhưng hiểu sự khác biệt về tính mutable là chìa khóa ￼.

Lập trình Hướng đối tượng (OOP)

Câu hỏi: Các nguyên tắc chính của lập trình hướng đối tượng là gì? Hãy nêu tên và giải thích ngắn gọn từng nguyên tắc, kèm ví dụ trong Python. (Độ khó: Junior)

Câu hỏi: So sánh list, set và dictionary trong Python về cách lưu trữ, cách truy cập và hiệu năng (độ phức tạp thời gian cho các thao tác cơ bản). (Độ khó: Mid)

Trả lời: Đây là các cấu trúc dữ liệu cơ bản rất thông dụng trong Python, mỗi loại có đặc trưng riêng:
	•	List: Danh sách liên kết tuyến tính các phần tử. List có thứ tự xác định (giữ theo thứ tự chèn vào) và có thể chứa trùng lặp. Các phần tử list được đánh chỉ số, do đó:
	•	Truy cập phần tử theo chỉ số (ví dụ list[i]): độ phức tạp O(1) – do list được quản lý như mảng động, có thể tính toán địa chỉ phần tử ngay ￼.
	•	Tìm kiếm tuyến tính (kiểm tra phần tử có trong list hoặc tìm chỉ số của phần tử): O(n) trong trường hợp xấu nhất, vì phải duyệt qua các phần tử cho đến khi tìm thấy hoặc hết danh sách.
	•	Thêm/Xóa:
	•	Thêm cuối list: amortized O(1) (Python cấp phát dư không gian để list phát triển).
	•	Thêm/Xóa ở đầu hoặc giữa list: O(n) do cần dời các phần tử còn lại.
	•	Ứng dụng: List phù hợp cho danh sách có thứ tự, thường truy cập theo chỉ số hoặc cần duyệt tuần tự. Ví dụ: lưu danh sách người dùng, cần giữ thứ tự đăng ký.
	•	Set: Tập hợp các phần tử không trùng lặp, không có thứ tự cố định. Set được cài đặt bằng bảng băm (hash table). Điều này mang lại:
	•	Kiểm tra phần tử tồn tại (x in set): trung bình O(1) – rất nhanh, do dùng hàm băm để xác định vị trí. (Trường hợp xấu nhất O(n) nếu xảy ra nhiều xung đột băm, nhưng rất hiếm khi cấu trúc tốt).
	•	Thêm/Xóa phần tử: trung bình O(1) (tương tự lý do trên).
	•	Duyệt qua set: O(n) để lần lượt lấy các phần tử (thứ tự duyệt có thể khác lần chèn).
	•	Ứng dụng: Set lý tưởng để loại bỏ trùng lặp và tìm kiếm nhanh. Ví dụ: kiểm tra nhanh xem một phần tử đã xuất hiện trước đó chưa (dùng set lưu dấu), hoặc các phép toán tập hợp (giao, hợp, hiệu) trên tập dữ liệu.
	•	Dictionary (dict): Cấu trúc ánh xạ khóa – giá trị (key-value) cũng được cài bằng hash table (từ Python 3.7+ còn duy trì thứ tự chèn của keys, nhưng thường ta không dựa vào thứ tự này trừ khi có lý do cụ thể). Đặc điểm:
	•	Truy cập giá trị theo key: trung bình O(1). Ví dụ my_dict[key] truy xuất rất nhanh bất kể kích thước dict lớn nhỏ, vì key được băm để tìm ra vị trí lưu value tương ứng ￼.
	•	Thêm/Sửa/Xóa cặp key-value: trung bình O(1) tương tự (sửa value theo key nếu đã tồn tại cũng O(1)). Khi số lượng phần tử tăng nhiều có thể Python sẽ tự động nới kích thước bảng băm để giữ hiệu suất.
	•	Duyệt dict: O(n) để duyệt qua toàn bộ các key (thứ tự theo thứ tự chèn kể từ Python 3.7).
	•	Ứng dụng: Dict được dùng khi cần tra cứu thông tin theo một khóa định danh. Ví dụ: tra số điện thoại (value) theo tên người (key), hoặc đếm tần suất phần tử (dùng key là phần tử, value là đếm).

Tóm lại:
	•	List thích hợp khi cần thứ tự ổn định và truy cập theo chỉ số vị trí hoặc duyệt thứ tự. Tuy nhiên tìm kiếm phần tử trong list chậm (O(n)).
	•	Set và dict sử dụng băm nên cho phép tìm kiếm và truy xuất rất nhanh (trung bình O(1)), phù hợp khi làm việc với tập dữ liệu lớn cần kiểm tra thành viên hoặc ánh xạ khóa. Nhược điểm là set/dict tốn thêm bộ nhớ cho bảng băm và không duy trì thứ tự logic (dù Python 3.7+ giữ thứ tự chèn, nhưng đó là chi tiết cài đặt).

Ứng viên nên nắm các độ phức tạp này vì phỏng vấn viên có thể hỏi: “Tại sao tìm trong list lại chậm hơn trong set?” hoặc “Trong trường hợp X, dùng cấu trúc nào tốt hơn?”. Câu trả lời mong đợi: do cấu trúc băm của set/dict cho phép truy xuất O(1) trung bình, còn list phải duyệt tuần tự O(n).

SQL (Cơ sở dữ liệu quan hệ)

Câu hỏi: Phân biệt các loại JOIN trong SQL (INNER JOIN, LEFT JOIN, RIGHT JOIN, FULL JOIN). (Độ khó: Junior)

Trả lời: Các phép JOIN trong SQL dùng để kết hợp các bảng dựa trên mối quan hệ giữa các cột. Giả sử có hai bảng A và B, ta phân biệt như sau:
	•	INNER JOIN: Chỉ trả về những bản ghi khớp giữa hai bảng – tức là những hàng có khóa liên kết xuất hiện ở cả A và B. Các bản ghi không có đối ứng ở bảng kia sẽ bị loại bỏ. Đây là join phổ biến nhất. Ví dụ: truy vấn danh sách nhân viên kèm tên phòng ban, dùng INNER JOIN giữa bảng Employee và Department trên DeptID. Những nhân viên chưa được gán phòng ban (DeptID không khớp) sẽ không xuất hiện.
	•	LEFT JOIN (LEFT OUTER JOIN): Trả về toàn bộ các bản ghi từ bảng bên trái (bảng A), cùng các bản ghi khớp từ bảng bên phải (B). Nếu bảng phải không có bản ghi tương ứng, các cột của B sẽ trả về NULL. Nói cách khác, LEFT JOIN đảm bảo lấy tất cả hàng của A, ngay cả khi không có match ở B. Ví dụ: lấy danh sách tất cả nhân viên và tên phòng ban của họ (nếu có). Nhân viên nào chưa có phòng ban vẫn liệt kê, với tên phòng ban là NULL.
	•	RIGHT JOIN (RIGHT OUTER JOIN): Ngược lại với LEFT JOIN – trả về mọi bản ghi từ bảng bên phải (B), và các bản ghi khớp từ bảng trái (A). Nếu A không có tương ứng thì các cột A sẽ NULL. (RIGHT JOIN ít dùng hơn, vì có thể đạt được kết quả tương tự bằng cách đổi thứ tự bảng và dùng LEFT JOIN).
	•	FULL JOIN (FULL OUTER JOIN): Lấy toàn bộ bản ghi từ cả hai bảng, kết hợp theo khóa nếu có khớp. Nghĩa là hàng nào match thì gộp lại một hàng, còn hàng nào chỉ có ở A hoặc chỉ có ở B cũng đều xuất hiện trong kết quả (với các cột bảng kia NULL). Full join giống như hợp của left join và right join. Lưu ý: Một số hệ quản trị (như MySQL) không hỗ trợ trực tiếp FULL JOIN, nhưng có thể giả lập bằng UNION của LEFT và RIGHT.

Hình dung: Nếu coi tập bản ghi A và B, thì:
	•	INNER JOIN = phần giao (intersection) của A và B theo khóa.
	•	LEFT JOIN = toàn bộ A + (phần B giao A).
	•	RIGHT JOIN = toàn bộ B + (phần A giao B).
	•	FULL JOIN = hợp (union) của A và B theo khóa.

Ví dụ cụ thể:
Bảng A (Students): {StudentID, Name, ClassID}
Bảng B (Classes): {ClassID, ClassName}
	•	INNER JOIN A,B on ClassID: Lấy sinh viên có lớp, ghép thêm tên lớp. (Bỏ sinh viên không có ClassID hợp lệ, bỏ lớp không có sinh viên nào).
	•	LEFT JOIN A,B: Lấy mọi sinh viên, nếu có lớp thì ghép tên lớp, nếu không thì tên lớp NULL. (Nhưng lớp không có sinh viên thì không hiện).
	•	RIGHT JOIN A,B: Lấy mọi lớp, nếu có sinh viên thì hiện kèm, nếu lớp trống thì vẫn hiện lớp (sinh viên NULL).
	•	FULL JOIN: Lấy mọi sinh viên và mọi lớp, ghép khi khớp ClassID. Sinh viên không lớp và lớp trống đều xuất hiện.

Nhìn chung, ứng viên cần nêu đúng bản chất giữ bên nào, bỏ bên nào. Đây là câu hỏi cơ bản về SQL nhằm kiểm tra tư duy hệ quản trị dữ liệu quan hệ.

Web Frameworks (Django/Flask/FastAPI)

Câu hỏi: So sánh Django, Flask và FastAPI – điểm khác biệt chính và trường hợp sử dụng mỗi framework. (Độ khó: Mid)

Trả lời: Đây đều là các framework Python phổ biến để xây dựng ứng dụng web, nhưng chúng khác nhau về triết lý thiết kế và tính năng:
	•	Django: Django là một full-stack framework “batteries-included” lâu đời (ra đời 2005). Nó cung cấp mọi thứ sẵn có: hệ thống ORM (Object-Relational Mapping) để thao tác database, hệ thống template HTML, cơ chế routing, authentication, admin site tự động, v.v. Django tuân theo nguyên tắc “DRY (Don’t Repeat Yourself)” và “Convention over Configuration”, giúp lập trình viên phát triển nhanh các ứng dụng web hoàn chỉnh.
	•	Ưu điểm: Phù hợp các ứng dụng lớn, phức tạp cần nhiều thành phần (ví dụ trang web thương mại điện tử, cổng thông tin…). Cộng đồng lớn, tài liệu phong phú, nhiều plugin (Django apps) sẵn có.
	•	Nhược điểm: Django có cấu trúc khá cứng, học ban đầu hơi cao; ít linh hoạt nếu chỉ cần API nhỏ. Hiệu năng cho các request sync thông thường tốt, nhưng chưa tối ưu cho async (mặc dù Django 3.x+ đã hỗ trợ async phần nào).
	•	Flask: Flask là một micro-framework (ra đời 2010) – core của Flask rất nhẹ, chỉ cung cấp những tính năng tối thiểu: routing (định tuyến URL), WSGI, xử lý request/response. Mọi thứ khác (kết nối database, form, auth…) cần thêm extensions bên ngoài.
	•	Ưu điểm: Nhỏ gọn, linh hoạt, dễ học. Lập trình viên có thể tự quyết định kiến trúc, chỉ tích hợp những thành phần cần dùng => ứng dụng Flask có thể rất nhẹ cho các dịch vụ nhỏ. Phù hợp viết RESTful API service nhanh chóng, hoặc các ứng dụng nhỏ đến vừa.
	•	Nhược điểm: Với dự án lớn, Flask đòi hỏi lập trình viên tự tổ chức nhiều thứ (quản lý thư mục, kiến trúc code, chọn thư viện phù hợp), nên cần kinh nghiệm để duy trì dự án lớn tránh spagetti. Flask cũng thiếu sẵn tính năng, nên đôi khi phải tích hợp nhiều extension (khả năng xung đột phiên bản).
	•	FastAPI: FastAPI (ra mắt ~2018) là framework mới nổi chuyên cho RESTful API với hiệu năng cao. Điểm độc đáo của FastAPI là sử dụng asyncio (async/await) ngay từ đầu và tích hợp Pydantic để parse dữ liệu và tự động sinh OpenAPI docs.
	•	Ưu điểm: Hiệu năng rất tốt (dựa trên ASGI Uvicorn, Starlette) – xử lý I/O bất đồng bộ hiệu quả, phù hợp dịch vụ yêu cầu throughput cao. Code rõ ràng, khai báo bằng cách sử dụng type hints của Python – FastAPI tự tạo tài liệu API và validate request/response dựa trên kiểu dữ liệu. Thích hợp cho microservices, API server hiện đại.
	•	Nhược điểm: Vì mới nên cộng đồng nhỏ hơn, tài liệu chưa đồ sộ như Django. Không phải full-stack: nếu cần hệ thống template render HTML hay ORM mạnh như Django ORM thì phải tích hợp thêm (FastAPI có thể dùng SQLAlchemy cho ORM, Jinja2 cho template, nhưng các phần đó không built-in chặt chẽ như Django).

Tóm lại:
	•	Django cho ứng dụng monolithic lớn, cần xây nhanh với nhiều tính năng sẵn có.
	•	Flask cho dự án nhỏ hoặc trung bình, muốn linh hoạt tùy biến, hoặc để học do đơn giản.
	•	FastAPI lý tưởng cho việc xây dựng API hiện đại, hiệu năng cao (đặc biệt nếu dùng async, microservice).

Nếu so sánh vui, có thể xem Django như “xe buýt nhiều chỗ” (nặng nhưng chở được nhiều), Flask như “xe máy” (nhanh gọn, tuỳ biến), còn FastAPI như “mô-tô thể thao” (tối ưu tốc độ cho quãng đường nhất định). Tuỳ yêu cầu dự án mà chọn công cụ cho phù hợp.

REST API (Giao tiếp dịch vụ Web)

Câu hỏi: Các phương thức HTTP chính trong một RESTful API là gì? Nêu chức năng của mỗi phương thức. (Độ khó: Junior)

Trả lời: Trong thiết kế RESTful API (trên giao thức HTTP), chúng ta thường sử dụng các HTTP method (động từ HTTP) để chỉ định hành động muốn thực hiện trên tài nguyên. Các phương thức chính gồm:
	•	GET: Lấy dữ liệu (Retrieve) từ server. GET được dùng để đọc hoặc truy vấn tài nguyên, không thay đổi trạng thái trên server (HTTP SAFE – an toàn, không gây hiệu ứng phụ). Ví dụ: GET /users/123 để lấy thông tin user 123. GET có thể được cache và bookmark.
	•	POST: Tạo mới một tài nguyên. Client gửi dữ liệu trong request body để server tạo một resource mới. Ví dụ: POST /users với JSON payload thông tin user mới, server sẽ tạo user và trả về user ID. POST không idempotent – gọi nhiều lần có thể tạo nhiều tài nguyên trùng (nếu không cẩn thận).
	•	PUT: Cập nhật một tài nguyên toàn bộ. Client gửi toàn bộ trạng thái mong muốn của resource, server thay thế resource hiện có bằng dữ liệu mới. Nếu resource chưa tồn tại, tùy chuẩn có thể tạo mới (PUT thường được thiết kế idempotent – gọi nhiều lần kết quả như nhau). Ví dụ: PUT /users/123 với body là đầy đủ thông tin user 123 để thay thế bản ghi hiện tại.
	•	PATCH: Cập nhật một phần tài nguyên. Khác với PUT (thay thế toàn bộ), PATCH chỉ chứa các thay đổi cục bộ. Ví dụ: PATCH /users/123 với body chỉ chứa { "phone": "0987654321" } để cập nhật số điện thoại của user 123. PATCH cũng thường idempotent nếu áp dụng đúng (cùng một PATCH lặp lại nhiều lần vẫn ra kết quả cuối giống nhau).
	•	DELETE: Xoá tài nguyên. Ví dụ: DELETE /users/123 để xóa user 123 khỏi hệ thống. DELETE nên được cài đặt idempotent (xóa nhiều lần thì kết quả cuối cùng vẫn là đã xóa hoặc không tồn tại).

Ngoài ra còn có các phương thức ít phổ biến hơn:
	•	HEAD: Giống GET nhưng chỉ yêu cầu header, không lấy body. Dùng để kiểm tra nhanh (ví dụ xem tài nguyên có tồn tại không, hoặc lấy thông tin metadata như Content-Length mà không tải nội dung).
	•	OPTIONS: Yêu cầu server liệt kê các phương thức/hành động được hỗ trợ trên resource hoặc máy chủ (hay dùng trong CORS – Cross-Origin Resource Sharing, để khai báo phương thức được phép).
	•	CONNECT, TRACE: Ít dùng trong REST (CONNECT cho thiết lập tunnel, TRACE để debug, hầu như không gặp trong thiết kế API thông thường).

Tính chất an toàn & idempotent:
	•	GET, HEAD, OPTIONS là safe (không thay đổi server).
	•	PUT, DELETE, idempotent PATCH là idempotent (gọi nhiều lần hiệu ứng như một lần).
	•	POST thì không an toàn cũng không idempotent (mỗi lần gọi thường tạo mới).

Khi thiết kế API, việc chọn đúng method rất quan trọng để tuân thủ chuẩn REST. Ví dụ: tạo mới phải dùng POST, không nên lạm dụng GET để thay đổi dữ liệu. EPAM thường hỏi các câu như sự khác nhau giữa POST và PUT (create vs update, idempotent) nhằm kiểm tra hiểu biết nền tảng về REST.

Unit Testing (Kiểm thử đơn vị)

Câu hỏi: Unit test là gì và tại sao quan trọng? Bạn có thể kể tên một số framework/unit test library phổ biến trong Python không? (Độ khó: Junior)

Trả lời: Unit test (kiểm thử đơn vị) là quá trình kiểm tra các thành phần nhỏ nhất của phần mềm (thường là các hàm hoặc lớp) một cách độc lập, nhằm đảm bảo rằng mỗi đơn vị hoạt động đúng như kỳ vọng. Mục tiêu của unit test là bắt lỗi ngay ở mức độ hàm, trước khi các thành phần ghép lại với nhau.

Tầm quan trọng: Unit test giống như “người gác cổng” chất lượng code. Một bộ test đơn vị tốt giúp:
	•	Phát hiện sớm các bug khi code thay đổi (hàm không cho kết quả như mong đợi sẽ bị test báo đỏ).
	•	Đảm bảo tính đúng đắn của hàm trong mọi trường hợp (bao gồm cả các trường hợp biên, đầu vào bất thường mà ta viết test cho chúng).
	•	Tạo ra tài liệu sống: test đóng vai trò ví dụ sử dụng hàm, người khác đọc có thể hiểu cách hàm hoạt động dựa trên các test case.
	•	Hỗ trợ refactor tự tin: khi chỉnh sửa code, chạy lại test để chắc không phá vỡ chức năng cũ (regression). Nếu test đều pass nghĩa là các trường hợp đã lường trước vẫn OK.

Nói ngắn gọn, unit test nâng cao độ tin cậy và ổn định cho codebase, đặc biệt quan trọng trong môi trường làm việc nhóm và dự án lớn.

Framework Python phổ biến cho unit test:
	•	unittest: Thư viện tích hợp sẵn (built-in) trong Python (module unittest) – cung cấp kiểu xUnit (giống JUnit của Java) với lớp TestCase, các phương thức assert*. Unittest khá đầy đủ tính năng (test fixture, skipping, subTest, etc.).
	•	pytest: Framework bên thứ ba rất phổ biến, được ưa chuộng nhờ cú pháp gọn nhẹ và nhiều plugin mạnh mẽ. Pytest cho phép viết test đơn giản bằng các hàm, sử dụng các assert thông thường (pytest sẽ phân tích biểu thức assert nếu fail để in thông tin). Pytest hỗ trợ parametrized test, fixtures linh hoạt, v.v.
	•	nose / nose2: Trước đây nose là một test runner mở rộng unittest, nhưng hiện nay nose không còn phát triển tích cực. Pytest phần lớn đã thay thế nose trong cộng đồng Python.
	•	hypothesis: Thư viện cho property-based testing – tự động tạo dữ liệu đầu vào dựa theo đặc tả để thử nhiều trường hợp, giúp phát hiện các edge case mà lập trình viên có thể không nghĩ đến.

Ngoài ra, trong bối cảnh phát triển web, có Django Test framework (tích hợp trên unittest) nếu dùng Django, hoặc Robot Framework (test tự động cấp cao)…
Câu hỏi: Phân biệt git merge và git rebase. Bạn sử dụng mỗi lệnh trong trường hợp nào? (Độ khó: Mid)

Trả lời: Cả git merge và git rebase đều dùng để tích hợp thay đổi từ nhánh này sang nhánh khác trong Git, nhưng cách thức rất khác nhau:
	•	Git merge: Tạo một merge commit để hợp nhất lịch sử của hai nhánh. Khi merge, Git sẽ giữ nguyên toàn bộ lịch sử commit của cả hai nhánh và tạo thêm một commit mới (commit M) trên nhánh mục tiêu, thể hiện sự kết hợp của hai luồng lịch sử. Kết quả thường tạo ra một cấu trúc “nhánh cây” (dạng diamond kim cương khi nhìn lịch sử) vì có điểm phân nhánh và điểm hợp lại ￼ ￼.
	•	Ưu: Merge không thay đổi lịch sử các nhánh gốc – an toàn, dễ lần theo commit gốc. Thích hợp khi làm việc nhóm, không yêu cầu lịch sử phẳng.
	•	Nhược: Lịch sử commit có thể bị rối (nhiều nhánh đan vào nhau). Mỗi lần merge thêm một commit “Merge branch …”, khi xem log có nhiều “nút hợp” khó hình dung trình tự thời gian.
	•	Git rebase: Rebase sẽ di chuyển (áp dụng lại) các commit của nhánh hiện tại lên đỉnh nhánh mục tiêu, tạo ra một chuỗi commit mới, không tạo merge commit. Cụ thể, Git sẽ lấy từng commit của nhánh feature và “phát lại” (replay) trên nền nhánh đích (thường là master), kết quả là lịch sử trở nên thẳng một dòng – như thể các commit feature được tạo sau commit cuối của master. Lúc này, các commit cũ trên nhánh feature được ghi lại thành commit mới (có hash mới). Kết quả, ta tránh được “diamond shape”, lịch sử nhìn linear rõ ràng hơn ￼.
	•	Ưu: Lịch sử gọn gàng, tuần tự, rất dễ đọc – không có các merge commit thừa. Khi xem git log sẽ không thấy chỗ phân nhánh – phù hợp khi làm cleanup trước khi đẩy lên kho chính (ví dụ squash hoặc chỉnh lại commit).
	•	Nhược: Rebase thực chất viết lại lịch sử (thay đổi commit hash), nên không được rebase những commit đã public (đã push cho người khác) nếu không sẽ gây xung đột lịch sử. Rebase cũng đòi hỏi cẩn thận: trong quá trình rebase có thể gặp conflict ở từng commit, cần giải quyết tuần tự.

Khi nào dùng gì:
	•	Dùng merge cho tình huống tích hợp bình thường, đặc biệt trong làm việc nhóm trên nhánh chung – merge đảm bảo an toàn, lịch sử gốc được giữ nguyên (dễ debug về sau). Chấp nhận log có commit merge.
	•	Dùng rebase khi muốn có một lịch sử sạch sẽ, chẳng hạn trước khi gửi pull request, có thể rebase để cập nhật code mới nhất từ master và squash các commit nhỏ thành một commit logic. Rebase cũng hữu ích khi cherry-pick một loạt commit hoặc thay đổi thứ tự commit trước khi chia sẻ. Nhớ chỉ rebase nhánh local chưa push, hoặc rebase nhánh feature chung cẩn thận sau khi thông báo mọi người (tránh rebase nhánh đã có người clone và làm việc).

Ví dụ minh họa: Bạn tạo nhánh feature từ master, commit vài lần, trong khi master có các commit mới do người khác merge. Giờ muốn cập nhật feature với thay đổi từ master:
	•	Nếu dùng merge: trên feature, chạy git merge master. Sẽ tạo 1 commit merge. Lịch sử feature chứa cả commit gốc của feature lẫn commit từ master, không theo thứ tự thời gian hoàn toàn (nhánh feature tách rồi nhập).
	•	Nếu dùng rebase: trên feature, chạy git rebase master. Git sẽ lấy các commit của feature, tạm rút chúng ra, đồng bộ code feature theo master, rồi lần lượt áp các commit feature trở lại. Kết quả: trên feature bây giờ toàn bộ commit master ở dưới, commit feature ở trên, như feature bắt đầu sau master. Lịch sử thẳng, không có merge commit.

Tóm lại, merge bảo toàn lịch sử, rebase tạo lịch sử mới (phẳng) ￼. Cả hai có chỗ dùng riêng:
	•	Team thường dùng merge cho nhánh chung để dễ theo dõi ai làm gì, tránh rủi ro rewrite.
	•	Cá nhân hoặc dự án open-source hay dùng rebase để lịch sử commit sạch sẽ trước khi merge vào main (ví dụ dự án Linux kernel rất chuộng rebase tương tác để các patch series gọn gàng).

Người phỏng vấn muốn nghe ứng viên hiểu rõ sự khác biệt này, nhất là vấn đề rebase thay đổi commit history và lợi ích “giữ lịch sử thẳng” của nó. Một câu trả lời tốt sẽ nhấn mạnh: merge thì tạo commit hợp nhất, rebase thì di chuyển commit – không tạo commit mới ngoài commit của chính mình.
Câu hỏi: GIL (Global Interpreter Lock) trong Python là gì và tại sao nó quan trọng? Nó ảnh hưởng thế nào đến việc sử dụng đa luồng (multithreading) trong Python? (Độ khó: Mid/Senior)

Trả lời: GIL – Global Interpreter Lock là một cơ chế khóa đặc thù của trình thông dịch CPython (phiên bản Python phổ biến nhất). GIL đảm bảo rằng tại mỗi thời điểm, chỉ có một thread (luồng) được thực thi mã bytecode Python duy nhất trong một process CPython ￼. Nói cách khác, dù chương trình Python có tạo nhiều thread, GIL sẽ tuần tự hóa việc thực thi Python bytecode – không có hai thread chạy song song thực sự cùng lúc trên nhiều CPU.

Lý do tồn tại GIL: GIL giúp đơn giản hóa việc quản lý bộ nhớ và đối tượng trong CPython, vì CPython không phải lo đến trạng thái bất đồng bộ của các object (do chỉ một thread chạy tại một thời điểm). Nó đảm bảo CPython là thread-safe ở mức interpreter. GIL ra đời từ những ngày đầu Python, khi ưu tiên sự đơn giản cài đặt hơn là hiệu năng đa luồng.

Ảnh hưởng đến đa luồng: GIL là con dao hai lưỡi:
	•	Với các tác vụ CPU-bound (đòi hỏi CPU nhiều, ví dụ tính toán lớn, giải mã, xử lý hình ảnh): đa luồng trong Python không tăng tốc khi chạy trên CPU đa nhân, vì GIL chặn không cho nhiều thread chạy đồng thời trên các core khác nhau. Thậm chí nhiều thread CPU-bound có thể chạy chậm hơn do overhead chuyển GIL qua lại giữa thread (context switch).
	•	Với các tác vụ I/O-bound (đợi I/O nhiều, ví dụ chờ đọc ghi file, network): đa luồng vẫn có lợi trong Python. Khi một thread chờ I/O, nó sẽ nhường GIL (release) cho thread khác chạy. Nhờ đó các thread có thể luân phiên tiến hành I/O, khiến tổng thể chương trình sử dụng thời gian hiệu quả hơn. Nên trong các ứng dụng như web crawler, server I/O, có thể dùng multithreading để xử lý nhiều kết nối đồng thời – GIL không cản trở nhiều vì phần lớn thời gian thread ở trạng thái chờ I/O ￼.
	•	Đa tiến trình (multiprocessing): Để tận dụng nhiều CPU core với tác vụ CPU-bound, người ta thường dùng multiprocessing (tạo nhiều tiến trình Python, mỗi tiến trình có GIL riêng). Do mỗi process có interpreter riêng, GIL không bị chia sẻ giữa các process. Nhược điểm là tốn bộ nhớ và overhead giao tiếp liên tiến trình, nhưng Python cung cấp module multiprocessing để đơn giản hóa việc này.

Ví dụ minh họa: Nếu chạy một vòng lặp tính toán nặng  trên 2 thread, thời gian gần như tương đương 1 thread (thậm chí tệ hơn do GIL switching). Ngược lại, nếu chạy tải về file từ mạng bằng 10 thread, có thể nhanh hơn đáng kể so với chạy tuần tự, vì khi thread này chờ mạng thì thread khác tranh thủ chạy.

Ngoại lệ: GIL thuộc về CPython. Các triển khai Python khác như Jython (Python trên JVM) hay IronPython (trên .NET) không có GIL, nhưng chúng ít phổ biến trong giới dev chung. Ngoài ra, trong CPython, ta có thể dùng các thư viện native (C/C++ tính toán, ví dụ NumPy) – các thư viện này có thể thả GIL khi thực thi code C bên dưới, nên có thể tận dụng đa nhân trong tác vụ nội bên dưới (như tính ma trận bằng NumPy dùng nhiều core do GIL được nhả trong đoạn tính toán C).

Tóm lại, GIL là một trong những khía cạnh “tranh cãi” của Python. Nó đơn giản hóa việc viết interpreter và modules C, nhưng hạn chế khả năng đa luồng song song thực sự trên CPU. Hiểu GIL quan trọng khi thiết kế chương trình Python: nếu cần hiệu năng đa nhân, phải xem xét dùng đa tiến trình hoặc tận dụng async IO hoặc nhờ thư viện native.

(Tham khảo: GIL đảm bảo chỉ một thread thực thi trong interpreter CPython tại một thời điểm ￼. Nó khiến multithreading Python không tận dụng được đa core trong tác vụ CPU-bound.)

OOP nâng cao / Design Principles

Câu hỏi: SOLID principles là gì? Liệt kê 5 nguyên tắc SOLID trong thiết kế hướng đối tượng và giải thích ngắn gọn. (Độ khó: Senior)

Trả lời: SOLID là chữ viết tắt đại diện cho 5 nguyên tắc cơ bản trong thiết kế phần mềm hướng đối tượng, do Robert C. Martin (Uncle Bob) đề xuất ￼. Mục tiêu của SOLID là giúp code dễ hiểu, dễ bảo trì, dễ mở rộng. 5 nguyên tắc bao gồm:
	•	S – Single Responsibility Principle (SRP) – Nguyên tắc trách nhiệm đơn lẻ: Mỗi lớp (hoặc module) chỉ nên đảm nhiệm một trách nhiệm (một lý do để thay đổi) duy nhất ￼. Nói cách khác, không nhồi nhét nhiều chức năng không liên quan vào một lớp. Ví dụ: Lớp Invoice chỉ nên lo nghiệp vụ hóa đơn, không kiêm luôn việc gửi email hay in ấn – những việc đó nên tách ra lớp khác. Tuân thủ SRP giúp code dễ bảo trì: khi yêu cầu thay đổi đến, chỉ một lớp bị ảnh hưởng thay vì nhiều nơi.
	•	O – Open/Closed Principle (OCP) – Nguyên tắc đóng/mở: Class nên “mở” để mở rộng, nhưng “đóng” để sửa đổi ￼. Nghĩa là có thể mở rộng chức năng của class bằng cách thêm mã (thông qua kế thừa, composition, thêm lớp mới) chứ không nên chỉnh sửa mã nguồn lớp có sẵn. Làm vậy tránh làm hỏng hành vi cũ và giảm thiểu retest những phần không liên quan. Ví dụ: Thay vì sửa lớp ReportGenerator mỗi khi thêm định dạng báo cáo mới (PDF, Excel,…), ta thiết kế cho nó một interface và kế thừa các lớp con cụ thể cho từng định dạng – khi thêm định dạng chỉ cần tạo lớp mới, không sửa lớp gốc.
	•	L – Liskov Substitution Principle (LSP) – Nguyên tắc thay thế Liskov: Các lớp con phải có thể thay thế hoàn toàn cho lớp cha mà không làm thay đổi tính đúng đắn của chương trình. Nói cách khác, đối tượng của lớp con có thể sử dụng ở mọi nơi yêu cầu đối tượng lớp cha, và hành vi chương trình không bị phá vỡ. Nếu lớp con làm yếu đi giao kèo (contract) của lớp cha hoặc thay đổi quy ước đầu ra đầu vào, thì vi phạm LSP. Ví dụ: Giả sử có lớp cha Bird với phương thức fly(). Nếu ta tạo lớp con Penguin kế thừa Bird nhưng Penguin không thể bay – mọi chỗ code tưởng Bird bay được sẽ hỏng khi gặp Penguin. Đây là vi phạm LSP. Cách sửa là thiết kế lại kế thừa (ví dụ tách Bird thành FlyingBird và NonFlyingBird…).
	•	I – Interface Segregation Principle (ISP) – Nguyên tắc phân tách interface: Không nên ép các class phụ thuộc vào những interface mà họ không dùng đến. Thay vì một interface lớn bao trùm nhiều chức năng, hãy tách thành nhiều interface nhỏ, mỗi cái chuyên về một nhiệm vụ, để lớp triển khai chỉ cần triển khai cái họ thực sự cần ￼. Ví dụ: Có interface lớn IMultiFunctionPrinter bao gồm print(), fax(), scan(). Nếu ta có class OldPrinter chỉ có chức năng in, không fax, scan – việc buộc implement interface lớn (và để trống fax/scan) là không đúng ISP. Ta nên tách thành IPrinter, IFax, IScanner riêng. OldPrinter chỉ cần implement IPrinter. ISP giúp tránh code “cồng kềnh” và giảm tác động khi thay đổi interface (thay vì đổi interface lớn rồi kéo theo thay đổi nhiều class không liên quan).
	•	D – Dependency Inversion Principle (DIP) – Nguyên tắc đảo ngược sự phụ thuộc: Các thành phần cấp cao không nên phụ thuộc trực tiếp thành phần cấp thấp; cả hai nên phụ thuộc vào các abstraction chung. Đồng thời, các abstraction không nên phụ thuộc chi tiết, mà chi tiết phụ thuộc abstraction. Hiểu nôm na: code nên hướng đến interface/abstract class thay vì cụ thể. Ví dụ: Một lớp PaymentProcessor (cấp cao) cần dùng chức năng gửi thông báo SMS (cấp thấp). Thay vì gọi trực tiếp TwilioSMSService cụ thể, PaymentProcessor nên phụ thuộc vào một interface INotificationService. Lớp cụ thể TwilioSMSService sẽ implement interface này. Khi đó, nếu sau này đổi sang dịch vụ SMS khác hoặc thêm email, ta chỉ cần đổi ở cấu hình hoặc inject đối tượng khác, không phải sửa code PaymentProcessor. DIP giúp code linh hoạt, dễ mở rộng và test (có thể mock interface khi unit test).

Nhìn chung, SOLID hướng tới thiết kế code module hóa, giảm kết nối chặt (low coupling), tăng gắn kết nội bộ (high cohesion). Ví dụ áp dụng SOLID: trong dự án, nếu tuân theo SRP + OCP, khi thêm tính năng ta tạo class mới thay vì sửa class cũ (giảm rủi ro). DIP + ISP giúp code dễ mở rộng và tiêm phụ thuộc (dependency injection) hiệu quả – rất hữu ích trong các kiến trúc phức tạp, ví dụ xây dựng hệ thống plugin.

Ứng viên nên nhớ rõ tên và ý nghĩa của từng nguyên tắc. Một số phỏng vấn viên có thể hỏi sâu: “Anh/Chị có thể lấy ví dụ thực tế vi phạm nguyên tắc LSP không?” hoặc “Làm thế nào để áp dụng DIP trong Python khi ngôn ngữ này không có interface rõ ràng?”. Hãy chuẩn bị trả lời bằng kinh nghiệm của bản thân nếu có (ví dụ DIP trong Python thì dùng abstract base class hoặc protocol để định nghĩa interface, rồi cấu hình inject phụ thuộc…).

Cơ sở dữ liệu & SQL nâng cao

Câu hỏi: Chỉ mục (Index) trong cơ sở dữ liệu là gì? Tại sao dùng index lại giúp tăng tốc truy vấn? Khi nào thì không nên lạm dụng index? (Độ khó: Mid/Senior)

Trả lời: Chỉ mục (index) trong database là một cấu trúc dữ liệu đặc biệt (thường là cây B-Tree đối với nhiều hệ quản trị như MySQL, PostgreSQL) được tạo ra để tăng tốc độ truy vấn và tìm kiếm dữ liệu ￼. Có thể hình dung index giống như mục lục của cuốn sách: thay vì phải duyệt qua toàn bộ cuốn sách để tìm một chủ đề, ta tra mục lục để nhảy ngay đến trang có nội dung đó ￼.

Cụ thể: khi tạo index trên một hoặc nhiều cột của bảng, database sẽ duy trì một cấu trúc (thường được sắp xếp theo giá trị cột) chứa các con trỏ đến các hàng dữ liệu thực sự. Ví dụ tạo index trên cột email của bảng User, DB sẽ sắp xếp các giá trị email theo thứ tự, kèm pointer tới vị trí record tương ứng trên ổ đĩa. Do đó:
	•	Truy vấn SELECT * FROM User WHERE email = 'abc@example.com' có thể dùng index để tìm kiếm nhị phân trên cây thay vì duyệt tuần tự toàn bảng. Độ phức tạp tìm kiếm giảm từ O(n) xuống O(log n). Với bảng hàng triệu record, index có thể tăng tốc truy vấn lên hàng trăm lần.
	•	Index cũng giúp tăng tốc các phép JOIN và sắp xếp (ORDER BY) trên cột được đánh chỉ mục, vì dữ liệu đã được tổ chức ở dạng thuận lợi.

Tuy nhiên, đánh đổi khi sử dụng index:
	•	Tốn không gian lưu trữ: Index chiếm thêm bộ nhớ (trên đĩa và có thể RAM), vì nó là cấu trúc dữ liệu riêng biệt.
	•	Ảnh hưởng hiệu năng ghi (INSERT/UPDATE/DELETE): Mỗi khi dữ liệu thay đổi, index phải được cập nhật để phản ánh thay đổi đó ￼. Điều này làm chậm các câu lệnh ghi. Ví dụ: chèn một hàng mới sẽ phải chèn cả vào vị trí phù hợp trong cây index (O(log n) cho mỗi index). Nếu bảng có nhiều index, chi phí ghi tăng đáng kể.
	•	Không phải lúc nào cũng cần: Nếu bảng nhỏ vài trăm bản ghi, scanning tuần tự cũng nhanh, index overhead có khi còn không đáng.

Khi nào nên tạo index:
	•	Trên các cột thường xuyên xuất hiện trong mệnh đề WHERE, JOIN, hoặc ORDER BY. Ví dụ cột khóa ngoại dùng join, cột tên đăng nhập hay tra cứu.
	•	Các cột độc nhất hoặc phân bố giá trị đa dạng. Index hiệu quả nhất khi phân biệt được nhiều bản ghi. Nếu cột chỉ có vài giá trị lặp đi lặp lại (ví dụ cột Giới tính), index không phát huy tác dụng mấy (vì vẫn phải truy nhiều bản ghi giống nhau).
	•	Khi performance truy vấn là vấn đề và đã xác định nút thắt (bottleneck) là do thiếu index.

Khi không nên/hoặc cẩn thận khi tạo index:
	•	Bảng quá nhỏ (dưới vài nghìn bản ghi) – overhead duy trì index có thể không xứng đáng.
	•	Bảng cập nhật quá thường xuyên, trong khi truy vấn đọc ít – index làm chậm ghi nhiều hơn lợi ích lúc đọc.
	•	Index trên nhiều cột (composite index) phải cân nhắc thứ tự cột và loại truy vấn sẽ sử dụng.
	•	Không nên tạo quá nhiều index “thừa” – mỗi index đều có chi phí bảo trì. Thống kê thường cho thấy 3-5 index mỗi bảng là bình thường, nếu bảng có vài chục index có thể xem xét lại.

Một số bổ sung:
	•	Clustered index: (ví dụ Primary Key trong InnoDB) tổ chức dữ liệu vật lý theo thứ tự chỉ mục, giúp truy cập rất nhanh theo PK. Mỗi bảng thường chỉ có một clustered index.
	•	Covering index: index chứa đủ mọi cột để trả lời một truy vấn (tránh truy cập bảng gốc).
	•	Implicit index: nhiều DBMS tự động tạo index cho khóa chính, khóa ngoại… ￼.

Đối với phỏng vấn, ứng viên cần cho thấy hiểu khái niệm index và trade-off: “index làm truy vấn nhanh hơn nhờ giảm hoạt động I/O đọc, nhưng làm chậm thao tác ghi”. Có thể nêu kinh nghiệm tối ưu: dùng EXPLAIN để kiểm tra query có dùng index không, tránh sử dụng hàm trên cột trong WHERE (vì sẽ bỏ qua index), v.v.

EPAM có thể đánh giá cao nếu bạn chia sẻ tình huống bạn tối ưu query nhờ thêm index, hoặc trường hợp index sai làm giảm hiệu năng. Ví dụ: “Trước đây tôi có một bảng 10 triệu bản ghi, truy vấn join 3 bảng chậm, tôi phát hiện thiếu index ở khóa ngoại, sau khi thêm index thời gian giảm từ 30s xuống 0.5s”. Một câu chuyện thực tế sẽ gây ấn tượng rằng bạn thực sự có kinh nghiệm.

REST API & Security

Câu hỏi: Bạn sẽ triển khai việc xác thực và phân quyền (authentication & authorization) cho một RESTful API như thế nào? Hãy nêu một số phương thức bảo mật API phổ biến. (Độ khó: Senior)

Trả lời: Bảo mật một RESTful API gồm hai phần chính: xác thực (authentication) – xác minh client là ai, và phân quyền (authorization) – kiểm soát client đó có được phép truy cập tài nguyên hay hành động cụ thể không. Có nhiều cách triển khai, nhưng các phương pháp phổ biến hiện nay bao gồm:
	1.	Token-based Authentication (Xác thực dùng mã thông báo): Thay vì phiên (session) truyền thống, API thường dùng token vì REST hay stateless (server không lưu trạng thái phiên, mỗi request tự chứa thông tin xác thực).
	•	JWT (JSON Web Token): Đây là cách rất thịnh hành. Khi user đăng nhập thành công (ví dụ qua API /login), server phát về một JWT (chuỗi mã hóa gồm header.payload.signature). Các request sau client gửi kèm JWT (thường trong header Authorization: Bearer <token>). Server kiểm tra chữ ký của JWT để xác thực tính hợp lệ và giải mã lấy thông tin user/roles từ payload ￼. JWT có thể chứa thông tin phân quyền (vd vai trò user là admin hay user thường). JWT có ưu điểm là self-contained (tự nó mang thông tin), server không cần lưu session, và khó giả mạo nếu dùng thuật toán ký đủ mạnh.
	•	Opaque Token + DB/Cache: Một số hệ thống phát token ngẫu nhiên (chuỗi vô nghĩa), lưu map token->user trên server (trong DB hoặc memory cache như Redis). Mỗi request đến với token, server tra bảng để biết user nào tương ứng và còn hạn không. Cách này giống session nhưng không dùng cookie, phù hợp microservice (có thể dùng OAuth2 introspection nếu phân tán). Kém tiện bằng JWT nhưng dễ thu hồi token (revoke) nếu cần, vì server quản lý được danh sách token.
	•	API Key: Một dạng token tĩnh thường dùng cho dịch vụ server-to-server. Mỗi client được cấp một API key bí mật để gửi kèm request (ví dụ dưới dạng header X-API-Key). Server kiểm tra key có hợp lệ/đúng quota không. API key đơn giản nhưng thường chỉ xác thực danh tính ứng dụng, không xác thực user cụ thể.
	2.	OAuth2/OpenID Connect: Nếu API cung cấp cho bên thứ ba hoặc cần tích hợp với hệ thống xác thực chung, có thể dùng OAuth2 (để ủy quyền) kết hợp OpenID Connect (để xác thực danh tính). Ví dụ: Sử dụng Authorization Code Flow – client chuyển hướng người dùng đến trang đăng nhập của nhà cung cấp (Google, Facebook, hoặc Identity Server nội bộ), người dùng đăng nhập và đồng ý cấp quyền, sau đó client nhận được access token (thường là JWT) để gọi API. OAuth2 cho phép các mức scope phân quyền (ví dụ read:user, write:posts), và refresh token để lấy token mới khi hết hạn.
	3.	Basic Auth qua HTTPS: Cách đơn giản theo chuẩn HTTP Basic – client gửi username:password (đã encode base64) trong header Authorization mỗi request. Cách này rất không an toàn nếu không có HTTPS, và ngay cả có HTTPS cũng không nên dùng lâu dài vì buộc user gửi password liên tục. Chỉ phù hợp cho test nhanh hoặc môi trường nội bộ an toàn. Thực tế production, Basic Auth thường được thay bằng token như trên.

Sau khi xác thực, phân quyền (authorization) có thể thực hiện bằng nhiều cách:
	•	Dựa trên role: Ví dụ gán user một số vai trò (admin, user) và trong code API check: nếu vai trò không đủ thì trả 403 Forbidden. JWT có thể chứa roles để tiện kiểm tra.
	•	Dựa trên chi tiết quyền (permission): Fine-grained hơn, ví dụ user A có quyền edit_post nhưng user B thì không. Khi đó có bảng quyền hoặc danh sách permission trong token.
	•	Attribute-based access control: Theo thuộc tính (ví dụ chỉ cho phép user truy cập resource nếu resource.owner_id == user.id trừ khi có quyền admin).
	•	OAuth2 scopes: Nếu dùng OAuth2, token đi kèm scope (phạm vi quyền) – API dựa vào scope để quyết định cho phép hay không (ví dụ cần scope users.delete mới cho xóa user).

Biện pháp bảo mật khác cho API:
	•	HTTPS: Luôn dùng HTTPS để mã hóa lưu lượng, tránh nghe lén token hoặc thông tin nhạy cảm.
	•	CORS: Thiết lập Cross-Origin Resource Sharing hợp lý nếu API gọi từ trình duyệt, để tránh bị trang độc hại gọi trái phép.
	•	Rate Limiting & Throttling: Giới hạn số request để ngăn chặn brute force hoặc lạm dụng.
	•	Input Validation: Dù đã xác thực, vẫn phải kiểm tra kỹ tham số đầu vào để tránh injection (SQL injection, NoSQL injection) và các lỗ hổng (một phần của bảo mật).
	•	Logging & Monitoring: Ghi log các lần đăng nhập, các hành động quan trọng và cảnh báo nếu thấy bất thường để kịp thời phản ứng.
	•	Refresh Token & Token Expiry: Nếu dùng JWT, cho JWT hết hạn sau ngắn hạn (ví dụ 15 phút) và dùng refresh token riêng để lấy JWT mới – giảm nguy cơ JWT bị lộ có thể dùng lâu dài.
	•	Revoke Token: Có cơ chế thu hồi token (ví dụ maintain danh sách đen JWT ID nếu cần, hoặc dùng opaque token để có thể xóa server-side).

Ví dụ ngắn: “Giả sử tôi xây dựng một API cho ứng dụng mobile, tôi sẽ dùng JWT để user đăng nhập. Mỗi request API có header Authorization: Bearer <JWT>. Server có một secret để verify JWT. Payload JWT chứa user_id và roles. Với những endpoint nhạy cảm (ví dụ xóa user) tôi sẽ kiểm tra if 'admin' not in user.roles: return 403. JWT có hạn 1 giờ, mobile app sẽ gọi refresh token API khi gần hết hạn.” – Cách trả lời như vậy cho thấy ứng viên hiểu cách làm cụ thể.

EPAM đánh giá cao ứng viên hiểu tiêu chuẩn bảo mật hiện đại. Đặc biệt, biết về JWT là gần như bắt buộc (vì rất phổ biến). Nếu bạn đề cập đến OAuth2, OpenID Connect, đó là điểm cộng cho thấy trải nghiệm với hệ thống phức tạp. Ngoài ra, có thể được hỏi về các lỗ hổng API thường gặp (như JWT replay, CSRF, v.v.), nhưng trong phạm vi câu hỏi này, trả lời như trên là đầy đủ.

Unit Testing nâng cao

Câu hỏi: Mocking trong unit test là gì? Bạn sử dụng kỹ thuật mock/stub như thế nào khi viết unit test bằng Python? (Độ khó: Mid)

Trả lời: Mocking là một kỹ thuật trong kiểm thử đơn vị cho phép ta thay thế những thành phần phụ thuộc bằng các đối tượng giả lập (mock objects) để kiểm soát hành vi và tương tác trong môi trường test. Nói đơn giản, khi hàm/class A phụ thuộc vào B (gọi API, truy cập CSDL, đọc file, v.v.), ta không muốn test A lại phụ thuộc B thật (vì B có thể chậm, khó dự đoán hoặc chưa có sẵn), ta sẽ mock B – tạo một đối tượng giả B với hành vi xác định trước để A tương tác trong khi test.

Trong Python, mô-đun unittest.mock cung cấp các công cụ để tạo mock một cách dễ dàng ￼:
	•	unittest.mock.Mock và MagicMock: đối tượng giả có thể tự động “nhận mọi lời gọi” mà không làm gì thật sự, nhưng ghi nhận lại các lệnh gọi đó (call). Mình có thể cấu hình Mock trả về giá trị mong muốn khi được gọi (gán mock_object.return_value hoặc dùng side_effect).
	•	Monkeypatch (pytest): pytest cung cấp fixture monkeypatch để thay thế đối tượng trong module bằng đối tượng fake.
	•	patch(): Hàm unittest.mock.patch (dùng như decorator hoặc context manager) để thay thế một tên (name) trong module bằng một mock trong suốt thời gian test. Ví dụ: with patch('requests.get') as mock_get: sẽ thay hàm requests.get bằng mock_get.

Tại sao cần mock:
	•	Đảm bảo unit test độc lập: khi test hàm A, ta muốn lỗi chỉ do A chứ không do phụ thuộc.
	•	Loại bỏ yếu tố không xác định: ví dụ hàm gửi request HTTP, ta không muốn test đơn vị phải gọi mạng (chậm, kết quả biến thiên). Thay vào đó mock kết quả HTTP (giả lập response) để test logic xử lý của A.
	•	Tăng tốc và đơn giản hóa test: truy xuất DB thật hay API thật vừa chậm vừa đòi môi trường phức tạp. Dùng mock cho phép test chạy nhanh, môi trường gọn (không cần cài DB, không cần mạng).
	•	Kiểm tra tương tác: Mock cho phép xác nhận xem hàm A có gọi hàm B với tham số đúng hay không (số lần gọi, thứ tự gọi). Đây gọi là behavior verification.

Ví dụ tình huống:
Giả sử có hàm:
import requests
def fetch_user_email(user_id):
    resp = requests.get(f"https://example.com/api/users/{user_id}")
    data = resp.json()
    return data["email"]
from unittest.mock import patch, MagicMock
def test_fetch_user_email():
    fake_resp = MagicMock()
    fake_resp.json.return_value = {"email": "alice@example.com"}
    # patch requests.get to return fake_resp
    with patch('requests.get', return_value=fake_resp) as mock_get:
        email = fetch_user_email(123)
        assert email == "alice@example.com"
        mock_get.assert_called_once_with("https://example.com/api/users/123")
Ở đây:
	•	Mình dùng patch để thay requests.get bằng một mock, cấu hình mock trả về fake_resp.
	•	fake_resp.json.return_value đặt là dict chứa email.
	•	Gọi hàm, kiểm tra hàm trả về email đúng.
	•	Dùng assert_called_once_with để đảm bảo requests.get (giờ là mock_get) được gọi đúng 1 lần với URL như mong đợi.

Kỹ thuật này khá chuẩn: Arrange (sắp xếp) đối tượng giả, Act (hành động) gọi hàm, Assert (kiểm tra) kết quả và tương tác.

Phân biệt một số khái niệm liên quan:
	•	Stub: đối tượng giả cung cấp sẵn dữ liệu cho hàm test nhưng không được test đến (chỉ trả về fixed value, không quan tâm có được gọi đúng hay không).
	•	Mock: đối tượng giả có thể cả cung cấp dữ liệu và ghi nhận cách nó được gọi để ta assert. (Trong unittest.mock, mọi thứ gọi là Mock).
	•	Patch: thao tác thay thế đối tượng thật bằng đối tượng giả trong môi trường test, thường tạm thời.

Lưu ý khi mock:
	•	Chỉ mock phụ thuộc bên ngoài, không mock chính hệ thống đang test (nếu mock hết bên trong, test mất ý nghĩa).
	•	Coi chừng over-mocking: nếu lạm dụng, test sẽ bớt ý nghĩa vì kiểm tra quá cụ thể các call nội bộ – code thay đổi chút có thể fail test dù chức năng vẫn đúng. Nên tập trung assert output nhiều hơn assert implementation, trừ phi behavior đó là một phần hợp đồng (ví dụ đảm bảo gọi phương thức thanh toán đúng 1 lần).
	•	Đảm bảo patch đúng nơi: Trong Python, patch phải nhắm vào tên biến được hàm dùng. VD, hàm fetch_user_email import requests cục bộ, ta phải patch 'module_cua_ham.requests.get' chứ không patch 'requests.get' ở global.

Nhìn chung, một ứng viên Python nên biết dùng unittest.mock hoặc pytest-mock. EPAM sẽ đánh giá cao nếu bạn có kinh nghiệm viết test thực tế. Bạn có thể kể: “Ở dự án trước, khi test lớp gửi email, tôi đã mock SMTP server, kiểm tra hàm gửi được gọi với email đúng mà không thực sự gửi email đi”. Điều đó cho thấy bạn hiểu ứng dụng của mock.

(Tham khảo: unittest.mock cho phép thay thế các phần của hệ thống bằng mock object và kiểm tra cách chúng được sử dụng ￼.)

System Design (Thiết kế hệ thống)

Câu hỏi: Thiết kế hệ thống rút gọn URL (giống như TinyURL hoặc Bitly). Bạn sẽ thiết kế các thành phần như thế nào để hệ thống có thể tạo URL rút gọn và phân giải ngược về URL gốc một cách hiệu quả, có thể mở rộng? (Độ khó: Senior)

Trả lời: Đây là một câu hỏi thiết kế hệ thống tổng quát. Mục tiêu là đánh giá khả năng phân tích yêu cầu, đề xuất kiến trúc và thảo luận các phương án xử lý quy mô lớn (scalable). Với hệ thống rút gọn URL, các yêu cầu chính thường là:
	•	Chức năng cốt lõi: Nhận một URL dài, sinh ra một mã rút gọn (short code) duy nhất và lưu ánh xạ (mapping) từ mã -> URL gốc. Khi có yêu cầu truy cập URL rút gọn, hệ thống tra mã và chuyển hướng (redirect) người dùng đến URL gốc.
	•	Các yếu tố thiết kế quan trọng: Tính duy nhất của mã rút gọn (không trùng lặp), hiệu năng tra cứu (tra mã nhanh để redirect nhanh), khả năng mở rộng (hỗ trợ số lượng URL cực lớn và lưu lượng truy cập cao), khả năng chịu lỗi (fault tolerance).

Thiết kế cấp cao:
	1.	Kiến trúc tổng quát: Có thể thiết kế dạng microservice nhỏ:
	•	Service API để tạo URL rút gọn: nhận URL gốc từ client (qua HTTP), xử lý và trả về URL ngắn.
	•	Service redirect (có thể chung với trên): lắng nghe request GET cho mã rút gọn, tra DB và trả về HTTP redirect.
	•	Các service này có thể được triển khai nhiều instance để chịu tải cao (load balancing).
	2.	Cơ sở dữ liệu lưu mapping: Sử dụng một database (có thể NoSQL key-value hoặc RDBMS đơn giản) để lưu cặp short_code -> long_url. Key là short_code, value là long_url.
	•	DB Key-Value (như Redis, Cassandra, DynamoDB): rất phù hợp vì mô hình đơn giản, truy cập theo key nhanh.
	•	Cũng có thể dùng MySQL với bảng có primary key là short_code. Tuy nhiên, với lượng cực lớn (hàng tỷ URL) NoSQL phân tán sẽ dễ scale hơn.
	3.	Thuật toán sinh short code:
	•	Cần tạo định danh duy nhất độ dài cố định (ví dụ 6-8 ký tự chữ cái chữ số). Một cách phổ biến:
	•	Sử dụng tăng ID tuần tự (auto-increment ID) rồi chuyển đổi ID sang dạng Base62 (0-9A-Za-z) để thành chuỗi ngắn ￼. Base62 cho phép biểu diễn ID lớn trong chuỗi ngắn (6-7 ký tự base62 có thể biểu diễn hàng chục tỷ).
	•	Hoặc dùng băm (hash) URL + cơ chế xử lý trùng. Hash có thể tạo chuỗi cố định nhưng cần kiểm tra trùng, và hash có khả năng đụng độ cao khi nhiều URL.
	•	Hoặc sử dụng UUID rồi rút gọn, nhưng UUID 128-bit thì rút gọn thành 22 ký tự Base64, hơi dài.
	•	Quyết định độ dài mã rút gọn tùy yêu cầu số lượng: 6 ký tự Base62 ~ 56 tỷ khả năng, đủ với đa số ứng dụng. Nếu scale như Bitly (đã tạo >10^11 URL) có thể tăng dần độ dài mã.
	•	Đảm bảo không sinh trùng: nếu dùng ID tuần tự thì trùng không xảy ra (mỗi ID duy nhất). Nếu hash thì cần cơ chế nếu trùng thì thử phương án khác (ví dụ thêm số random).
	•	Có thể cung cấp tính năng tùy chỉnh alias: user tự chọn mã (nếu chưa bị dùng).
	4.	Xử lý redirect:
	•	Người dùng truy cập http://short.domain/abc123, hệ thống (service redirect) nhận mã abc123, tra cứu trong DB ra https://really-long-url.... Sau đó trả về HTTP 301/302 redirect tới URL gốc.
	•	Tối ưu: có thể đặt cache (như Redis hoặc memory cache) cho các mã phổ biến để giảm truy vấn DB.
	•	Thông thường, hiệu suất tra key trong DB NoSQL đã rất nhanh (ms), và có thể scale bằng cách shard theo range hoặc hash key (short_code). Một cụm Cassandra hoặc Dynamo phân tán có thể xử lý hàng ngàn request/s dễ dàng.
	5.	Quy mô lớn & phân tán:
	•	Phân vùng dữ liệu: Nếu DB lưu mapping không đủ trong một máy, cần phân tán. Với key-value store có thể dùng consistent hashing để phân chia key short_code đồng đều giữa các node.
	•	Không có trạng thái: Các service API/redirect nên stateless (không giữ dữ liệu cục bộ), để có thể nhân bản và load balance.
	•	Cân bằng tải (Load Balancer): Đặt LB phía trước các server ứng dụng để chia request. Sử dụng CDN hoặc LB để redirect request cũng có thể, nhưng do logic tra DB, để server ứng dụng làm.
	•	Tính sẵn sàng (High Availability): Triển khai nhiều instance, DB dùng cluster nhiều node (ví dụ Cassandra có replication). Nếu 1 node down, hệ thống vẫn hoạt động.
	•	Scaling: Khi lưu lượng tăng, có thể mở rộng chiều ngang: thêm server ứng dụng, thêm node DB (nếu NoSQL horizontal scalable).
	•	Chú ý cạnh tranh (concurrency): Nếu dùng counter ID toàn cục, coi chừng race khi nhiều instance API tạo mã: có thể dùng 1 DB global sequence, hoặc mỗi instance được cấp 1 khối ID riêng để tự tăng (phức tạp hơn).
	•	Phân tích hiệu năng: Tạo code: chủ yếu ghi DB -> DB nên tối ưu cho ghi (NoSQL). Redirect: chủ yếu đọc -> DB tối ưu đọc + caching.
	6.	Các tính năng bổ sung (nếu đề cập mở rộng):
	•	Thống kê: đếm số lần truy cập mỗi URL rút gọn, thống kê IP, referrer… => cần một cơ chế logging hoặc increment counter (có thể làm bất đồng bộ để không chậm redirect).
	•	Hết hạn: có thể đặt URL tự hết hạn sau thời gian. Cần có job dọn dẹp hoặc trường expiry trong DB.
	•	Chống tấn công: cần cơ chế bảo vệ nếu ai đó tạo quá nhiều URL spam (rate limit API create), hay check URL gốc an toàn (tránh redirect link độc hại).
	•	UI: Hệ thống có thể kèm một trang web nhỏ để người dùng nhập URL và nhận link rút gọn (giống bitly website), nhưng trọng tâm design thường là backend.

Tóm tắt thiết kế qua các thành phần:
	•	Client – gửi URL gốc.
	•	Application Layer (URL Shortening Service) – nhận URL gốc, tạo mã ngắn (sinh unique ID, chuyển base62), lưu DB. Trả về short URL.
	•	Database (URL Mapping Store) – Lưu map {short_code -> long_url}. Ví dụ dùng NoSQL phân tán. Mục tiêu: tra cứu by key nhanh.
	•	Redirect Service – nhận request với mã, tra DB (có thể qua cache), được long_url, trả về HTTP redirect.
	•	Scaling/HA – Cân bằng tải giữa nhiều instance service; DB phân cụm để chịu tải cao và không mất dữ liệu.

Sơ đồ đơn giản như sau:

￼ ￼
	•	Client gọi API tạo URL → Service (tạo mã, lưu DB) → DB lưu mapping.
	•	Khi dùng: Client truy cập short URL → Service tra DB (hoặc cache) → trả về redirect (3xx) → Client được chuyển đến long URL.

*(Mô tả theo cách khác: “Hệ thống gồm các thành phần: database lưu cặp long-short, service để tạo short URL dùng thuật toán sinh ID duy nhất, và service để chuyển hướng. Sử dụng mã định danh duy nhất cho mỗi URL gốc để tạo URL ngắn và hệ thống ánh xạ lưu trữ URL dài và URL ngắn đó ￼. Nhờ thiết kế phân tán, hệ thống có thể xử lý hàng tỷ URL.”) ￼

Người phỏng vấn có thể đặt câu hỏi phụ: “Làm sao đảm bảo không trùng short code?”, “Nếu hệ thống cần handle 10^7 requests/day thì thiết kế có chịu nổi không? chỗ nào cần cải tiến?”. Lúc đó ta giải thích về scale (ví dụ phân tán DB, caching, v.v.) như trên. Cũng có thể hỏi về cấu trúc dữ liệu: “Tại sao dùng Base62?” – ta giải thích để bao gồm cả chữ hoa, chữ thường, số – 62 ký tự – mã ngắn gọn hơn base10 rất nhiều.

Một điểm hay có: “Nếu 2 người cùng rút gọn cùng 1 URL, hệ thống có trả cùng mã hay tạo mã khác?” – tùy yêu cầu. Thường bitly tạo mã khác (không kiểm tra URL trùng lặp, đơn giản và scale tốt), nhưng cũng có thể kiểm tra và trả về mã cũ để tiết kiệm (đòi hỏi search trong DB xem URL đã tồn tại, chi phí cao nếu DB lớn, nhưng có thể dùng hash table phụ). Ta có thể nêu ra nhưng thường chọn cách đơn giản: không cần check trùng URL gốc, mỗi yêu cầu cứ tạo mã mới (vì nhiều URL dài có thể do người khác gửi, chuyện trùng không nhiều và không ảnh hưởng chức năng).

Qua câu trả lời, người phỏng vấn muốn xem tư duy hệ thống của ứng viên: biết tách thành phần, quan tâm scale, consistency. Trả lời mạch lạc các ý trên, có kèm lý do chọn công nghệ (SQL vs NoSQL, etc.), là sẽ ghi điểm.

Cloud & DevOps (Triển khai trên đám mây)

Câu hỏi: Làm thế nào để deploy (triển khai) một ứng dụng web Python lên môi trường AWS? Bạn hãy liệt kê một số dịch vụ AWS phổ biến có thể sử dụng cho nhiệm vụ này và vai trò của chúng. (Độ khó: Mid)

Trả lời: AWS cung cấp rất nhiều dịch vụ hỗ trợ việc triển khai một ứng dụng web. Cách triển khai phụ thuộc vào kiến trúc ứng dụng và mức độ quản lý hạ tầng mà ta mong muốn. Sau đây là một số phương án tiêu biểu cho ứng dụng web Python (giả sử một ứng dụng Django/Flask):
	1.	Triển khai trên máy ảo EC2 (Elastic Compute Cloud):
Đây là cách “truyền thống” và linh hoạt nhất. Ta sẽ:
	•	Khởi tạo một EC2 instance (máy ảo) chạy hệ điều hành (ví dụ Amazon Linux hoặc Ubuntu).
	•	Cài đặt môi trường: cài Python, các gói cần thiết, thiết lập web server (Nginx/Apache) và ứng dụng (qua Git clone hoặc SCP code lên). Có thể sử dụng dịch vụ AWS Systems Manager để chạy script cài đặt.
	•	Chạy ứng dụng: Dùng một WSGI server (Gunicorn/uWSGI) để chạy ứng dụng Python, reverse proxy qua Nginx để phục vụ HTTP. Mở các cổng cần (80, 443) trong Security Group.
	•	Quản lý thủ công việc cấu hình scale: có thể gắn Auto Scaling Group để tự động tạo thêm EC2 khi tải cao, và Elastic Load Balancer (ELB) để phân phối request giữa các instance.
	•	Dữ liệu ứng dụng (như DB) có thể dùng RDS (dịch vụ database managed) hoặc cài DB trên EC2 riêng.
	•	Ưu điểm: Kiểm soát hoàn toàn máy chủ, tùy biến cao (có thể cài bất cứ thứ gì).
	•	Nhược: cần nhiều công sức quản trị (update OS, scale out thủ công trừ khi cấu hình phức tạp auto-scaling).
	2.	Sử dụng AWS Elastic Beanstalk:
Elastic Beanstalk là dịch vụ PaaS giúp triển khai ứng dụng dễ dàng.
	•	Chỉ cần chuẩn bị mã nguồn (hoặc container Docker), EB sẽ lo tạo EC2, cài đặt môi trường, cấu hình scaling, load balancing.
	•	Cụ thể, với ứng dụng Python, chỉ cần cung cấp code và file cấu hình (ví dụ Procfile chỉ định cách chạy Gunicorn). EB sẽ tự tạo một environment gồm EC2 (hoặc container) + ELB + Auto Scaling.
	•	Bạn có thể cấu hình trên EB dashboard một số tham số như instance type, số lượng instance min/max.
	•	Ưu: triển khai nhanh, AWS lo nhiều việc ops; tích hợp giám sát CloudWatch; hỗ trợ rolling update.
	•	Nhược: ít linh hoạt hơn tự làm trên EC2 (Beanstalk có opinion riêng), debug phức tạp khi gặp vấn đề do lớp abstraction.
	3.	Chạy dưới dạng Container:
	•	Đóng gói ứng dụng Python vào một Docker image.
	•	Sử dụng Amazon ECS (Elastic Container Service) hoặc Amazon EKS (Elastic Kubernetes Service) để triển khai container.
	•	Với ECS: có thể chạy trên Fargate (serverless container) – chỉ cần đưa image lên ECR (Elastic Container Registry) và ECS sẽ lo chạy container, tự động scale số task theo cấu hình (cũng có load balancer integration). Fargate giúp không phải quản lý server.
	•	Với EKS: nếu công ty dùng Kubernetes, EKS cung cấp control plane Kubernetes, ta triển khai container qua pods, service. EKS phức tạp hơn ECS, thường dùng nếu đã có system K8s.
	•	AWS App Runner: một dịch vụ mới, cho phép chạy trực tiếp ứng dụng web container hoặc code từ source. App Runner tự build container từ source, deploy và scale tự động. Mục tiêu cạnh tranh với Heroku, rất tiện cho dev muốn đẩy code nhanh (chỉ hỗ trợ web service, không phức tạp bằng ECS).
	•	Container hóa phù hợp khi muốn đóng gói đồng nhất môi trường dev-prod, hoặc cần microservice phức tạp. AWS ECS/EKS giúp ứng dụng Python chạy trong môi trường có quản lý (orchestrated environment).
	4.	Serverless (AWS Lambda + API Gateway):
	•	Nếu ứng dụng có thể chia thành các function hoặc endpoint độc lập, có thể triển khai một số thành phần dưới dạng AWS Lambda (hàm serverless). Lambda chạy code Python theo sự kiện mà không cần quản lý server ￼.
	•	Kết hợp Amazon API Gateway để xây dựng các endpoint HTTP mà khi được gọi sẽ trigger Lambda.
	•	Kiến trúc này loại bỏ việc quản lý server hoàn toàn, và tự động scale theo lượng request (mỗi request có thể spawn một lambda instance).
	•	Tuy nhiên, không phải ứng dụng nào cũng phù hợp serverless (phải khởi động nhanh, stateless hoàn toàn, và chi phí có thể cao nếu lưu lượng rất lớn do tính theo request).
	•	Thường được dùng cho các microservice nhỏ, hoặc backend của ứng dụng di động mà mỗi endpoint là hàm riêng.
	5.	Các dịch vụ phụ trợ khác:
	•	AWS RDS: Dùng để triển khai các database quan hệ (MySQL, PostgreSQL, etc.) cho ứng dụng một cách quản lý (thay vì cài DB trên EC2).
	•	Amazon S3: Lưu trữ tĩnh (ảnh, file) – nhiều ứng dụng Django dùng S3 để lưu media file, static file và phục vụ qua CloudFront (CDN) để giảm tải.
	•	AWS Secrets Manager / SSM Parameter Store: Lưu trữ các cấu hình nhạy cảm (DB password, API keys) để ứng dụng lấy ra khi chạy, thay vì hardcode.
	•	CloudWatch: Giám sát logs, chỉ số CPU/memory, v.v. Tích hợp CloudWatch Alarms để cảnh báo nếu server quá tải.
	•	Route 53: quản lý DNS, trỏ tên miền tới Load Balancer hoặc CloudFront của ứng dụng.

Một kịch bản ví dụ: Triển khai một ứng dụng Django trên AWS:
	•	Sử dụng Elastic Beanstalk Python Platform. Upload code qua AWS Console. EB khởi chạy 2 EC2 t2.medium cho web app + 1 Load Balancer.
	•	Sử dụng RDS PostgreSQL cho database, EB sẽ auto attach biến môi trường DB cho app.
	•	Tệp static được cấu hình dùng S3 + CloudFront (CDN).
	•	Domain tùy chỉnh trỏ về CloudFront, dùng AWS Certificate Manager phát SSL miễn phí, LB/CloudFront dùng chứng chỉ đó để HTTPS.
	•	Mọi log app được đẩy qua CloudWatch Logs để xem dễ dàng.
	•	Cài đặt auto-scaling: nếu CPU trung bình > 70% trong 5 phút, EB thêm 1 instance; < 30% thì giảm bớt.

Cách trên khá phổ biến nhờ EB làm nhiều việc. Một ứng viên có thể đưa ra phương án khác như “Dockerize app rồi chạy trên ECS Fargate để không lo quản lý EC2”. Điều quan trọng là liệt kê đúng các dịch vụ AWS liên quan và vai trò:
	•	EC2 (máy chủ),
	•	ECS/EKS (chạy container),
	•	Lambda (serverless)
	•	RDS (database), S3 (storage),
	•	ELB (cân bằng tải),
	•	CloudFront (CDN),
	•	Route53 (DNS),
	•	… và giải thích ngắn gọn cái nào dùng khi nào.

Người phỏng vấn muốn thấy bạn quen thuộc với môi trường cloud, đặc biệt AWS. Ở EPAM, dev không nhất thiết rành cấu hình chi tiết, nhưng cần biết phải dùng dịch vụ gì cho nhu cầu nào.

Docker & Containerization

Câu hỏi: Docker là gì và container khác gì máy ảo (VM)? Bạn sẽ tiến hành container hóa một ứng dụng Python như thế nào? (Độ khó: Mid)

Trả lời: Docker là một nền tảng giúp đóng gói, phân phối và chạy ứng dụng trong các đơn vị gọi là container. Container có thể xem là một môi trường chạy ứng dụng nhẹ và tách biệt, trong đó bao gồm tất cả những gì ứng dụng cần (mã nguồn, thư viện, runtime), nhưng dùng chung kernel của hệ điều hành máy chủ.

So sánh Container vs Virtual Machine (VM):
	•	Cả hai đều là công nghệ ảo hóa để đóng gói môi trường chạy.
	•	Máy ảo (VM): ảo hóa toàn bộ phần cứng. Mỗi VM chạy một hệ điều hành đầy đủ (guest OS) trên hypervisor. VM chứa kernel riêng, các dịch vụ hệ thống – do đó thường nặng hơn (tốn nhiều RAM, CPU) và thời gian khởi động lâu (phải boot OS). Tuy nhiên VM cách ly rất tốt (môi trường hoàn toàn độc lập) và có thể chạy OS khác với host (ví dụ host Windows, VM Linux). ￼
	•	Container: ảo hóa ở mức hệ điều hành (OS-level). Nhiều container chia sẻ cùng một kernel của OS chủ, nhưng mỗi container có filesystem, process space, network interface riêng ￼. Container nhẹ hơn nhiều – thường chỉ vài chục MB, khởi động gần như tức thì (vì chỉ cần khởi chạy process chính bên trong). Container giới hạn bởi OS chung (ví dụ host Linux chạy container Linux; Docker trên Windows thực chất chạy Linux container thông qua nhân Linux bên trong).
	•	Tóm lại: Docker container dùng tài nguyên hiệu quả hơn, phù hợp triển khai số lượng lớn ứng dụng vi mô trên cùng máy. VM phù hợp khi cần cô lập hoàn toàn hoặc chạy các môi trường OS khác nhau.

Container hóa ứng dụng Python:
Để container hóa, ta cần viết Dockerfile mô tả cách xây dựng image cho ứng dụng:
	1.	Chọn base image: Thường dùng ảnh nền chính thức, ví dụ python:3.10-slim (đã có sẵn Python 3.10 trên nền Debian slim). Slim image nhỏ gọn giúp image cuối nhỏ hơn.
	2.	Copy mã nguồn và cài dependencies:
	•	Sử dụng chỉ thị COPY để đưa code vào image.
	•	Copy riêng requirements.txt rồi chạy pip install -r requirements.txt (dùng RUN trong Dockerfile) để cài thư viện. (Copy requirements trước giúp cache layer – khi code đổi nhưng requirements không đổi, Docker không cần cài lại thư viện từ đầu).
	3.	Thiết lập môi trường chạy:
	•	Đặt biến môi trường qua ENV nếu cần (ví dụ ENV FLASK_ENV=production).
	•	Tạo user không quyền root (tốt cho bảo mật) nếu cần qua RUN adduser rồi USER.
	•	Expose cổng dịch vụ (ví dụ EXPOSE 8000).
	4.	Command khởi động: Dùng CMD hoặc ENTRYPOINT chỉ định lệnh chạy khi container khởi động. Với Flask có thể là flask run, với Django có thể gunicorn myproject.wsgi:application.
	•	Thường CMD ["gunicorn", "-w", "4", "-b", "0.0.0.0:8000", "app:app"] (ví dụ cho Flask app).
	5.	Build image: Chạy docker build -t myapp:1.0 . (dấu . là context nơi có Dockerfile). Docker sẽ thực thi các bước trong Dockerfile tạo ra image.
	6.	Chạy container: docker run -d -p 8000:8000 myapp:1.0. Cờ -p map cổng container ra cổng host. -d chạy detach nền.
    FROM python:3.10-slim

# Tạo thư mục làm việc
WORKDIR /app

# Cài các dependencies
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy code
COPY . .

# Expose port
EXPOSE 5000

# Command chạy Flask (giả sử app.py, app chạy trên 0.0.0.0:5000)
CMD ["python", "app.py"]


def fib_generator(n):
    a, b = 0, 1
    for _ in range(n):
        yield a
        a, b = b, a + b

print(list(fib_generator(5)))  # Kết quả: [0, 1, 1, 2, 3]
from collections import Counter
arr = [1, 2, 2, 3, 3, 3]
freq = Counter(arr)
print(freq)  # Counter({3: 3, 2: 2, 1: 1})
for val, count in freq.items():
    print(f"{val} xuất hiện {count} lần")
