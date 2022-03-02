from datetime import date
Year = input("Enter the year you were born on: ")
Age = date.today().year - int(Year)
print("You are " + str(Age) + " years old.")
