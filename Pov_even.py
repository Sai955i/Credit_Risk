num = int(input("Enter a number: "))

if num % 2 == 0 and num > 0:
    print("Even and Positive")
elif num % 2 == 0 and num < 0:
    print("Even and Negative")  
elif num % 2 != 0 and num > 0:
    print("Odd and Positive")
elif num % 2 != 0 and num < 0:
    print("Odd and Negative")
else:
    print("Zero")
# This code checks if a number is even or odd and positive or negative.