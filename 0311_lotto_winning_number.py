from random import randint


def draw_winning_numbers():
    # 코드를 작성하세요.
    winning_number_list = []
    
    while len(winning_number_list) < 7:
        number = randint(1,45)
        if number not in winning_number_list:
            winning_number_list.append(number)
        if len(winning_number_list) == 6:
            winning_number_list.sort()
            
    return winning_number_list

print(draw_winning_numbers())
