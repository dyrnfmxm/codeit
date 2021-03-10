with open('vocabulary.txt', 'r') as f:

    for line in f:
        voca = line.strip().split(': ')
        kor_word = voca[1]
        eng_word = voca[0]
        
        answer = input(f"{kor_word}: ")
        if answer == eng_word:
            print("맞았습니다!\n")
        else:
            print(f"아쉽습니다. 정답은 {eng_word}입니다.\n")
