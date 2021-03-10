with open('data/chicken.txt', 'r') as f:
    
    sales_sum = 0
    days = 0
    
    for line in f:
        chicken_sales = (line.strip().split(': '))
        sales_sum += int(chicken_sales[1])
        days += 1
    
    print(sales_sum/days)
