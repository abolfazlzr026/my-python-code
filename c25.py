# list slicing -> to make a copy of a list
# chapter 25


# mylist=[2,4,6,8,10]
# number=mylist[1]
# mylist_2=mylist[1]
# print(number)



# mylist=[2,4,6,8,10,12,14,18]
# number=mylist[1]
# #sme_list[start:end:step]
# mylist_2=mylist[1:5:1] 
# print(mylist_2)






# mylist=[2,4,6,8,10,12,14,18]
# number=mylist[1]
# #sme_list[start:end:step]
# mylist_2=mylist[1:5:2] 
# print(mylist_2)




# mylist=[2,4,6,8,10,12,14,18]
# number=mylist[1]
# #sme_list[start:end:step]
# mylist_2=mylist[3:] 
# print(mylist_2)




# mylist=[2,4,6,8,10,12,14,18]
# number=mylist[1]
# #sme_list[start:end:step]
# mylist_2=mylist[-3:] 
# print(mylist_2)




# mylist=[2,4,6,8,10,12,14,18]
# number=mylist[1]
# #sme_list[start:end:step]
# mylist_2=mylist[-5:] 
# print(mylist_2)
# copyofmylist=mylist[0:]
# print(copyofmylist)





colors=["red","blue","pink","black"]
copyofcolors=colors[ : : -1]
colors.reverse()
print(colors)
print(copyofcolors)




myname="abolfazl"
print(myname[ : :-1])