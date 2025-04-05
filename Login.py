userid = input("Enter your user ID: ")
password = input("Enter your password: ")

# Check if the user ID and password are correct
if userid == "admin" and password == "password":
    print("Login successful!")  
else:
    print("Login failed. Please try again.")
# The code above is a simple login system that checks if the user ID and password are correct. If they are, it prints "Login successful!", otherwise it prints "Login failed. Please try again.".
# This code is a basic example of how to implement a login system in Python. It uses the input() function to get the user ID and password from the user, and then checks if they match the predefined values. If they do, it prints a success message, otherwise it prints a failure message.