list = []
for i in range(3,1000):
    if i%3 == 0:
        list.append(i)
    elif i%5 == 0 :
        list.append(i)
    i += 1
add = sum(list)
print("sum :", add)



