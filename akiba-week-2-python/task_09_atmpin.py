correct_pin="1234"
for i in range(3):
    user_pin=input("Enter your 4-digit PIN: ")
    if user_pin==correct_pin:
        print("Access granted.")
        break
    else:
        print("Incorrect PIN. Try again.")
print("Access denied. You have exceeded the maximum number of attempts.")