# Write a function named `stats()` that takes in a list of numbers
# and finds the maximum, minimum, average and sum of the numbers.
# Print these values to the console you call the function.

example_list = [1, 2, 3, 4, 5, 6, 7]

def stats():
  # define the function here
  pass

# call the function below here

def stats(numbers):
    maximum = max(numbers)
    minimum = min(numbers)
    average = sum(numbers) / len(numbers)
    total = sum(numbers)
    print(f"Maximum: {maximum}")
    print(f"Minimum: {minimum}")
    print(f"Average: {average}")
    print(f"Total: {total}")

stats(example_list)
