income = float(input("Enter the income: "))

if income <= 85528:
    tax = income * 0.18 - 556.02
else:
    tax = 14839.02 + 0.32 * (income - 85528)

tax = round(tax)
print("The calculated tax is:", tax, "thalers")