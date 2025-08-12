def calculate_discount(price, discount_percent):
    if discount_percent >= 20:
        discount_amount = price * (discount_percent / 100)
        final_price = price - discount_amount
        return final_price
    else:
        return price
    
# Get OG price
while True:
    try:
        original_price = float(input("Enter the original price: "))
        if original_price < 0:
            print("Price cannot be negative. Please enter a valid price.")
            continue
        break
    except ValueError:
        print("Invalid input. Please enter a valid number.")

# Get discount percent
while True:
    try:
        discount_price = float(input("Enter the discount percent: "))
        if discount_price < 0:
            print("Discount percent cannot be negative. Try again.")
            continue
        break
    except ValueError:
        print("Invalid input. Please enter a valid number.")

# Calculate final price after discount
final_price = calculate_discount(original_price, discount_price)

# Show the final price
if final_price != original_price:
    print(f"Discount applied! Final price: {final_price:.2f}")
else:
    print(f"No discount applied. Final price remains: {final_price:.2f}")