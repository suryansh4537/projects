dishPrice=100
dishesPrices=100,200,350,500,120
anotherdishesPrices=(100,"string",2.3)

print(dishPrice,hex(id(dishPrice)),type(dishPrice))

print(dishesPrices[0],hex(id(dishesPrices[0])))
print(anotherdishesPrices[0])
print(anotherdishesPrices[1])
print()

ages1=(1,2,3,4,5)#tuple(immutable) can not add change data
ages2=[1,2,3,4,5]#list can add ,change and remove data  MUTABLE
ages3={1,2,3,4,5}#set UNIQUENESS (IF SAME VALUE OCCURS MAORE THAN ONCE OUTPUT WILL SHOW IT ONLY ONES (EACH ELEMENT ONLY ONCE AND UNIQUE))

print(ages1,hex(id(ages1)),type(ages1))
print(ages2,hex(id(ages2)),type(ages2))
print(ages3,hex(id(ages3)),type(ages3))