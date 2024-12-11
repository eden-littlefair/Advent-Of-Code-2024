list1 = []
sublists = []
sum = 0
sum2 = 0
sum3 = 0
counter = 0

with open("/Users/edenlittlefair/Downloads/adventofcode/day2/puzzle2.txt", "r") as f:
    for line in f:
        number = [int(num) for num in line.split()]       #2d array creation
        list1.append(number)

print(list1[0])


for i in range(0,1000):  #initialise loop through 1000 lines

    newlist = list1[i]
    print("")
    #counter += 1
    #print("sublist increasing:")
    #print(newlist)
    for k in range(len(newlist)):   
               
        sublist = newlist[:k] + newlist[k+1:]
        total2 = 0
        total3 = 0
        print("current sublist:", sublist)
                                   
        for l in range(len(sublist)-1):
            if sublist[l] < sublist[l+1] and sublist[l+1] - sublist[l] <=3 and sublist[l+1] - sublist[l] >= 1:
                total2 += 1
            elif sublist[l+1] < sublist[l] and sublist[l] - sublist[l+1] <=3 and sublist[l] - sublist[l+1] >= 1:
                total3 += 1
            else:
                break
                
        if total2 == len(sublist)-1 or total3 == len(sublist)-1:
            #print(sublist)
            sum2 += 1 
            counter += 1 
            print(sum2) 
            break
  

            

    ''''           
    else:
        total = 0
        for j in range(0, len(list1[i])-1):
            if list1[i][j] > list1[i][j+1]:
                if list1[i][j] - list1[i][j+1] <= 3 and list1[i][j] - list1[i][j+1] >= 1:
                    total += 1
        if total == len(list1[i])-1:
            sum += 1


#sublist 1

        elif total == len(list1[i])-2:
            newlist1 = list1[i]
            #print(newlist1)
            #print(newlist1)
            print("sublist decreasing:")
            for m in range (len(newlist1)):
                           

                sublist1 = newlist1[:m] + newlist1[m+1:]
                total3 = 0
                
                print(sublist1)

                for n in range(len(sublist1)-1):
                   
                    if sublist1[n] > sublist1[n+1]:
                        if sublist1[n] - sublist1[n+1] <=3 and sublist1[n] - sublist1[n+1] >= 1:
                            total3 += 1


                if total3 == len(sublist1)-1:
                    sum3 += 1
                    print(sum3)

                    break
                
        else:
            print("")
                
'''                            


'''
#print("counter (ignore):",(total))
print(sum)
print(sum2)
print(sum3)

print(sum+sum2+sum3)
'''