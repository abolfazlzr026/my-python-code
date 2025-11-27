# chapter 12
# number = 2
# if type (number) == 1:
#     print("this is true")
# else:
#     print("this is false")
print("----------------------")
number = 8.2
if type (number) is int:
    print("this is true")
else:
    print("this is false")
print('---------------------')    
# difference between is and ==
list_1= [1,2,3]
list_2= list_1
list_3= list(list_1)
print(list_1)
print(list_2)
print(list_3)
print('--------------------')
print(list_1 == list_2)
print(list_1 == list_3)
print("---------------------")
print(list_1 is list_2)
print(list_1 is list_3)

# the == operator -> values are equal
# the is operator -> point to the same object
if "kjfdjed":
    print("this is true")
else:
    print("this is false")
print("---------------------")
print("enter your favorite colore")
colore= input()
# print(f"your favorite colore is {colore}") 
# # or
if colore:
    print(f"your favorite colore is {colore}")