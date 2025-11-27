# list
# chapter 21


# mynumber = [1,2,3,4,5]
# print(mynumber[0])
# print(mynumber[1])
# print(mynumber[2])
# print(mynumber[3])
# print(mynumber[4])



mycolor=["red, blue , green, pink",4.5]
for color in mycolor:
    if type(color)==str:
        print(f'color is :{color}' )
    else:
        print(f"{color} is not color")
print("----------------")


index =0
while index < len(mycolor):
    color = mycolor[index]
    if type(color)==str:
        print(f'color is :{color}' )
    else:
        print(f"{color} is not color")
    index += 1