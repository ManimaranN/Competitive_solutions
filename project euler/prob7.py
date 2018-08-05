list = []
test = 0
list.append(2)
num = 3
while len(list) <= 10000:
    for i in range(2,num-1):
        if num % i == 0:
            test = 1
            break
        else:
            test = 0
    if test == 0:
        list.append(num)
    num = num+1

print(list)
ln = len(list)
print("largest prime number in the list of first 10001 prime numbers is: ", list[ln-1])

