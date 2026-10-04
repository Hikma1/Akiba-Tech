customer_name = input("Enter your name: ")
product = input("Enter product name: ")
price = float(input("Enter the price of the product: "))
quantity = int(input("How many products do you want? : "))

total = price * quantity

print(f"Customer: {customer_name}")
print(f"Product Name: {product}")
print(f"Price of product: {price}")
print(f"Number of products: {quantity}")
print(f"Total: {total}")