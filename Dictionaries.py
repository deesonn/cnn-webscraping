'''
You are managing a grocery store's inventory. Write a Python program to:

Store the initial inventory as a dictionary where the keys are the names of items 
(e.g., 'apples', 'bananas') and the values are the quantities in stock (e.g., 10, 20).
Allow the user to:
Add new items to the inventory.
Update the quantity of an existing item.
Check the stock for a specific item.
At the end, display the entire inventory.
'''

inventory = {'apples' : 10, 'bananas' : 20, 'pears' : 22, 'jack fruit' : 8, 'oranges' : 15}

# Display menu with options
print("1. Add a new item \n" +
      "2. Update an existing item \n" +
      "3. Check the stock for a specific item \n" +
      "4. Display the entire inventory \n" +
      "5. Quit ")

# User choices
user_choice = input("Enter an option: ")

# Check user choice
if user_choice == 1:
      

# Prompt user to add new items to inventory
new_item = input("Enter a new grovery item and its quantity e.g. (apples 10): ")
# Split() to split new_item's item and quantity
item, quantity = new_item.split()
# Turn quantity into an integer
quantity = int(quantity)
# Add item and quantity to inventory dictionary (appending)
inventory[item] = quantity
# Display inventory
print(inventory)
