def trapping_rain(buildings):
    # 코드를 작성하세요
    trapping = 0
    for i in range(1, len(buildings)-1):
        height = min(max(buildings[:i]), max(buildings[i:]))
        if height == buildings[i]:
            continue
        elif height < buildings[i]:
            continue
        elif height != 0:
            trapping += height - buildings[i]
        #print(buildings[i], height, trapping)
        #print(trapping)
    return trapping
# 테스트
print(trapping_rain([3, 0, 0, 2, 0, 4]))
print(trapping_rain([0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1]))
