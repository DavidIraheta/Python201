# Reproduce the functionality of Python's built-in `enumerate()` function.
# Define a function called `my_enumerate()` that takes an iterable as input
# and gives back both the element as well as its index position as an integer.

def my_enumerate(iterable, start =0): 
      index = start
      for item in iterable:
        yield index, item
        index += 1
 # add your arguments
      # add your code implementation
      pass

pantry_items = ["brown_rice", "arborio_rice", "quinoa", "rice_pilaf", "pasta", "wild_rice","garbanzo_beans", "black_beans","chocolate","candy_bars","granola_bars", "cereal"]  

for index, item in enumerate(pantry_items):
      print(f"Item {index}: {item}")
