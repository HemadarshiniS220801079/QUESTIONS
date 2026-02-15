def password_check(correct_password, max_attempts=3):
    
    attempts = 0
    
    while attempts < max_attempts:
        entered = input("Enter password: ")
        
        if entered == correct_password:
            print("Access Granted")
            return
        
        attempts += 1
        print("Incorrect password")
    
    print("Access Denied")


if __name__ == "__main__":
    correct_password = "secure123"   # change this as needed
    password_check(correct_password)
