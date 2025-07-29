"""
Imagine you are given a list of strings like this:
    Input: ["eat", "tea", "tan", "ate", "nat", "bat"]
    Output:
        [
            ["eat", "tea", "ate"],
            ["tan", "nat"],
            ["bat"]
        ]

"""


def group_anagrams(items: list):
    check_appear = {}
    for item in items:
        sorted_item = sorted(item)  # sorted luôn luôn trả về list => ['e', 'a', 't']
        sorted_item = "".join(sorted_item)  # join lại để trả về string/item đã sắp xếp
        if (
            sorted_item not in check_appear
        ):  # Đi kiểm tra xem sorted_item có trong dict hay không
            check_appear[sorted_item] = [
                item
            ]  # Nếu chưa thì add key = list với item đó có rồi thì tiếp tục thêm phần tử vào dict
        else:
            check_appear[sorted_item].append(item)
    print("Check appear", check_appear)
    # Cuối cùng ta được {'aet': ['eat', 'tea', 'ate'], 'ant': ['tan', 'nat'], 'abt': ['bat']}
    result = [value for value in check_appear.values()]  # Đi lấy value ra
    return result


if __name__ == "__main__":
    items = ["eat", "tea", "tan", "ate", "nat", "bat"]
    result = group_anagrams(items)
    print(f"Anagrams group are {result}")
