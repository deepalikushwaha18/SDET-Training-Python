
# Write a program that asks the user to enter their name and their age.


name=input("Enter your Name")
age=int(input("Enter your age"))

# Print out a message addressed to them that tells them the year that they will turn 100 years old.
year=str((2020-age)+100)
print(name+"  will be turned 100 years in "+year)