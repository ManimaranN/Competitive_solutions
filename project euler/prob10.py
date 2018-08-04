list = []
test = 0
list.append(2)
num = 3
while num <= 2000000:
    for i in range(2,num-1):
        if num % i == 0:
            test = 1
            break
        else:
            test = 0
    if test == 0:
        list.append(num)
    num = num+1
result = sum(list)
print(result)
print(list)

# 2000000