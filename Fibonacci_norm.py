i = 0
j = 1
k = 0
fib = 0
while i < 30:
    print( str(i + 1) + ". ", fib)
    fib = j + k
    j = k
    k = fib
    i = i+1
