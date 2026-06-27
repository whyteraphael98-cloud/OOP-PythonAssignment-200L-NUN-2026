correct_password = "breadandegg"
max_attempts = 3
attempts = 0

while attempts < max_attempts:
    password = input("Enter password: ")
    attempts += 1
    if password == correct_password:
        print("Access Granted.")
        break
    if attempts < max_attempts:
        print("Incorrect password. Try again.")
else:
    print("Access Denied.")
