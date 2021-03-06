APARTMENT = 1100000000
BANK = 0.12

year = 1988
money = 50000000

while year < 2016:
    money = money * (1+BANK)
    year += 1
if money > APARTMENT:
    print(f"{int(money-APARTMENT)}원 차이로 동일 아저씨 말씀이 맞습니다.")
elif money < APARTMENT:
    print(f"{int(APARTMENT-money)}원 차이로 미란 아주머니 말씀이 맞습니다.")
