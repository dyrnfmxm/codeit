def binary_search(element, some_list):
    start_index, end_index = 0, len(some_list)
    index = int((start_index + end_index)/2)
        
    while element != some_list[index]:
        index = int((start_index + end_index)/2)
        
        if element < some_list[start_index] or element > some_list[end_index-1]:
            return None
        if element > some_list[index]:
            start_index = index
        elif element < some_list[index]:
            end_index = index
            
    return index
    # 코드를 작성하세요.

print(binary_search(2, [2, 3, 5, 7, 11]))
print(binary_search(0, [2, 3, 5, 7, 11]))
print(binary_search(5, [2, 3, 5, 7, 11]))
print(binary_search(3, [2, 3, 5, 7, 11]))
print(binary_search(11, [2, 3, 5, 7, 11]))
