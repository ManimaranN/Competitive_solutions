num = 1
c = 0
list = []
samp_list = range(1,10)
while list == []:
    for i in samp_list:
        if num % i == 0:
            c = 1
        else:
            c = 0
            break
    
    if c == 1:
        list.append(num)
    num = num + 1
print(list)