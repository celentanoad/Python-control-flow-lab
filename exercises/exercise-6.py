# exercise-06 What's the  Season?

# Write the code that:
# 1. Prompts the user to enter the month (as three characters):
#      Enter the month of the season (Jan - Dec):
# 2. Then propts the user to enter the day of the month: 
#      Enter the day of the month:
# 3. Calculate what season it is based upon this chart:
#      Dec 21 - Mar 19: Winter
#      Mar 20 - Jun 20: Spring
#      Jun 21 - Sep 21: Summer
#      Sep 22 - Dec 20: Fall
# 4. Print the result as follows:
#      <Mmm> <dd> is in <season> 

# Hints:
# Consider using the in operator to check if a string is in a particular list/tuple like this:
# if input_month in ('Jan', 'Feb', 'Mar'):
#
# After setting the likely season, you can use another if...elif...else statement to "adjust" if
# the day number falls within a certain range.

month = input("Enter a month (using 3 characters): ")
day = int(input("Enter the day of the month: "))
season = ""
if (month.lower() in "dec, feb, mar"):
    if (month == "dec" and day < 21):
        season = "Fall"
    elif (month == "mar" and day >19):
        season = "Spring"
    else:
        season = "Winter"
elif (month.lower() in "apr, jun"):
    if (month == "jun" and day > 20):
        season = "Summer"
    else:
        season = "Spring"
elif (month.lower() in "jul, aug, sep"):
    if (month == "sep" and day > 21):
        season = "Fall"
    else:
        season = "Summer"
else:
    season = "Winter"
print(month, " ", day, "is in ", season)
