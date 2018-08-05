a =[]
for i in range(20):
    a.append(list(map(int,input().split())))
list = []
sum = 0
sum1 = 0
for j in range(20):
    for key in range(0, 17):
        for k in range(key, key+4):
                sum1 = sum1 + a[j][k]
        if sum1 > sum:
            sum = sum1
        sum1 = 0

for j in range(20):
    for key in range(0, 17):
        for k in range(key, key+4):
                sum1 = sum1 + a[k][j]
        if sum1 > sum:
            sum = sum1
        sum1 = 0

for j in range(20):
    for key in range(0,17):
        for k in range(key,key+4):
            sum1 = sum1 + a[k][k]
        if sum1 > sum:
            sum = sum1
        sum1 = 0


for i in range(17):
    for key in range(0,17):
        for k in range(key, key+4):
            sum1 = sum1 + a[key][key+1]
        if sum1 > sum:
            sum = sum1
        sum1 = 0

for i in range(17):
    for key in range(0,17):
        for k in range(key, key+4):
            sum1 = sum1 + a[key+1][key]
        if sum1 > sum:
            sum = sum1
        sum1 = 0


print(sum)


        
        
            
        

    
         
        

   



