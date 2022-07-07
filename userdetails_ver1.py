# ================================ USER DETAILS ================================
# ================================== VERSION 1 =================================
# Ask the user details (name, age, year level)
# Check if they are eligible to take the quiz

#Print a welcome statement
print("Welcome to Chemistry Quiz!")
print("Let's start by answering a few questions!")

#Ask the user to input their name
while True:
    name = input("What is your name? ")

    #Check if the name is valid
    if name.isalpha() == True:
        print("Continue")
        break
    else:
        print("This name is unvalid. Please try again.")
        continue

#Ask the user to input their age
while True:
    try:
        age = int(input("How old is you? "))
    except ValueError:
        print("This age is invalid. Please try again.")
        continue
    
    if age >= 12 and age <=18:
        print("Continue")
        break
    else:
        print("This age is unvalid. Please try again.")
        continue

#Ask the user to input their year level
while True:
    try:
        year_level = int(input("What year level are you in now? "))
    except ValueError:
        print("The one that you entered is invalid. Please try again.")
        continue

    if year_level >= 9 and year_level <= 13:
        print("Continue")
        break
    else:
        print("The one that you entered is invalid. Please try again.")

        


