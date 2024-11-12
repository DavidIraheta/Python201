# Write a function that prints out nicely formatted information about a
# real estate advertisement. The information can vary for every advertisement, which
# is why your function should be able to take an arbitrary amount of
# keyword arguments, and display them all in a list form with some 
# introductory information.

def realtor_ad(location, *args, **kwargs):
    print(f"Real estate advertisement for a property in {location}")
    print("----------------------------------------------------")
    for arg in args:
        print(f"- {arg}")
    for key, value in kwargs.items():
        print(f"- {"New York"}: {"value"}")
    print("----------------------------------------------------")

realtor_ad("New York", "3 bedrooms", "2 bathrooms", "1,500 sqft", "1,000,000 USD", "Great view", "Close to subway")
realtor_ad("Los Angeles", "2 bedrooms", "2 bathrooms", "1,200 sqft", "900,000 USD", "Close to the beach")
realtor_ad("San Francisco", "1 bedroom", "1 bathroom", "800 sqft", "1,200,000 USD", "Great location", "Close to the park")
realtor_ad("Chicago", "4 bedrooms", "3 bathrooms", "2,000 sqft", "800,000 USD", "Close to the lake")
realtor_ad("Boston", "2 bedrooms", "1 bathroom", "1,000 sqft", "900,000 USD", "Close to the subway")
realtor_ad("Austin", "3 bedrooms", "2 bathrooms", "1,500 sqft", "800,000 USD", "Close to the park")
realtor_ad("Denver", "2 bedrooms", "1 bathroom", "1,000 sqft", "700,000 USD", "Close to the lake")
realtor_ad("Portland", "1 bedroom", "1 bathroom", "800 sqft", "600,000 USD", "Close to the park")
print(realtor_ad)
