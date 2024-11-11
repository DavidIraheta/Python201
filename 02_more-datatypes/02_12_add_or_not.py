# MEMORY GAME WITH SETS
# Continuously collect number input from a user with a `while` loop.
# Confirm that the input can be converted to an integer,
# then add it to a Python `set()`.
# If the element was already in the set, notify the user that their
# their input is a duplicate and deduct a point.
# If the user loses 5 points, quit the program.
# They win if they manage to create a set that has more than 10 items.
user_set = set()
points = 0
deductions = 0
while True:
    user_input = input("Enter a number: ")
    if not user_input.isdigit():
        print("Please enter a number.")
        continue
    user_input = int(user_input)
    if user_input in user_set:
        print("You already entered that number.")
        deductions += 1
        points -= 1
    else:
        user_set.add(user_input)
        points += 1
    if deductions == 5:
        print("You lost!")
        break
    if len(user_set) > 10:
        print("You win!")
        break
print(user_set)

        
