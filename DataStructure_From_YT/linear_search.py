def linearsearch(list11, key):
    for i in range (len(list)):
        if list11[i] == key:
            return i
    else:
        return "key not in lists"

list = [1,3,5,11,44,55]
key = int (input("please enter your keys: "))
print(list)
result = linearsearch(list, key)
print(f"result are: {result} ")