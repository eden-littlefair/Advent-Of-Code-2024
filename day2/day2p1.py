list1 = []
sum = 0

with open("/Users/edenlittlefair/Downloads/adventofcode/day2/puzzle2.txt", "r") as f:
    for line in f:
        number = [int(num) for num in line.split()]
        list1.append(number)

print(list1[0])


for i in range(0,1000):

    if list1[i][0] < list1[i][1]:
        total = 0
        for j in range(0, len(list1[i])-1):
            if list1[i][j] < list1[i][j+1]:
                if list1[i][j+1] - list1[i][j] <= 3 and list1[i][j+1] - list1[i][j] >= 1:
                    total += 1
                    if total == len(list1[i])-1:
                        sum += 1

    else:
        total = 0
        for j in range(0, len(list1[i])-1):
            if list1[i][j] > list1[i][j+1]:
                if list1[i][j] - list1[i][j+1] <= 3 and list1[i][j] - list1[i][j+1] >= 1:
                    total += 1
                    if total == len(list1[i])-1:
                        sum += 1


           
print(total)
print(sum)