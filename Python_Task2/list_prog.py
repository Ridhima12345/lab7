list = []
print("Enter the marks of different subjects you stored in 12th\n")
for i in range(0,5):
    marks = int(input())

    #append() adds the elements to the existing/new list

    list.append(marks)
print(list)

marks1 = int(input("Enter the marks of 6th subject\n"))

#insert() inserts element at a specific position[+1 posn from the index given]

list.insert(2,marks1)
print(list)

list2 = ["Maths","Chem","Social","English","Hindi","GK"]

#extend() add contents of the later list to the previous one

list.extend(list2)
print("Extended list\n",list)

marks = [90,45,56,87,12,82]

#sum() calculates sum of all the elements

print("Total marks are:")
print(sum(marks))

#length() calculates total length of the list

print("Length of the list:")
print(len(list2))

#min() calculates minimum of all the elements

print("The minimum marks you scored are:")
print(min(marks))

#max() calculates the maximum of all elements

print("The maximum marks you scored are:")
print(max(marks))
