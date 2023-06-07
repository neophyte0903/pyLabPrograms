def binary(array,key):
    low=0
    high=len(array)-1
    mid=0


    while low<=high:
        mid=(high+low)//2
        if array[mid]< key:
            low=mid+1
        elif array[mid] < key:
            high=mid-1
        else:
            return mid
    return -1



myArray=[2,3,6,7,8,91,213,341]

print("element found at",binary(myArray,213))