'''hackerrank Test: Python Alphabet Filter
This code is fully copy from hackrank
input: hackerrank
output:
hckrrnk
aea
resource: 
https://stackoverflow.com/questions/10289761/python-strings-consonants/10289856
https://stackoverflow.com/questions/43164161/how-to-count-vowels-and-consonants-in-python
''' 
class LetterFilter:

    def __init__(self, s):
        self.s = s      

# Enter your code here. 
# Complete the classes below.
# Reading the inputs and writing the outputs are already done for you.
#
# class LetterFilter:
#
    #def __init__(self, s):
       #self.s = s
	
    def filter_vowels(self):                
        # Enter your code here
        # Return a string       
        vowel = "aeiou"
        count = 0
        arr = []
        for y in self.s:
            if y in vowel:
                arr.append(y)
                count += 1
        result = self.convertListStr(arr)
        return result
            
    def filter_consonants(self):
        # Enter your code here
        # Return a string
        consonants = "bcdfghjklmnpqrstvwxyz"
        count = 0
        arr = []
        #print(self.s)
        for y in self.s:
            if y in consonants:
                arr.append(y)
                count += 1
        result = self.convertListStr(arr)
        return result
    def convertListStr(self,text):        
        str= ""
        result = str.join(text)
        return result
s = input("please enter string: ")
f = LetterFilter(s)
print(f.filter_vowels())
print(f.filter_consonants())

##############################################################

'''
This is same, just not used hankrank code, i modify myself with no class

def consonants(text):
    consonants = "bcdfghjklmnpqrstvwxyz"
    count = 0
    arr = []
    for y in text:
        if y in consonants:
            arr.append(y)
            count += 1
    result = convertListStr(arr)
    return result
    #print(arr)

def vowel(text):
    vowel = "aeiou"
    count = 0
    arr = []
    for y in text:
        if y in vowel:
            arr.append(y)
            count += 1
    result = convertListStr(arr)
    return result
    #print(arr)

#this is the same as consonants
def vowelnot(text):
    vowel = "aeiou"
    count = 0
    arr = []
    for y in text:
        if y not in vowel:
            arr.append(y)
            count += 1
    result = convertListStr(arr)
    return result
def convertListStr(text):
    str= ""
    result = str.join(text)
    return result

text = "hackerank"
print(vowel(text))
print(consonants(text))
print( vowelnot(text))

'''

#################

''' another way without array
def eliminate_consonants(x):
        vowels= ['a','e','i','o','u']
        for char in x:
            if char not in vowels:
                print(char, end = "")

eliminate_consonants('mississippi')
'''