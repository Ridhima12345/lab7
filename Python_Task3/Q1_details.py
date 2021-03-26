#Function to return Name

def funcName(firstName,lastName):
    fullName = firstName + " " + lastName
    return fullName

#Function to return Total Marks

def funcMarks(noSub):
    marks = []
    print("Enter marks of subject:")
    for i in range(0,noSub):
        score = int(input())
        marks.append(score)    
    totalMarks = sum(marks)
    return totalMarks

#Function to return Percentage

def funcPer(totalMarks):
    percentage = (totalMarks/5)
    return percentage

#Function to return Grade

def funcGrade(percentage):
    if(percentage>=95):
        return "A"
    if(percentage>=85 and percentage<=95):
        return "B"
    if(percentage>=75 and percentage<=85):
        return "C"
    if(percentage>=65 and percentage<=75):
        return "D"

#Function to print 

def funcprint(tMarks,percentage,grade):
    print("Total marks:",tMarks)
    print("Percentage:",percentage)
    print("Grade:",grade)

#Input and function calling

fName = input("Enter your first name")
lName = input("Enter your last name")
noSub = int(input("Enter total subjects"))
tMarks = funcMarks(noSub)
percentage = funcPer(tMarks)
grade = funcGrade(percentage)
print("Name:",funcName(fName,lName))
funcprint(tMarks,percentage,grade)


    
    
    
    
