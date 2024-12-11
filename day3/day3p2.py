import re
sum = 0
list1 = []
list2 = []
value = 0

with open("/Users/edenlittlefair/Downloads/adventofcode/day3/puzzle3.txt", "r") as f:
    lines = f.readlines()
#print(lines)
charString = ''.join(lines)
#print(charString)

#string mul( then integer 1-3 digits then string , t
pattern = r'mul\(\d{1,3}\,\d{1,3}\)'
truepattern = r'do\(\)'
falsepattern = r'don\'t\(\)'
numPattern = r'\d{1,3}'

patterns = [pattern, truepattern, falsepattern]
combined_pattern = '|'.join(patterns)
print(combined_pattern)


matches = re.finditer(combined_pattern, charString)

result = [match.group() for match in matches]
print(result)

currentstate = True

for i in range(len(result)):
    if result[i] == "don't()":
        currentstate = False
    elif result[i] == "do()":
        currentstate = True
    else:
        currentstate = currentstate
    list1.append(currentstate)
print(list1)

for j in range(len(result)):
    if list1[j] == True and re.fullmatch(pattern, result[j]):
        print(result[j])   #printing functions that should be applied
        list2.append(result[j])

print(list2)

list2String = ''.join(list2)  #converting from list to string
numbers = re.findall(numPattern, list2String)

numbersInt = [int(num) for num in numbers] #converting to integer list

for i in range(0,len(numbersInt)-1,2):
    value = (numbersInt[i] * numbersInt[i+1])
    print(value)
    #print(value)
    sum += value
print(sum)
    



#on = re.findall(truepattern, charString)
#off = re.findall(falsepattern, charString)

#print(matches)

#numPattern = r'\d{1,3}'
#matchesString = ''.join(matches)  #converting from list to string
#numbers = re.findall(numPattern, matchesString)

#numbersInt = [int(num) for num in numbers] #converting to integer list

#print(numbersInt)
'''
for i in range(0,len(numbersInt)-1,2):
    value = (numbersInt[i] * numbersInt[i+1])
    print(value)
    #print(value)
    sum += value
print(sum)


print(off)
print(on)
'''

#random code:

#for i in range(len(result)):
#   if currentstate == True:
#       pass
# #multiply
