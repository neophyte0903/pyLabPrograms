def squareRoot(n,iterations):
    a=float(n)

    for i in range(iterations):
        n=0.5*(n+(a/n))
    return n


a=int(input("enter a number to find squareroot of"))

print(squareRoot(a,100))

