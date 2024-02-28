"""Compress a string 'aabcccccaaa' into 'a2b1c5a3' """


def string_compression(s: str)-> str:
    compress_string = ''
    count_consecutive = 0
    for i in range(len(s)):
        count_consecutive += 1
        if i + 1 == len(s) or s[i] != s[i+1]:
            compress_string += s[i] + str(count_consecutive)
            count_consecutive = 0
    return compress_string

if __name__ == '__main__':
    print(string_compression('aabcccccaaa'))