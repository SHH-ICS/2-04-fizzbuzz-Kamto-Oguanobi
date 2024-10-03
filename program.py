# My Python Program
# Task:  use if statements to output the result of the game fizzbuzz.  
# Start at 1
# For multiples of 3, output   Fizz
# For multiples of 5, output   Buzz
# For multiples of 15, output   FizzBuzz
# End at 32

result = ""
for myNumber in range(1, 33):
    if myNumber % 15 == 0:
        result += "FizzBuzz\n"
    elif myNumber % 3 == 0:
        result += "Fizz\n"
    elif myNumber % 5 == 0:
        result += "Buzz\n"
    else:
        result += str(myNumber) + "\n"

print(result)