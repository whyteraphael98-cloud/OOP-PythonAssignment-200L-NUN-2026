n = int(input("Enter a positive integer: "))
if n <= 0:
    print("Please enter a positive integer.")
else:
    for i in range(1, n + 1):
        row = ""
        for j in range(1, i + 1):
            row += str(j)
        print(row.ljust(n))
