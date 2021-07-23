

def cmpString(list):
    bool = True
    for c in list[1]:
        if c in list[0]:
            pass
        else:
            bool = False
            break
    return bool


str_1 = input('Enter first string: ')
str_2 = input('Enter second string: ')
list = [str_1, str_2]


print(cmpString(list))
