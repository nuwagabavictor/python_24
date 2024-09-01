def calculate_discount(price, discount_percent):
    if discount_percent >= 20:
        discount_amount = price * (discount_percent / 100)
        final_price = price - discount_amount
        return final_price
    else:
        return price

# Prompt the user for input
price = float(input("Enter the price of the item: "))
discount_percentage = float(input("Enter the discount percentage: "))

# Calculate the final price
final_price = calculate_discount(price, discount_percentage)

# Display the result
if final_price < price:
    print(f"The final price after a {discount_percentage}% discount is: ${final_price:.2f}")
else:
    print(f"No discount applied. The original price is: ${price:.2f}")
    #or
print(f"the final price is: {calculate_discount(100,20)}")
