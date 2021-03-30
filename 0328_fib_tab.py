def fib_tab(n):
    fib_list = [0, 1, 1]
    
    for i in range(3, n+1):
        fib_list.append(fib_list[i-2] + fib_list[i-1])
    #print(fib_list)
    return fib_list[n]
    
    # 코드를 작성하세요.

# 테스트
print(fib_tab(10))
print(fib_tab(56))
print(fib_tab(132))
