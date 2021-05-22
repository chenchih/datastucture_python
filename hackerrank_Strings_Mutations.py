'''
Mutations: change string's specfic postion

Input: 
STDIN           Function
-----           --------
abracadabra     s = 'abracadabra'
5 k             position = 5, character = 'k'

output:
abrackdabra 

>>> string = "abracadabra"
>>> l = list(string)
>>> l[5] = 'k'
>>> string = ''.join(l)
>>> print string
abrackdabra

reference: https://www.geeksforgeeks.org/python-program-convert-string-list/
'''
def mutate_string(string, position, character):
    list1= []
    list1[:0]=string
    list1[position] = character  

    return "".join(list1)

if __name__ == '__main__':
    s = input()
    i, c = input().split()
    s_new = mutate_string(s, int(i), c)
    print(s_new)