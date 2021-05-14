#binary search all list must be in order
def BinarySearch(list, key):
    left =0
    right = len(list)-1
    result = -1
    
    while left <= right:
        mid = (left+right)//2
        if list[mid] == key:
            result = mid
            return mid
        if list[mid] < key:
            left = mid +1 
            #return left
        else:
            right = mid -1 
            #return right
    return "not in list"


list1 = [23 , 50, 60, 11]
list1.sort()
print(list1)
key = int(input("Enter the key to search: "))
res= BinarySearch(list1, key)
print(res)