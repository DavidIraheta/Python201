# Write a script where you complete the following tasks:
# - define a function that determines whether the number is
#   divisible by 4 OR 7 and returns a boolean
# - define a function that determines whether a number is
#   divisible by both 4 AND 7 and returns a boolean
# - take in a number from the user between 1 and 1,000,000,000
# - call your functions, passing in the user input as the arguments,
#   and set their output equal to new variables 
# - print your the result variables with descriptive messages

def four_or_seven(number):
    if number % 4 == 0 or number % 7 == 0:
        return True
    else:
        return False
    
def four_and_seven(number):
    if number % 4 == 0 and number & 7 == 0:
        return True
    else: 
        return False 
    
user_input = int(input("Enter a number betweeen 1 and 1,000,000,000: "))
result_1 = four_or_seven(user_input)
result_2 = four_and_seven(user_input)

print(f"Is {user_input} divisible by 4 or 7? {result_1}")
print(f"Is {user_input} divisble by 4 and 7? {result_2}")


