x = 0
fib = [0,1]
while True:
    if (x==0):
        print("0")
    if (x==1):
        print("1")
    else:
        fib.append(fib[len(fib)-1]+fib[len(fib)-2])
        print(fib[len(fib)-1])
    x = x + 1
