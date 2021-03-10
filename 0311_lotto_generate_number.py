from random import randint


def generate_numbers(n):
    number_list = []
    count = 0
    
    while count < n:
        number = randint(1,45)
        if number not in number_list:
            number_list.append(number)
            count += 1
            
    return number_list
    # 코드를 작성하세요.

n = int(input())
print(generate_numbers(n))
