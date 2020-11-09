#Combining Lists
list1= [13,20,40,90,11,60]
list2= [12,5,9,5,81,6]
#new list should contain only odd numbers from the first list and even numbers from the second list.
newList = []
for num in list1:
    if(num % 2 != 0):
        newList.append(num)
for num in list2:
    if(num % 2 == 0):
        newList.append(num)
print("new List")
print(newList)