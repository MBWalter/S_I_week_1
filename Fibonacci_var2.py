i = 0
j = 1
k = 0
fib = 0
number_want = int(input("How many of the Fibonacci numbers you want to see from the smallest: "))
while i < number_want:
    print( (str(i + 1) + ":").ljust(4, ' ') + str(fib).rjust(30, ' '))
    fib = j + k
    j = k
    k = fib
    i = i+1
