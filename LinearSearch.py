def LinearSearch(array,key):
    for i in range(0,len(array)):
        if (array[i]==key):
            return i
    return -1


array=[]
n=int(input("enter size of array"))


for i in range(0, n):
    array.append(int(input("enter the element")))

find=int(input("enter a key"))
a=LinearSearch(array,find)

if a!=-1:
    print(f"element found at index {a}")
else:
    print("element not found")
