def merge(list1, list2):
    # 코드를 작성하세요.
    i, j = 0, 0
    merge_list = []
    while True:
        if len(list1) == 0:
            return merge_list + list2
        elif len(list2) == 0:
            return merge_list + list1
        elif list1[i] > list2[j]:
            merge_list.append(list2[j])
            del list2[j]
        elif list1[i] < list2[j]:
            merge_list.append(list1[i])
            del list1[i]
    return merge_list
# 테스트
print(merge([1],[]))
print(merge([],[1]))
print(merge([2],[1]))
print(merge([1, 2, 3, 4],[5, 6, 7, 8]))
print(merge([5, 6, 7, 8],[1, 2, 3, 4]))
print(merge([4, 7, 8, 9],[1, 3, 6, 10]))
