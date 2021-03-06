i = 1
s = 0

while i < 1000:
    if i % 2 == 0 or i % 3 == 0:
        s += i
    i += 1
print(s)
