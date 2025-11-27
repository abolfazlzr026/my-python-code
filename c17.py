# range() -> to create a list of numbers
# chpter 17
# mynumber=range(1,17)
# result=list(mynumber)
# print(mynumber)
# print(result)

# or
# print(list(range(1,10)))

for i in range(1,7):
    j = " "    
    for k in range(1, i+1):
      j += "*" 
    print(j)










# for i in range(1,15):
#     if i % 2 == 1:
#         for star in range(1,9):
#             print("*" * star)
#     else:
#         for star in range(8,0, -1):
#             print("*" * star)