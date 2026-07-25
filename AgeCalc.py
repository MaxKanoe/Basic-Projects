import datetime

current_year = datetime.datetime.now().year

def get_username():
    username = input("Enter your name: ")
    confirmation = input("Your name is " + username + " Correct? y/n:")
    confirmation = confirmation.lower()

    if confirmation == "yes" or confirmation == "y":
        return username
    elif confirmation == "no" or confirmation == "n":
        get_username()

def get_age():
    age = int(input("Enter your age: "))
    if age > 0 and age < 100:
        confirmation = input("Your name is " + str(age) + " Correct? y/n:")
        confirmation = confirmation.lower()

        if confirmation == "yes" or confirmation == "y":
            return age
        elif confirmation == "no" or confirmation == "n":
            get_age()
    else:
        get_age()

name = get_username()
age = get_age()
oneHundredthBirthday = ( current_year - age ) + 100

print(str(name) + ", The current year is " + str(current_year) + " and the year you turn 100 is " + str(oneHundredthBirthday))
