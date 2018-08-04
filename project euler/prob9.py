a=b=c=range(500,1,-1)
for num1 in a:
    for num2 in b:
        for num3 in c:
            if not num1<num2<num3:
                continue
            if num1+num2+num3 == 1000:
                if num1**2 + num2**2 == num3**2:
                    print(num1, num2, num3)
                    result = num1*num2*num3
print (result)             