previous = 0
current = 1
i = 1

while i <= 50:
    print(current)
    temp = previous
    previous = current
    current = previous + temp
    i += 1
