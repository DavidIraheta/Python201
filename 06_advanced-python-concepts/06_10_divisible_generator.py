# Create a Generator that loops over the given range and prints out only
# the items that are divisible by 1111.

nums = range(1, 1000000)
generator = (i for i in nums if i % 1111 == 0 )
for i in generator:
    print(i)
