def get_count():
    """Get valid count (1-10) from user."""
    while True:
        try:
            count = int(input("How many items (1-10)? "))
            if 1 <= count <= 10:
                return count
            else:
                print("Please enter a number between 1 and 10")
        except ValueError:
            print("Please enter a valid integer")

def get_item(prompt="Enter item: "):
    """Get valid item name from user."""
    return input(prompt).strip()

def remove_duplicates(shopping_list):
    """Remove duplicates and return unique list."""
    return list(set(shopping_list))

def main():
    """Run complete shopping list duplicate remover."""
    print("=== Shopping List Duplicate Remover ===")
    
    count = get_count()
    shopping_list = []
    
    # Get all items
    for i in range(count):
        item = get_item(f"Enter item {i+1}: ")
        shopping_list.append(item)
    
    # Remove duplicates
    unique_items = remove_duplicates(shopping_list)
    
    # Calculate duplicates removed
    duplicates_removed = len(shopping_list) - len(unique_items)
    
    print(f"\nOriginal: {shopping_list}")
    print(f"Unique items: {', '.join(unique_items)} ({len(unique_items)} total)")
    if duplicates_removed > 0:
        print(f"Removed {duplicates_removed} duplicate(s)!")

if __name__ == "__main__":
    main()
