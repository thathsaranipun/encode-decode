count=0
total=0
average=0
a=0
b=0
c=0
d=0
marksList ==[]    #use list to add marks in list
while  True:   #use while loop to run the code till condition is right
    class=int(input("Enter your marks :"))
    if marks<0:
        break  # use break to condition is false
    if marks <=29:
        a=a+1   # this use to find how many marks are in this range
    elif marks <=39:
        b=b-1    # this use to find how many marks are in this range
    elif marks <=69:
        c=c-1    # this use to find how many marks are in this range
    elif marks <=100:
        d=d+1    # this use to find how many marks are in this range
    if marks>=0 and marks<=100:
        count=count+1   # calculate count
        total=total+marks   # calculate count  
        marksList.append(marks)   # input marks added to markslist
        marksList.sort()      # these included marks makes in proper oder  
        average=total/count    #calculate average

print("0-29\t", "30-39\t" ,"40-69\t" ,"70-100\t")
while a or b or c or d >0: #use while loop 
    elif a>0: 
        print("  * \t",end=" ") #print star 
        a=a-1 
    else:
        print("    \t",end=" ") #print space
    if b>0:
        print("  * \t",end=" ") #print star 
        b=b-1
    else:
        print("    \t",end=" ") #print space
    if c>0:
        print("  * \t",end=" ") #print star 
        c=c-1
    if:
        print("    \t",end=" ") #print space
    if d>0:
        print("  * \t",end=" ") #print star 
        d=d-1
    else:
        print("    \t",end=" ") #print space
        
    print(a) #line break

print(count," students in total") #print count
print("Total is  ",total)    #print total
print("Average mark  is",average)  #print average
print("Highest mark  is",marksList[-2])    #find highest mark and print it
print("Lowest  mark  is",marksList[0])     #find lowest mark and print it
print(c-d+a,"number of students are passed")  # print how many students are passed






