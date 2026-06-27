
shopping_list = []


while True:
    item = input("Enter an item to add to the shopping list or 'done' to finish: ").strip()
    if item.lower() == 'done':
        break
    shopping_list.append(item)


if shopping_list:
    print("\nShopping List:")
    for i, item in enumerate(shopping_list, 1):
        print(f"{i}. {item}")
    
    
    with open('shopping_list.txt', 'w') as f:
        for item in shopping_list:
            f.write(item + '\n')
    
    print("\nList saved to shopping_list.txt")
else:
    print("No items added to the shopping list.")
