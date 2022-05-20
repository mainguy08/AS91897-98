#Print a welcome statement
print("Welcome to TODO!")
print("Let's start by answering a few questions!")

while True:
    #Ask the user to input their name
    name = input("What is your name? ")

    #Check if the name is valid
    if name.isalpha() == True:
        print("Continue")
        break
    else:
        print("This name is unvalid.")
        continue

while True:
    try:
        age = int(input("How old is you? "))
    except ValueError:
        print("This name is invalid.")
        continue
    
    if age >= 12:
        print("Continue")
        break
    else:
        print("This name is unvalid.")
        continue



