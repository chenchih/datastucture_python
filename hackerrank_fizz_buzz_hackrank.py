
def fizzBuzz(n):
 
    # Write your code here
   
    for num in range(1, n+1):
        if num % 3 == 0 and num % 5 == 0:
            print("FizzBuzz")
        elif num % 3 is 0:
            print("Fizz")
        elif num % 5 is 0:
            print("Buzz")
        else:
            print(num)

    

if __name__ == '__main__':
    n = int(input().strip())

    fizzBuzz(n)