def course_selection(course_list):
    # 코드를 작성하세요.
    sorted_list = sorted(course_list, key=lambda x: x[1])
    course = [sorted_list[0],]
    #print(sorted_list)
    
    for i in range(1,len(sorted_list)):
        #print(sorted_list[i][0], sorted_list[i-1][1])
        
        last_course = course[-1:]
        #print(last_course[0][0], last_course[0][1])
        
        if sorted_list[i][0] > last_course[0][1]:
            course += [(sorted_list[i][0], sorted_list[i][1]),]
        """
        j = i
        
        while j < len(sorted_list):
            if sorted_list[j][0] > sorted_list[i-1][1]:
                if sorted_list[j] not in course:
                    print(sorted_list[j], sorted_list[i])
                    course += [(sorted_list[j][0], sorted_list[j][1]),]
                break
            j += 1
        """    
    return course
            

# 테스트
print(course_selection([(6, 10), (2, 3), (4, 5), (1, 7), (6, 8), (9, 10)]))
print(course_selection([(1, 2), (3, 4), (0, 6), (5, 7), (8, 9), (5, 9)]))
print(course_selection([(4, 7), (2, 5), (1, 3), (8, 10), (5, 9), (2, 5), (13, 16), (9, 11), (1, 8)]))
