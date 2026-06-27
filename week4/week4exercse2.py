
names = []
scores = []


def get_grade(score):
    if score >= 70:
        return 'A'
    elif score >= 60:
        return 'B'
    elif score >= 50:
        return 'C'
    else:
        return 'F'


while True:
    name = input("Enter student name or 'done' to finish: ").strip()
    if name.lower() == 'done':
        break
    try:
        score = float(input(f"Enter score for {name}: "))
        names.append(name)
        scores.append(score)
    except ValueError:
        print("Invalid score. Please enter a number.")


if not scores:
    print("No students entered.")
else:
    
    average = sum(scores) / len(scores)
    
    
    max_score = max(scores)
    min_score = min(scores)
    
    
    print("\nGrade Report:")
    print("-" * 40)
    for i, (name, score) in enumerate(zip(names, scores), 1):
        grade = get_grade(score)
        marker = ""
        if score == max_score:
            marker = " (Highest)"
        elif score == min_score:
            marker = " (Lowest)"
        print(f"{i}. {name}: {score:.1f} - {grade}{marker}")
    print("-" * 40)
    print(f"Class Average: {average:.2f}")
    
    
    with open('grade_book.txt', 'w') as f:
        f.write("Grade Report:\n")
        f.write("-" * 40 + "\n")
        for name, score in zip(names, scores):
            grade = get_grade(score)
            f.write(f"{name}: {score:.1f} - {grade}\n")
        f.write("-" * 40 + "\n")
        f.write(f"Class Average: {average:.2f}\n")
    
    print("\nReport saved to grade_book.txt")
