
fib = [1, 1]
i = 1
add = 0
while add < 4000000:
    add = fib[i] + fib[i - 1]
    if add <= 4000000:
        fib.append(add)
        i += 1






fib_res = []

for i in range (1, len(fib)):
    if fib[i] % 2 == 0:
        fib_res.append(fib[i])

res = sum(fib_res)

print ("the sum of the even-valued terms in the Fibonacci sequence whose values do not exceed four million: ", res)

