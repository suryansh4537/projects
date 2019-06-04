# ALL VARIABLES ARE REFERENCE VARIABLES AND POINT TO A CONTAINER HAVING THE VALUE
johnsAge=30
print(johnsAge,hex(id(johnsAge)))  #

davidAge=30                        # Same as johnsAge
print(davidAge,hex(id(davidAge)))           # Memory already contains 30 in a Container so both will use single 30

del johnsAge
print(davidAge,hex(id(davidAge)))
print()

#reference copy
davidAge=90
johnsAge=davidAge
print(davidAge,hex(id(davidAge)))
print(johnsAge,hex(id(johnsAge)))

zomato=40
print(zomato,hex(id(zomato)))

zomato=50                #id also changes with value
print(zomato,(hex(id(zomato))))