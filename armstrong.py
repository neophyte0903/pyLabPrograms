n=int(input("enter a number"))

s=str(n)
l=[]
for i in s: #insertion
    l.append(i)

r=len(l)
sum=0

for i in l: #traversal
    sum=sum+(int(i)**r)

print(sum)

if sum==n:
    print("number is armstrong")

else:
    print("not armstrong")
    
    
