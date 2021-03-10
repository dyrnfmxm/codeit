import random

with open('vocabulary.txt', 'r') as f:
    voca_dict = {}
    kor_list = []
    for line in f:
        voca = line.strip().split(': ')
        kor_word, eng_word = voca[1], voca[0]
        voca_dict[kor_word] = eng_word
        kor_list.append(kor_word)

while True:
    question = random.randint(0,len(kor_list)-1)
    answer = input(f"{kor_list[question]}: ")
    if answer == 'q':
        break
    elif answer == voca_dict[kor_list[question]]:
        print("맞았습니다!")
    else:
        print(f"틀렸습니다. 정답은 {voca_dict[kor_list[question]]}입니다.")
