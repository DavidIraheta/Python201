# Using f-strings, print out the name, last name, and favorite
# office supply item of each person in the given dictionary,
# formatted like so:
#
# LASTNAME, Name           Office supply item
# LONGERLASTNAME, Name     Office supply item
office = [
    {"full_name": "Michael Scott", "item": "world's best boss mug"},
    {"full_name": "Dwight Schrute", "item": "pepper spray"},
    {"full_name": "Jim Halpert", "item": "phone"},
    {"full_name": "Pam Beesly", "item": "post-its"},
    {"full_name": "Ryan Howard", "item": "business cards"},
    {"full_name": "Stanley Hudson", "item": "crossword-puzzle"},
    {"full_name": "Kevin Malone", "item": "m&ms"},
    {"full_name": "Meredith Palmer", "item": "flask"},
    {"full_name": "Angela Martin", "item": "cat food"},
    {"full_name": "Oscar Martinez", "item": "calculator"},
    {"full_name": "Phyllis Lapin", "item": "cut flowers"},
    {"full_name": "Kelly Kapoor", "item": "People magazine"},
    {"full_name": "Toby Flenderson", "item": "files"},
    {"full_name": "Creed Bratton", "item": "mung beans"},
    {"full_name": "Darryl Philbin", "item": "forklift"},
]


office_favorites = []
for person in office:
    name = person["full_name"].split()
    first_name = name[0]
    last_name = name[1].upper()
    item = person ["item"]
    new_name = last_name + ", " + first_name
    office_favorites.append(f'{new_name:<20} {person["item"]}')
for item in office_favorites:
    print(item)
# office_favorites = []
# for person in office:
#     name = person["full_name"].split()
#     last_name = name[1]
#     first_name = name[0]
#     item = person["item"]
#     office_favorites.append((last_name, first_name, item, len(last_name)))
    
#     print(f"[{last_name}, {first_name:<20}] {item}")








# print(f"{office_favorites <20}, {last_name<20, first_name}")
# for i in range(len(office_favorites)):
#     for j in range(0, len(office_favorites) - i - 1):
#         if office_favorites[j][3] > office_favorites[j + 1][3]:
#             office_favorites[j], office_favorites[j + 1] = office_favorites[j + 1], office_favorites[j]
# longest_lastname_length = 0
# for last_name, first_name, item, length in office_favorites:
#     if length > longest_lastname_length:
#         longest_lastname_length = length
# for last_name, first_name, item, _ in office_favorites:
#     print(f"{last_name}, {first_name:<{longest_lastname_length + 1}}{item}")
