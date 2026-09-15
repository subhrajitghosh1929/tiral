def convert_dollars_to_rupees(amount_in_dollars, conversion_rate):
    amount_in_rupees = amount_in_dollars * conversion_rate
    return amount_in_rupees

def convert_dollars_to_rupees_void(amount_in_dollars, conversion_rate):
    amount_in_rupees = amount_in_dollars * conversion_rate
    print("Amount in rupees:", amount_in_rupees)

amount = float(input("Enter amount in dollars "))
conversion_rate = float(input("Enter conversion rate "))

# Non-void function call
converted_amount = convert_dollars_to_rupees(amount, conversion_rate)
print("Converted amount (non-void function):", converted_amount)

# Void function call
convert_dollars_to_rupees_void(amount, conversion_rate)
