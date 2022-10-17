# exercise-01 Vowel or Consonant

# Write the code that:
# 1. Prompts the user to enter a letter in the alphabet:
#      Please enter a letter from the alphabet (a-z or A-Z):
# 2. Write the code that determines whether the letter entered is a vowel
# 3. Print one of following messages (substituting the letter for x):
#      - The letter x is a vowel
#      - The letter x is a consonant

# Hints:  Use the in operator to check if a character is in another string
#         For example, if some_char in 'abc':

#Attempt= 1 {Did not work LOL, after typing some of the variables it became confusing to me LOL}
# vltr= ['a', 'e', 'i', 'o', 'u']
# consonant= ['y']
# input =("Please enter a letter from a-z, please:").lower()
# if input in vltr:
#   print(f'the character {vltr} is a vowel')
# else:
#   print(f'the character {consonant} is a consonant')
"""
This process uses the == operator and or. It was easier for me to understand this way
"""
#Attempt 2: {Works and I added the funny LOL, and managed to use less characters}
vltr = input ("Please enter a letter from a-z, please. I promise I'll be nice😌 :")
if (vltr=='a' or vltr=='e' or vltr=='i' or vltr=='o' or vltr=='u'):
    print(vltr, "You entered in a vowel that's Dope son! 😎")
else: 
    print(vltr, "You entered some random consonant, bro😩")

#logic == compares the value or equality of two objects. It was the easiest for me to understand at the time. 
