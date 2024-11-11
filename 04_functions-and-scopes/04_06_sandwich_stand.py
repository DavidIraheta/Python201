# Write a function called `make_sandwich()` that sticks to the following:
# - takes a type of bread as its first, required argument
# - takes an arbitrary amount of toppings
# - returns a string representing a sandwich with the bread on top
#   and bottom, and the toppings in between.

def make_sandwich(meat, bread, *toppings):
    toppings_list = " ".join(toppings)
    sandwich = f"{meat} sandwich with {toppings} and {"".join(bread)} on top and bottom."
    return sandwich

print(make_sandwich("Turkey","wheat bread","Swiss","Lettuce, Tomato","Mayo"))