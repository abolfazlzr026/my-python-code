# dictionary
# chapter 29
# me={
#     "name":"abolfazl",
#     "family":"zekriyai",
#     "age":27
# }

# print(me["name"])

# isexist= "email" in me
# is2="family" in me
# print(isexist)
# print(is2)


# if "email" in me:
#     print(me["email"])
# else:
#     print("there is no email key in me")


#     isne="abolfazl "in me
#     print(isne)

#     isne="abolfazl"in me.values()
#     print(isne)


# fromkeys


# me={
#     "name":"abolfazl",
#     "family":"zekriyai",
#     "age":27
# }

# print(me)
# me.clear()
# print(me)


# copyme=me.copy()
# print(me)
# print(copyme)
# print(me == copyme)
# print(me is copyme)


# new= {"name":"unknown", "family":"unknown"}
# new2= {}.fromkeys("name", "unknown")
# print(new2)


# new= {"name":"unknown", "family":"unknown"}
# new2= {}.fromkeys(["name"], "unknown")
# print(new2)


# new= {"name":"unknown", "family":"unknown"}
# new2= dict.fromkeys(["name"], "unknown")
# print(new2)



#get

me={
    "name":"abolfazl",
    "family":"zekriyai",
    "age":27
}
print(me.get("name"))
# print(me["phone"])
print(me.get("phone"))

isphone=me.get("phone")
print(isphone is None) 
# if "phone" in me:
#     print("is there")
