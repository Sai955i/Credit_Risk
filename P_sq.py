import math ;

num = int(input("Enter a number: "))
if math.sqrt(num) == math.floor(math.sqrt(num)):
    print("The number is a perfect square.")
else:
    print("The number is not a perfect square.")
# # The code checks if a number is a perfect square by comparing its square root to its floor value.
