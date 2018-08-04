import math

def check(num):
    no = int(math.sqrt(num))
    for i in range(2,no+1):
        if num % i == 0:
            return False
    return True
   
sum = 2
list = []
for num in range(3,2000000):
    test1 = check(num)
    if check(num):
        sum += num
        list.append(num)
    num = num+1
print(list)
print(sum)

# 2000000