# exercise-03 Calculate Dog Years

# Write the code that:
# 1. Prompts the user to enter a dog's age in human years like this:
#      Input a dog's age in human years:
# 2. Calculates the equivalent dog years, where:
#      - The first two years count as 10 years each
#      - Any remaining years count as 7 years each
# 3. Prints the answer in the following format:
#      The dog's age in dog years is xx

# Hint:  Use the int() function to convert the string returned from input() into an integer
"""
At one human year a medium dog ages 15 years and the second 9 years(after that they age 5 years each year). So I did the calc to reflect every year after 1 to multiply by 5 and add 12. 
This age calc methodology was given by Dutch.com, they did not provide an actual calculation in terms of a numerical math problem.
But, they made reference to the dog ages in relation to human ages.
"""
huage = int(input("Hey there! Enter a dog's age in human years. Seeing that your're a human, this should be easy!"))
pupage= 0
if huage < 1:
    pupage += (huage ) + 15
else:
        pupage = huage * 5 + 12 
        print(f"Your dog's human age={pupage} 🐶  years! Wow. It really gives you something to think about.")

