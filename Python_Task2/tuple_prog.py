#Initializing the tuple

animals = ("lion","wolf","goose","wolf","lama","wolf",56,23,67)

#index() returns the first index at which value occurs

print("The first time wolf occurs in the tuple at posn:-")
print(animals.index("wolf"))

#len() returns the length of the tuple

print(len(animals))

#count() returns the no of times value is repeated

print("The no of times wolf accurs in the tuple:-")
print(animals.count("wolf"))

#Initializing another tuple

friends = ("Joey","Rachel","Ross","Barney")

#enumerate() returns a tuple containing a count for every iteration and the values obtained from iterating over a sequence

for index,friend in enumerate(friends):
    print(index,friend)

#Initialize another tuple

tuple3 = (85,56,48,99,42)

#min() finds the minimum element

print("The minimum value:- ",min(tuple3))

#max() finds the minimum element

print("The maximum value:- ",max(tuple3))

#del() deletes the whole tuple

del(tuple3)
print(tuple3)


    
