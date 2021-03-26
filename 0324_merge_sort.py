def  merge(list1, list2):
    # 코드를 작성하세요.
    i, j = 0, 0
    merge_list = []
    while True:
        if len(list1) == 0:
            return merge_list + list2
        elif len(list2) == 0:
            return merge_list + list1
        elif list1[i] >= list2[j]:
            merge_list.append(list2[j])
            del list2[j]
        elif list1[i] <= list2[j]:
            merge_list.append(list1[i])
            del list1[i]
    return merge_list
    # 이전 과제에서 작성한 코드를 붙여 넣으세요!

# 합병 정렬
def merge_sort(my_list):
    # 코드를 입력하세요.
    if len(my_list) == 1:
        return my_list
    
    mid = len(my_list) // 2
    #print(my_list)
    #print(merge(my_list[:mid], my_list[mid:]))
    #print(my_list[:mid], my_list[mid:])
    return merge(merge_sort(my_list[:mid]), merge_sort(my_list[mid:]))
    #return merge_sort(my_list[:mid]), merge_sort(my_list[mid:])

# 테스트
print(merge_sort([1, 3, 5, 7, 9, 11, 13, 11]))
print(merge_sort([28, 13, 9, 30, 1, 48, 5, 7, 15]))
print(merge_sort([2, 5, 6, 7, 1, 2, 4, 7, 10, 11, 4, 15, 13, 1, 6, 4]))
