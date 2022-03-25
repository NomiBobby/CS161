x = "3141592653589793238462643383279502884197169399375105820974944592"
y = "2718281828459045235360287471352662497757247093699959574966967627"

# Single Digit Multiplication
sum = 0
for i in range(len(x)):
    for j in range(len(y)):
        increase = int(x[len(x) - i - 1]) * int(y[len(y) - j - 1]) * (10 ** (i + j))
        sum  = sum + increase
print()
xxx = f"x is {x}"
print(f"Single Digit Result: {sum}")

# Karatsuba Mutiplication
def karatsuba(x,y):
    n = len(x)

    # Base Case
    if n == 1:
        return int(x) * int(y)

    a = x[0:n/2]
    b = x[n/2:]
    c = y[0:n/2]
    d = y[n/2:]
    ac = karatsuba(a, c)
    ad = karatsuba(a, d)
    bc = karatsuba(b, c)
    bd = karatsuba(b, d)
    result = (10 ** n) * ac + (10 ** (n/2)) * (ad + bc) + bd
    return result

result = karatsuba(x,y)
print(result)