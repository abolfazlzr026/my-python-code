# 1 2 3
# 2 4 6
# 3 6 9
#
# 1
# 2
# 3
# 2
# 4
# 6
# 3
# 6
# 9
# listofnumbers=range(1,4)
# for i in listofnumbers: 
#    print(i*1)
# for i in listofnumbers: 
#    print(i*2)
# for i in listofnumbers: 
#    print(i*3)

# listofnumbers=range(1,4)
# for i in range(1,4):
#  i=i*1, i*2, i*3
#  print(i)
 
# listofnumbers=range(1,10)
# for i in listofnumbers:
#     for j in listofnumbers:
#         print(f'{i*j:2d}',end=" ")
#     print("")


a=[1,2,3,4,5]
b = [1,4]
for number in a:
    for i in b:
        print(number*i)




x=int(input("enter your number: "))
isprime=True
if x<=1:
    isprime=False
for i in range(2,x):
     if x % i==0:
        isprime=False
if isprime :
    print("adad aval")
else:
    print("adad aval nist")    




text = "hello"
reversed_text = text[::-1]
print(reversed_text)



