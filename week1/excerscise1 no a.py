def fib(n):
    a = 0
    b = 1
    for i in range(n):
        print(a)
        a,b =b, a+b
        
n = int(input("How many terms do you wanna use:"))
fib(n)
        