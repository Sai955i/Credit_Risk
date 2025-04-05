a, b, c = map(int, input("enter value a,b,c with comma : ").split(","))

# a,b,c = 10,20,3

# Check if the number is positive, negative, or zero
if a > b and a > c:
    print("A is greater")
elif b > a and b > c:
    print("B is greater")
elif c > a and c > b:
    print("C is greater")
elif a == b and a == c:     
    print("A is equal to B and C")
elif a == b and a > c:
    print("A and B are equal and greater than C")
elif a == c and a > b:
    print("A and C are equal and greater than B")
elif b == c and b > a:
    print("B and C are equal and greater than A")
else:
    print("None of the numbers are equal")

# This code checks if a number is positive, negative, or zero.
# It takes three numbers as input and compares them to determine which one is the largest.