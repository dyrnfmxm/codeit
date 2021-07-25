import math

a, b, c = map(int,input().split())

result = math.gcd(math.gcd(a, b), c)

print(result)
