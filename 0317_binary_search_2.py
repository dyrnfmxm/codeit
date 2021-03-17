def binary_search(element, some_list):
    start_index, end_index = 0, len(some_list)-1

    while start_index <= end_index:
        index = (start_index + end_index) // 2
        if some_list[index] == element:
            return index
        elif element < some_list[index]:
            end_index = index - 1
        elif element > some_list[index]:
            start_index = index + 1

    return None
    # 코드를 작성하세요.

print(binary_search(2, [2, 3, 5, 7, 11]))
print(binary_search(0, [2, 3, 5, 7, 11]))
print(binary_search(5, [2, 3, 5, 7, 11]))
print(binary_search(3, [2, 3, 5, 7, 11]))
print(binary_search(11, [2, 3, 5, 7, 11]))
