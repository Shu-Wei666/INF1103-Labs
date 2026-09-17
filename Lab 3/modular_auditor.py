#Function to get and validate user input
def get_valid_input():
    stock_quantity = input("Enter the quantity of stock to add (or enter 'quit' to quit): ")
    if stock_quantity.lower() == 'quit': #.lower() covert all letters in a string to lowercase
        return "quit"
    if stock_quantity.startswith("-") and stock_quantity[1:].isdigit(): #[1:] is used to slice the string and get the substring starting from index 1 to the end of the string. This is done to check if the rest of the string after the negative sign is a valid number.
        print("Invalid input. Please enter a positive number.")
        return None
    elif not stock_quantity.isdigit():
        print("Invalid input. Please enter a valid number.")
        return None
    else:
        return int(stock_quantity)    

# Function to add the new delivery to the current inventory
def process_delivery(current_total, new_value):
    return current_total + new_value

# Function to calculate 10% tax for a delivery
def calculate_tax(amount):
    return amount * 0.10

# Function to generate the final report
def generate_report(total_units,failed_attempts):
    print(f"Total Units Processed: {total_units}")
    print(f"Number of Failed/Rejected Entries: {failed_attempts}")

total_inventory = 0
failed_entries = 0
deliveries_processed = 0

while True:
    stock_quantity = get_valid_input()

    if stock_quantity == 'quit': 
        break

    if stock_quantity is None:
        failed_entries += 1
        continue

    total_inventory = process_delivery(total_inventory, stock_quantity)
    deliveries_processed += 1

    tax = calculate_tax(stock_quantity)

    if total_inventory > 500:
        print("Warning: Total inventory exceeds 500 units! Please review your entries.")
        break

    print(f"Current Inventory: {total_inventory} units")
    print(f"Tax for this delivery: $ {tax}")

generate_report(total_inventory,failed_entries)