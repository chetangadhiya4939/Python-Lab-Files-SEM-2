print("GADHIYA CHETAN BHAVESHBHAI\n23BCP182\nD-3.")
class GroceryList:

  def __init__(self):
    self.items = []

  def add_item(self, item):
    self.items.append(item)

  def remove_item(self, item):
    if item in self.items:
      self.items.remove(item)
    else:
      print(f"{item} is not in the list.")

  def modify_item(self, old_item, new_item):
    if old_item in self.items:
      index = self.items.index(old_item)
      self.items[index] = new_item
    else:
      print(f"{old_item} is not in the list.")

  def display_list(self):
    print("Grocery List:")
    for item in self.items:
      print(item)


grocery_list = GroceryList()

# Add items to the list
grocery_list.add_item("Apples")
grocery_list.add_item("Bananas")
grocery_list.add_item("Milk")
grocery_list.add_item("Bread")

# Display the initial list
grocery_list.display_list()

# Modify an item in the list
grocery_list.modify_item("Milk", "Almond Milk")

# Display the list after modification
grocery_list.display_list()

# Remove an item from the list
grocery_list.remove_item("Bread")

# Display the list after removal
grocery_list.display_list()
