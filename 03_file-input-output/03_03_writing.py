# Write a script that reads in the contents of `words.txt`
# and writes the contents in reverse to a new file `words_reverse.txt`.
from pathlib import Path

original_file = Path("/Users/davidiraheta/Documents/CodingNomads/Projects/python-201-main/03_file-input-output/words.txt")
reversed_file = Path("/Users/davidiraheta/Documents/CodingNomads/Projects/python-201-main/03_file-input-output/words_reverse.txt")
for f in [original_file, reversed_file]:
    if not f.exists():
        print(f"Error: {f} does not exist.")
        exit(1)
with open(original_file, "r") as file:
    words = file.read().split()
    reversed_words = "\n".join(words[::-1])

    with open(reversed_file, "w") as file:
        file.write(reversed_words)
        print(reversed_words)

