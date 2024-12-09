'''
list1 = []
x = 5
f = open("/Users/edenlittlefair/Downloads/adventofcode/day1/puzzle1.txt", "r")

#print(f.read())
for line in f:
    list1.extend(list(line[:x]))

print(list1)
'''

sum = 0
list1 = []
list2 = []
x = 5
y = 13

with open("/Users/edenlittlefair/Downloads/adventofcode/day1/puzzle1.txt", "r") as f:
    for line in f:
        list1.append(line[:x])  # Add the first `x` characters as a single string :)
        list2.append(line[8:y]) # from 8 --> 13, getting rid of spaces 6 --> 8

list1 = [int(num) for num in list1] #convert list to integer values to be operated on
list2 = [int(num) for num in list2]

list1.sort() #numerical sort
list2.sort()

for i in range (1000): #1000 lines in file
    sum = sum + abs(list2[i]-list1[i]) #absolute function to find distance between two values

print(sum)