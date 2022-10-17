# exercise-04 What kind of Triangle?

# Write the code that:
# 1. Prompts the user to enter the three lengths of a triangle (one at a time):
#      Enter the lengths of three side of a triangle:
#      a:
#      b:
#      c:
# 2. Write the code that determines if the triangle is:
#      equalateral - all three sides are equal in length
#      scalene - all three sides are unequal in length
#      isosceles - two sides are the same length
# 3. Print a message such as:
#      - A triangle with sides of <a>, <b> & <c> is a <type of triangle> triangle
"""
I chose the float method so I can utilize decimals. 
"""
print("Let's see what type of triagngle we can create! Enter in a length for each side. Decimals are welcome😁: ")

side_1 = float(input('side one: '))
side_2 = float(input('side two: '))
side_3 = float(input('side three: '))
if side_1 == side_2 and side_1 == side_3:
    type = 'equalateral'
elif side_1 != side_2 and side_1 != side_3 and side_3 != side_2:
    type = 'scalene'
elif side_1 == side_2 or side_1 == side_3 or side_2 == side_3:
    type = 'isosceles'
print(f'A triangle with sides of {side_1}, {side_2} & {side_3} is a {type} triangle')