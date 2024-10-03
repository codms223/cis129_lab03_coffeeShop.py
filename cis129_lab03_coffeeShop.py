# cis129_lab03_coffeeShop.py
# This program calculates a receipt for coffee, muffins, cake, and tea with tax.

# Set the prices for items
coffee_price = 5.00
muffin_price = 4.00
strawberryshortcake_price = 7.00  # New item
cinnamonroll_price = 6.00   # New item
tax_rate = 0.06    # 6% tax

# Get user input
num_coffees = int(input("Number of coffees bought?\n"))
num_muffins = int(input("Number of muffins bought?\n"))
num_cakes = int(input("Number of cakes bought?\n"))  # New input
num_teas = int(input("Number of teas bought?\n"))    # New input

# Calculate the subtotal
coffee_total = num_coffees * coffee_price
muffin_total = num_muffins * muffin_price
cake_total = num_cakes * cake_price  # New total
tea_total = num_teas * tea_price      # New total
subtotal = coffee_total + muffin_total + cake_total + tea_total  # Updated subtotal

# Calculate the tax and total
tax = subtotal * tax_rate
total = subtotal + tax

# Display the receipt
print("\n***************************************")
print("My Coffee and Muffin Shop")
print(f"Number of coffees bought: {num_coffees}")
print(f"Number of muffins bought: {num_muffins}")
print(f"Number of cakes bought: {num_cakes}")  # New output
print(f"Number of teas bought: {num_teas}")    # New output
print("***************************************")

print("\n***************************************")
print("My Coffee and Muffin Shop Receipt")
print(f"{num_coffees} Coffee at ${coffee_price:.2f} each: $ {coffee_total:.2f}")
print(f"{num_muffins} Muffins at ${muffin_price:.2f} each: $ {muffin_total:.2f}")
print(f"{num_cakes} Cake at ${cake_price:.2f} each: $ {cake_total:.2f}")  # New output
print(f"{num_teas} Tea at ${tea_price:.2f} each: $ {tea_total:.2f}")      # New output
print(f"6% tax: $ {tax:.2f}")
print("---------")
print(f"Total: $ {total:.2f}")
print("***************************************")
