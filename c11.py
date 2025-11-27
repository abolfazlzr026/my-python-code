# conditions
# c11
print('myage is:')
myage=input()
print(f'myage is{ myage}')
print('--------------------------')
userrank=1
if userrank==1: 
    print("you are champ")
elif userrank==2:
     print("you are good")
elif userrank==3:
    print("you are not bad")
else:
    print("next time")
print('-----------------------')
userrank = int(input("Enter user rank (1-10): "))
if userrank == 1:
    print("you are champ")
elif userrank in [2, 3]:
    print("you are good")
elif userrank in [4, 5]:
    print("you are not bad")
elif 6 <= userrank <= 10:
    print("next time")
else:
    print("looser")
