'''
4. While Loop
Write a program that keeps asking the user to enter a password until they enter the correct one "python123".
'''

correct_password = "python123"

while True:
    password = input("Enter the password: ")
    if password == correct_password:
        print("Access granted.")
        break
    else:
        print("Incorrect password. Try again.")
