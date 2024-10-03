# cis129_lab03_coffeeShop.py
# This program calculates a receipt for coffee, muffins, strawberryshortcake, and cinnamonroll with tax.

# Set the prices for items
coffee_price = 5.00
muffin_price = 4.00
strawberryshortcake_price = 7.00  # New item
cinnamonroll_price = 6.00   # New item
tax_rate = 0.06    # 6% tax

# Get user input
num_coffees = int(input("Number of coffees bought?\n"))
num_muffins = int(input("Number of muffins bought?\n"))
num_strawberryshortcakes = int(input("Number of strawberryshortcake bought?\n"))  # New input
num_cinnamonrolls = int(input("Number of cinnamonrolls bought?\n"))    # New input

# Calculate the subtotal
coffee_total = num_coffees * coffee_price
muffin_total = num_muffins * muffin_price
strawberryshortcake_total = num_strawberryshortcakes * strawberryshortcake_price  # New total
cinnamonroll_total = num_cinnamonrolls * cinnamonroll_price      # New total
subtotal = coffee_total + muffin_total + strawberryshortcake_total + cinnamonroll_total  # Updated subtotal

# Calculate the tax and total
tax = subtotal * tax_rate
total = subtotal + tax

# Display the receipt
print("\n***************************************")
print("My Coffee and Muffin Shop")
print(f"Number of coffees bought: {num_coffees}")
print(f"Number of muffins bought: {num_muffins}")
print(f"Number of strawberryshortcakes bought: {num_strawberryshortcakes}")  # New output
print(f"Number of cinnamonrolls bought: {num_cinnamonrolls}")    # New output
print("***************************************")

print("\n***************************************")
print("My Coffee and Muffin Shop Receipt")
print(f"{num_coffees} Coffee at ${coffee_price:.2f} each: $ {coffee_total:.2f}")
print(f"{num_muffins} Muffins at ${muffin_price:.2f} each: $ {muffin_total:.2f}")
print(f"{num_strawberryshortcakes} strawberryshortcakes at ${strawberryshortcake_price:.2f} each: $ {strawberryshortcake_total:.2f}")  # New output
print(f"{num_teas} cinnamonrolls at ${cinnamonroll_price:.2f} each: $ {cinnamonroll_total:.2f}")      # New output
print(f"6% tax: $ {tax:.2f}")
print("---------")
print(f"Total: $ {total:.2f}")
print("***************************************")
print("Thank you for visiting My Coffee and Muffin Shop. One cup of coffee makes one's day :)")
