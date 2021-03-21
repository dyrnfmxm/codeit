# 파라미터 some_list를 거꾸로 뒤집는 함수
new_list = []
def flip(some_list):
    if len(some_list) == 0:
        return new_list
    new_list.append(some_list[-1])
    del some_list[-1]
    # 코드를 입력하세요.
    return flip(some_list)

# 테스트
some_list = [1, 2, 3, 4, 5, 6, 7, 8, 9]
some_list = flip(some_list)
print(some_list)
