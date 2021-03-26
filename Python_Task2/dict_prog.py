#Initializing the dictionary

carModel = {
    "brand" : "Ford",
    "model" : "Mustang",
    "year"  : "1964"
    }
print(carModel)

#get() gives the value of the key

val = carModel.get("model")
print("\nModel of the car :-",val)

#values() returns value of a dictionary

print("\nDetails about the car :-")
for i in carModel.values():
    print(i)

#items() returns both key and the value

print("\nDetailed version :-")
for i,j in carModel.items():
    print(i,j)

#len() determines the no of items in dictionary

print("\nLength :-",len(carModel))

#pop() removes item from dictionary

carModel.pop("model")
print("\nUpdated :-\n",carModel)

#copy() copies one dictionary into another

newDict = carModel.copy()
print("\nNew dictionary :-\n",newDict)

#clear() empties the dictionary

newDict.clear()
print(newDict)
