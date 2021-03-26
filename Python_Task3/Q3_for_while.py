#for loop

print("For Loop")
for i in range(1,11):
    if(i == 3 or i == 7):
        continue
    else:
        print(i)

#while loop

print("While Loop")
i = 1
while(i<=10):
    if(i==3 or i==7):
        i = i + 1
    else:
        print(i)
        i = i+1
