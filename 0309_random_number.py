import random

random_number = random.randint(1,20)
# 코드를 작성하세요.
count = 1
while count <= 4:
    n = int(input(f"기회가 {5-count}번 남았습니다. 1-20 사이의 숫자를 맞혀보세요: "))
    if count == 4:
        print(f"아쉽습니다. 정답은 {random_number}입니다.")
        count += 1
    elif n == random_number:
        print(f"축하합니다. {count}번만에 숫자를 맞히셨습니다.")
        break
    elif n < random_number:
        print("Up")
        count += 1
    elif n > random_number:
        print("Down")
        count += 1
