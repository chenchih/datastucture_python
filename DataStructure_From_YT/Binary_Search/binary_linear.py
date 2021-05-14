def binary_search(numbers_list, item):
    left_index = 0
    right_index = len(numbers_list) - 1

    while left_index <= right_index:
        midpoint = left_index + (right_index - left_index) // 2
        # or 
        #midpoint = (left_index + right_index) // 2
        midpoint_value = numbers_list[midpoint]
        if midpoint_value == item:
            return midpoint
        elif item < midpoint_value:
            right_index = midpoint - 1
        else:
            left_index = midpoint + 1
    return "Not in List "
def binary_search_recursive(numbers_list, item, left_index, right_index):
    if right_index < left_index:
        return "Not in List "
    mid_index = (left_index + right_index) // 2
    if mid_index >= len(numbers_list) or mid_index < 0:
        return "Not in List "
    mid_number = numbers_list[mid_index]
    if mid_number ==  item:
        return mid_index
    if mid_number <  item:
        left_index = mid_index + 1
    else:
        right_index = mid_index - 1

    return binary_search_recursive(numbers_list, item, left_index, right_index)

def linear_search_1(numbers_list, item):
    for index, element in enumerate(numbers_list):
        if element == item:
            return index
    return "Not in List "
def linear_search(numbers_list, item):   
    for i in range (len(numbers_list)):
        if numbers_list[i] == item:
            return i
    else:
        return "key not in lists"    


if __name__ == '__main__':
    #iteration method
    numbers_list = [2,4,5,6,7,8,9,10,12,13,14]
    find_target = 2
    print(f"List are:{numbers_list} \nFind Target: {find_target} ")
    print("")
    #print(binary_search(numbers_list, find_target))
    print(f"(Iteration Method) {binary_search(numbers_list, find_target)} ")
    #recression
    #print(binary_search_recursive(numbers_list, find_target, 0, len(numbers_list)))
    print(f"(Iteration Method) {binary_search_recursive(numbers_list, find_target, 0, len(numbers_list))} ")
   
    print(f"(Linear Method) {linear_search(numbers_list, find_target)} ")
