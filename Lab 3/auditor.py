total_inventory = 0
failed_entries = 0
while True:
    stock_quantity = input("Enter the quantity of stock to add (or enter 'quit' to quit): ")
    if stock_quantity.lower() == 'quit': #.lower() covert all letters in a string to lowercase
        break
    if stock_quantity.startswith("-") and stock_quantity[1:].isdigit(): #[1:] is used to slice the string and get the substring starting from index 1 to the end of the string. This is done to check if the rest of the string after the negative sign is a valid number.
        print("Invalid input. Please enter a positive number.")
        failed_entries += 1
        continue
    elif not stock_quantity.isdigit():
        print("Invalid input. Please enter a valid number.")
        failed_entries += 1
        continue
    else:
        total_inventory += int(stock_quantity)
    if total_inventory > 500:
        print("Warning: Total inventory exceeds 500 units! Please review your entries.")
        break

    print(f"Current Inventory: {total_inventory} units")

print(f"Total Units Processed: {total_inventory}")
print(f"Number of Failed/Rejected Entries: {failed_entries}")