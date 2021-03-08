numbers = [2, 3, 5, 7, 11, 13, 17, 19]

# 리스트 뒤집기
# 코드를 입력하세요.
reverse_numbers = []

for i in range(len(numbers)-1,-1,-1):
    reverse_numbers.append(numbers[i])

print("뒤집어진 리스트: " + str(reverse_numbers))
