def fib_optimized(n):
    current = 1
    previous = 0
    
    for i in range(1, n):
        temp = current
        current = current + previous
        previous = temp
    
    return current
    # 코드를 작성하세요. 


# 테스트
print(fib_optimized(16))
print(fib_optimized(53))
print(fib_optimized(213))
