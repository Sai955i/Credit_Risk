a1,a2,a3 = map(float, input("Enter the a1,a2,a3 angles (comma) : ").split(','))  
if a1+a2+a3 == 180 and a1 > 0 and a2 > 0 and a3 > 0:
    print("yes it is a valid triangle")
else:
    print("no it is not a valid triangle")
# The code checks if the angles of a triangle are valid.       