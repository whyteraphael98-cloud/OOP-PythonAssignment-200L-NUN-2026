import datetime

expenses = {}  
log = []  


while True:
    category = input("Enter expense category or 'done' to finish: ").strip()
    if category.lower() == 'done':
        break
    try:
        amount = float(input(f"Enter amount for {category}: "))
        if amount <= 0:
            raise ValueError("Amount must be positive.")
    except ValueError as e:
        print(f"Invalid input: {e}. Please try again.")
        continue
    
    
    if category not in expenses:
        expenses[category] = 0
    expenses[category] += amount
    
    
    running_total = expenses[category]
    log.append(f"{category} | {amount:.2f} | {running_total:.2f}")


if not expenses:
    print("No expenses entered.")
else:
    print("\nExpense Summary:")
    print("-" * 30)
    for category, total in expenses.items():
        print(f"{category:<15} {total:>10.2f}")
    print("-" * 30)
    grand_total = sum(expenses.values())
    print(f"Grand Total: {grand_total:>10.2f}")
    category
    max_category = max(expenses, key=expenses.get)
    print(f"Highest spending category: {max_category} ({expenses[max_category]:.2f})")
    
    
    with open('expenses.txt', 'a') as f:
        for entry in log:
            f.write(entry + '\n')
    
    print("\nSession log appended to expenses.txt")
