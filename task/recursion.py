def fact(n):
    if n == 0:
        return 1  
    else:
        return n + fact(n - 1)

n = int(input("Enter a number: "))
f = fact(n)
print("Factorial of", n, "is", f)
