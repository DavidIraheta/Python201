# Write code that removes all duplicates from a list.
# Solve this challenge in two ways:
# 1. Convert to a different data type
# 2. Use a loop and a second list to solve it more manually

list_ = [1, 2, 3, 4, 3, 4, 5]
# list_ = list(set(list_))
# print(list_)
new_list = []
for i in list_:
    if i not in new_list:
        new_list.append(i)
print(new_list)
