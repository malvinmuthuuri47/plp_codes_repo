def calculate_discount(price, discount_percentage):
    """
    # check if the discount is greater than or equal to 20%
    # if it is greater than 20%, return the discounted price
    # otherwise return the original price
    """
    if (discount_percentage / 100) >= 0.2:
        return (price * (discount_percentage / 100))
    else:
        return 0

def main():
    price = float(input("Enter the Price here: "))
    discount = float(input("Enter the discount on a scale of 0 to 100 here: "))
    
    final_price = price - (calculate_discount(price, discount))

    print(f"The final price after applying the discount is: {final_price}")

if __name__ == '__main__':
    main()
