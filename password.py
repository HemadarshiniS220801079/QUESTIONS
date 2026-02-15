correct_password = "admin123"

for i in range(3):
    entered = input("Enter password: ")
    
    if entered == correct_password:
        print("Unlocked")
        break
else:
    print("Locked")
