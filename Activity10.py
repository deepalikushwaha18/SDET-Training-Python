#Tuple Number Checker 
#Given a tuple of numbers, iterate through it and print only those numbers which are divisible by 5
#tuple = (10,20,31,81,60)
values = input("Enter comma seprated values")
list = values.split(",")
tuple = tuple(list)
print('List : ',list)
print('Tuple : ',tuple)
for num in tuple:
    num1 = int(num)
    if(num1 % 5 == 0):
        print(num)
