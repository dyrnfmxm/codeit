def mask_security_number(security_number):
    masking_number = list(security_number)
    masking_number_str = ""
    for i in range(len(masking_number)-1,len(masking_number)-5,-1):
        masking_number[i] = '*'
    for i in masking_number:
        masking_number_str += i 
    return masking_number_str
    # 코드를 입력하세요


# 테스트
print(mask_security_number("880720-1234567"))
print(mask_security_number("8807201234567"))
print(mask_security_number("930124-7654321"))
print(mask_security_number("9301247654321"))
print(mask_security_number("761214-2357111"))
print(mask_security_number("7612142357111"))
