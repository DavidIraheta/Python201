# Write a program with three functions. Each function must call
# at least one other function and use the return value
# of that function to do something with it. You can have more
# than three functions, and they don't need to call each other
# in a circular way.

def monthly_savings(income, expenses):
    savings = income - expenses
    return savings
def yearly_savings(savings):
    yearly = savings * 12
    return yearly
def calculate_total_savings(income, expenses, intrest_rate):
    savings = monthly_savings(income, expenses)
    yearly = yearly_savings(savings)
    total = yearly * intrest_rate
    return total

print(calculate_total_savings(5500, 2300, 4.05))
