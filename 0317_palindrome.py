def is_palindrome(word):
    # 코드를 입력하세요.
    reverse_word = word[::-1]
    for i in range(len(word)):
        if word[i] != reverse_word[i]:
            return False
            break
    return True            
    
# 테스트
print(is_palindrome("racecar"))
print(is_palindrome("stars"))
print(is_palindrome("토마토"))
print(is_palindrome("kayak"))
print(is_palindrome("hello"))
