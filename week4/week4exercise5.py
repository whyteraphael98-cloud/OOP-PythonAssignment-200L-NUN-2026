
fruits = ["popo", "watermelon", "agbalumo", "grape", "orange"]


votes = {fruit: 0 for fruit in fruits}


print("Available fruits to vote for:", ", ".join(fruit.capitalize() for fruit in fruits))
print("Type 'done' to finish voting.")


while True:
    vote = input("Enter your vote (fruit name): ").strip().lower()
    if vote == 'done':
        break
    if vote in votes:
        votes[vote] += 1
        print("Vote recorded for", vote.capitalize())
    else:
        print("Invalid choice. Please choose from the available fruits.")


print("\nVoting Results:")
for fruit, count in votes.items():
    print(f"{fruit.capitalize()}: {count} votes")
