# 자리수 합 리턴
def sum_digit(num):
    result = 0
    num = str(num)
    for i in num:
        i = int(i)
        result += i
    return result
    # 코드를 입력하세요.

s = 0
# sum_digit(1)부터 sum_digit(1000)까지의 합 구하기
# 코드를 입력하세요.
for i in range(1, 1001):
    s += sum_digit(i)
    
print(s)
