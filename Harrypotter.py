def fourdigit(number):
    str_num = str(number)
    first_num = int(str_num[0])
    last_num = int(str_num[-1])
    sum= first_num + last_num
    print(sum)
    return 0

number = int(input(""))
fourdigit(number)
