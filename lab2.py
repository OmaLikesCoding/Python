# exercise-02 Length of Phrase

# Write the code that:
# 1. Prompts the user to enter a phrase:
#      Please enter a word or phrase:
# 2. Print the following message:
#      - What you entered is xx characters long
# 3. Return to step 1, unless the word 'quit' was entered.
"""
This process can be done with single words or full sentences.
"""

slangword= print("Let's play a game and see how well my bots can count. Shall we? 🤖")
while slangword != "quit":
    slangword= input("Please enter your favorite slang word or term so that my bots can count how man characters it has it: ")
    if slangword != "quit":
        characters = len(slangword)
        print(f"Our bots counted that your slang word or term has: {characters} characters in it! Type quit if you want to give our bots a break.")