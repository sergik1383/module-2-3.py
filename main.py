
my_list = [42, 69, 0, 322, 13, 0, 99, -5, 9, 8, 7, -6, 5]
a = 0
while len(my_list) > a:
    num = my_list[a]
    a = a + 1
    if num == 0:
        continue
    elif num > 0:
        print(num)
    else:
        break




