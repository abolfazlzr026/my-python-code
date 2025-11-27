#dictionry
# chapter 30


#pop
# me={ 
#     "name":"abolfazl",
#     "family":"zekriyaei",
#     "age":27,
#     "email":"abolfazl@gmail.com"
# }
# print(me)
# me.pop("name")
# print(me)
# result=me.pop("family")
# print(result)
# me.popitem()
# me.popitem()
# print(me)


# update

me={ 
    "name":"abolfazl",
    "family":"zekriyaei",
    "email":"abolfazl@gmail.com"
}

second={
    "age":27,
    "name":"ali",}
print(second)
second.update(me)
print(second)
print("-----------------")

second["name"]= "hasan"
print(second)