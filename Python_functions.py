def  calculate_discount(price, discount_percent):  
    if (discount_percent >= 20):
        percentage = discount_percent / 100
        discount = percentage * price
        discounted_price = price - discount
        return discounted_price
    else:return price



if __name__ == "__main__":
    price = float(input("Enter Product Price: "))
    discount_percent = float(input("Enter Discount Percentage: "))
    
    discounted_price = calculate_discount(price, discount_percent)
    if discounted_price < price:
        print(f"The discounted price is: {discounted_price}")
    else:
        print(f"No discount applied. The price remains: {price}")