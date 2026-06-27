recipe = []
while True:
    ingredient = input("Enter ingredient or 'done': ").strip()
    if ingredient.lower() == 'done':
        break
    quantity = input(f"Enter quantity for {ingredient}: ").strip()
    recipe.append((ingredient, quantity))
print("Recipe Card")
print("-" * 20)
for ing, qty in recipe:
    print(f"{ing}: {qty}")
