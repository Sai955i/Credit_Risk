Year = int (input("Enter a year: "))
# Check if the year is a leap year or not   
if (Year % 4 == 0 and Year % 100 != 0) or (Year % 400 == 0):
    print(Year, "is a leap year")
else:   
    print(Year, "is not a leap year")
# This code checks if a year is a leap year or not.