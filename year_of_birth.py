def year_of_birth():
    name = input("Please enter your name")
    age = int(input("Please enter your age"))
    year = 2022 - age
    print(f"OMG ,{name} you are {age} years old so you were born in {year}")

year_of_birth()

def date_of_birth():
    full_name = input("Please enter your name")
    age = int(input("Please enter your age"))
    full_name = "Fatema Zahra"
    age = 25
    month = int(input("Please enter the month of birth as digit"))
    if month < 8:
        print("Birthday has passed")
    elif month > 8:
        print("Birthday yet to come")
    else:
        date = int(input("Please enter date of birth"))
        if date >= 2:
            print("Birthday has passed")
        else:
            print("Birthday yet to come")

date_of_birth()