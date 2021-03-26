#function for calculating total marks and percentage
def cal(maths,english,social,hindi,science):
    total_Marks = english+social+maths+hindi+science
    percentage = float((total_Marks/500)*100)      #percentage in float

    print("The total marks are: ",total_Marks)
    print("The percentage is: ",percentage)

fname = "Ridhima "
bname = "Goyal"
cname = "DIT University "
address = "Dehradun"
maths = 94
english = 86
social = 98
hindi = 98
science = 91
print("NAME: ",fname+bname)     #full_name
print("COLLEGE NAME & ADDRESS: ",cname+address) #college name & address
cal(maths,english,social,hindi,science)         #function call
