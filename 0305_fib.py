n1 = n2 = 1
i = 1

while i <= 50:
    if i == 1 or i == 2:
        print(n1)
    elif i % 2 == 1:
        n2 = n1 + n2
        print(n2)
    elif i % 2 == 0:
        n1 = n1 + n2
        print(n1)
    i += 1
