def count_matching_numbers(numbers, winning_numbers):
    # 지난 과제의 코드를 붙여 넣으세요.
    count = 0
    for i in numbers:
        for j in winning_numbers:
            if i == j:
                count += 1
    return count

def check(numbers, winning_numbers):
    # 코드를 작성하세요.
    count = count_matching_numbers(numbers, winning_numbers[:6])
    
    if count == 6:
        return 100000000
    elif count == 5:
        if winning_numbers[6] in numbers:
            return 50000000
        else:
            return 1000000
    elif count == 4:
        return 50000
    elif count == 3:
        return 5000
    
# 테스트
print(check([2, 4, 11, 14, 25, 40], [4, 12, 14, 28, 40, 41, 6]))
print(check([2, 4, 11, 14, 25, 40], [2, 4, 10, 11, 14, 40, 25]))
