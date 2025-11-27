# dictionary
#  chapter 28


# mynumber=[1,2,5,6,9,3]
# name=["ali", 'naghi','taghi']
# test=["hasan",True, 6 ,[1,2,3]]

# # ساختار دیکشنری
# shoppingcart=[{"name":"hasan","price": "free"},
#               {"name":"abolfazl","price": 4000}]


# dictionary=dict(name="new dictionary ", age=25)

# print(dictionary)
# print(dictionary["name"])
print("------------------")


# me={ 
#     "name":"abolfazl",
#     "family":"zekriyaei",
#     "age":27
# }
# print(me["name"])
# print(me["family"])
# print(me["age"])

print("------------------")


me={ 
    "name":"abolfazl",
    "family":"zekriyaei",
    "age":27
}

print(me.keys())
print(me.values())

for key in me.keys():
    print(key)


for value in me.values():
    print(value)

for key in me.keys():
    print(me[key])


for item in me.items():
    print(item)


for key, value in me.items():
    print(key, value)
