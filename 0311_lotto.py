from random import randint


def generate_numbers(n):
    number_list = []
        
    while len(number_list) < n:
        number = randint(1,45)
        if number not in number_list:
            number_list.append(number)
            
    return number_list

    # 코드를 작성하세요.

def draw_winning_numbers():
    # 코드를 작성하세요.
    winning_number_list = generate_numbers(7)        
    return sorted(winning_number_list[:6]) + winning_number_list[6:]

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
    else:
        return '꽝'
    
# 테스트
my_number = generate_numbers(6)
winning_number = draw_winning_numbers()
print(my_number)
print(winning_number)
print(check(my_number, winning_number))
