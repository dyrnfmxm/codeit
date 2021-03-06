for a in range(333):
    for b in range(a, 500):
        if a * a + b * b == (1000-a-b)**2:
            c = 1000-a-b
            print(a*b*c)
