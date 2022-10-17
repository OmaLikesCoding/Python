# exercise-06 What's the  Season?

# Write the code that:
# 1. Prompts the user to enter the month (as three characters):
#      Enter the month of the season (Jan - Dec):
# 2. Then promptshtt the user to enter the day of the month:
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

"""
Seasonal Calc.
"""

month = input("Let's see what the season is enter your month of choice:  ")
day = input("Now, enter the day (nums only please and thank you): ")

if month in ('January', 'February', 'March'):
	season = 'winter🥶'
elif month in ('April', 'May', 'June'):
	season = 'spring🌼'
elif month in ('July', 'August', 'September'):
	season = 'summer☀️'
elif month in ('October', 'November'):
    season= 'autumn🍁'
else:
	season = 'spring🌼'
if (month == 'March') and (day > 19):
	season = 'spring🌼'
elif (month == 'June') and (day > 20):
	season = 'summer☀️'
elif (month == 'September') and (day > 21):
	season = 'autumn🍁'
elif (month == 'December') and (day > 20):
	season = 'winter🥶'

print(f"By entering the month of {month}, and the day of {day}. We have calculated the season is {season} !")
