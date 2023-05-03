def gcd(x,y):
    if y==0:
        return x
    else:
        return gcd(y,x%y)
    

a=int(input("enter a number"))
b=int(input("enter another number"))

print("gcd is " , gcd(a,b))
    