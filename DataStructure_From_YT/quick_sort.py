
#https://www.youtube.com/watch?v=kFeXwkgnQ9U&t=92s
def quick_sort(sequence):
    length = len(sequence)
    #print(f"sequenc: {sequence} {length}")
    if length <= 1:
        #print("return 1 ", sequence)
        return sequence
    else:       
        pivot = sequence.pop()
    items_greater = []
    items_lower = []
    for item in sequence:
        if item > pivot:
            items_greater.append(item)
        else:
            items_lower.append(item)
    return quick_sort(items_lower) + [pivot] + quick_sort(items_greater)

print(quick_sort([5,6,7,8,9,8,7,6,5,6,7,8,9,0]))
#print(quick_sort([5,1,3,9]))