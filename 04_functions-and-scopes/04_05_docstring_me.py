# Add a Google-style docstring to the function below. Your docstring
# should at least describe what it does, what arguments it takes,
# and what it returns.

def km_to_miles(km):
    """This function to taking the argument kilometeres and converting it to miles.
    Args:
        km: float or int
    Returns:
        miles: float"""

    miles = km * 0.6
    return miles

print(km_to_miles.__doc__)
