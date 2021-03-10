def is_palindrome(word):
    word_list = list(word)
    reverse_word_list = list(word)
    reverse_word_list.reverse()
    if word_list == reverse_word_list:
        return True
    else:
        return False
    # 코드를 입력하세요.


# 테스트
print(is_palindrome("racecar"))
print(is_palindrome("stars"))
print(is_palindrome("토마토"))
print(is_palindrome("kayak"))
print(is_palindrome("hello"))
