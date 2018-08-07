def cross(list,num):
    sum2 = 0
    for j in range(0, 17):
        sum1 = 0
        for k in range(j, j+4):
            if num == 1:
                sum1 = sum1 + a[j][k]
            elif num == 2:
                sum1 = sum1 + a[k][j]
            elif num == 3:
                sum1 = sum1 + a[k][k+1]
            elif num == 4:
                sum1 = sum1 + a[k+1][k]
            elif num == 5:
                sum1 = sum1 + a[k][k]
            if sum1>sum2:
                sum2 = sum1
    return sum2


a =[]
for i in range(20):
    a.append(list(map(int,input().split())))
list = []
sum_r = 0

for i in range(20):
    sum = cross(a, 1)
    if sum > sum_r:
        sum_r=sum 

for i in range(20):
    sum = cross(a, 2)
    if sum > sum_r:
        sum_r=sum 

for i in range(17):
    sum = cross(a, 3)
    if sum > sum_r:
        sum_r=sum 

for i in range(17):
    sum = cross(a, 4)
    if sum > sum_r:
        sum_r=sum 

sum = cross(a, 5)
if sum > sum_r:
        sumr=sum 

print(sum_r)



           
        
    

        
        
        
            
        

    
         
        

   



