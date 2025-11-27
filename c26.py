#list comperhension
# chapter 26


# mylist=[1,2,4,6,7,8]
# doublednumber=[]
# for num in mylist:
#     doublednumber.append(num*2)
# print(mylist)
# print(doublednumber)



# mylist=[1,2,4,6,7,8]
# doublednumber=[num*2 for num in mylist]
# print(mylist)
# print(doublednumber)





# myname="AboLfazl"
# charlist=[char.lower() for char in myname]
# print(charlist)



# myname="abolfazl"
# charlist=[char.upper() for char in myname]
# print(charlist)



mylist=[1,2,4,6,7,8,9]
even=[num for num in mylist if num%2==0]
odd=[num for num in mylist if num%2!=0]
print(even)
print(odd)
newlist=[num*2 for num in mylist]
print(newlist)




mylist=[1,2,4,6,7,8,9]
even=[num for num in mylist if num%2==0]
odd=[num for num in mylist if num%2!=0]
print(even)
print(odd)
newlist=[num*2  if num %2 == 0 else num *3 for num in mylist]
print(newlist)
