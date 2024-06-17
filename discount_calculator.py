def calculate_discount(price, discount_percent):
    """
    Calculate the final price after applying the discount if it's 20% or higher.
    
    Parameters:
    price (float): The original price of the item.
    discount_percent (float): The discount percentage to be applied.
    
    Returns:
    float: The final price after applying the discount, or the original price if the discount is less than 20%.
    """
    if discount_percent >= 20:
        return price - (price * discount_percent / 100)
    else:
        return price

def main():
    # Prompt the user to enter the original price
    try:
        price = float(input("Enter the original price of the item: "))
    except ValueError:
        print("Invalid input. Please enter a valid number for the price.")
        return

    # Prompt the user to enter the discount percentage
    try:
        discount_percent = float(input("Enter the discount percentage: "))
    except ValueError:
        print("Invalid input. Please enter a valid number for the discount percentage.")
        return

    # Calculate the final price after applying the discount
    final_price = calculate_discount(price, discount_percent)

    # Print the final price or the original price
    if final_price != price:
        print(f"The final price after applying the discount is: ${final_price:.2f}")
    else:
        print(f"No discount applied. The original price is: ${price:.2f}")

if __name__ == "__main__":
    main()
