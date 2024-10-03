# cis129_lab03_coffeeShop.py
# This program calculates a receipt for coffee and muffins with tax.

# Step 1: Set the prices for coffee and muffins
coffee_price = 5.00
muffin_price = 4.00
tax_rate = 0.06  # 6% tax

# Step 2: Get user input
num_coffees = int(input("Number of coffees bought?\n"))
num_muffins = int(input("Number of muffins bought?\n"))

# Step 3: Calculate the subtotal
coffee_total = num_coffees * coffee_price
muffin_total = num_muffins * muffin_price
subtotal = coffee_total + muffin_total

# Step 4: Calculate the tax and total
tax = subtotal * tax_rate
total = subtotal + tax

# Step 5: Display the receipt
print("\n***************************************")
print("My Coffee and Muffin Shop")
print(f"Number of coffees bought?\n{num_coffees}")
print(f"Number of muffins bought?\n{num_muffins}")
print("***************************************")

print("\n***************************************")
print("My Coffee and Muffin Shop Receipt")
print(f"{num_coffees} Coffee at ${coffee_price:.2f} each: $ {coffee_total:.2f}")
print(f"{num_muffins} Muffins at ${muffin_price:.2f} each: $ {muffin_total:.2f}")
print(f"6% tax: $ {tax:.2f}")
print("---------")
print(f"Total: $ {total:.2f}")
print("***************************************")
exit()
