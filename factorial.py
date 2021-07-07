def factorial( n ):
    if n < 0: 
        return -1    
    elif n == 0: 
        return 1
    else:
        return n * factorial( n - 1)

n = 6
print( factorial( n ) )