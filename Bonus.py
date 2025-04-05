Year_of_service = int(input("Enter the year of service: "))
Performance_rating = int(input("Enter the performance rating (1-5): "))
if Year_of_service > 5 and Performance_rating >= 4:
    bonus = 0.1 * Year_of_service * 10000   # Assuming a base salary of 10000
    print("The bonus is:", bonus)
elif Year_of_service > 5 and Performance_rating < 4:
    bonus = 0.05 * Year_of_service * 10000
    print("The bonus is:", bonus)
elif Year_of_service <= 5 and Performance_rating >= 4:
    bonus = 0.07 * Year_of_service * 10000
    print("The bonus is:", bonus)
else:
    bonus = 0.03 * Year_of_service * 10000
    print("The bonus is:", bonus)
# The code calculates the bonus based on years of service and performance rating.
# It uses nested if-else statements to determine the bonus percentage based on the conditions.
