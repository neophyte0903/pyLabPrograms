import sys

print("name of file", sys.argv[0])

print(len(sys.argv))

sum=0

n=len(sys.argv)
for i in range(1,n):
    sum=sum+int(sys.argv[i])


print("result is ",sum)
