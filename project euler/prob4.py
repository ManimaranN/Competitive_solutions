def rev(num):
    if num == str(num)[::-1]:
        state = True
    else:
        state = False
    return state

list1 = []
large = 0
for num1 in range(10, 100):
    for num2 in range(10, 100):
        add = num1*num2
        check = rev(str(add))
        if check == 1:
            if add > large:
                large = add
            list1.append(add)

print(list1)
print(large)











