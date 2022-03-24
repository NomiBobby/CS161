x = "3141592653589793238462643383279502884197169399375105820974944592"
y = "2718281828459045235360287471352662497757247093699959574966967627"

def karatsuba(x,y):
    length = len(x)
    if length == 1:
        return int(x) * int(y)

    a = x[0:length/2]
    b = x[length/2:]
    c = y[0:length/2]
    d = y[length/2:]
    print(a, b)
    print(c, d)
    result = karatsuba(a,b) + karatsuba(c,d)
    return result

result = karatsuba(x,y)

print(result)
    
