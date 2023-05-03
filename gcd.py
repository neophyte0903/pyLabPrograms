number1=int(input("enter first number"))
number2=int(input("enter second number"))

minimum=min(number1,number2)


gcd=1

for factors in range (1,minimum+1):
    if(number1%factors==0 and number2%factors==0):
        gcd=factors
print(gcd)