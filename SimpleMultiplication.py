x = "3141592653589793238462643383279502884197169399375105820974944592"
y = "2718281828459045235360287471352662497757247093699959574966967627"

sum = 0

for i in range(len(x)):
    for j in range(len(y)):
        increase = int(x[len(x) - i - 1]) * int(y[len(y) - j - 1]) * (10 ** (i + j))
        sum  = sum + increase
        # print("i=", i, "j=", j, "increase=", increase)

print(sum)