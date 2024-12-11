import re
sum = 0

with open("/Users/edenlittlefair/Downloads/adventofcode/day3/puzzle3.txt", "r") as f:
    lines = f.readlines()
#print(lines)
charString = ''.join(lines)
#print(charString)

#string mul( then integer 1-3 digits then string , t
pattern = r'mul\(\d{1,3}\,\d{1,3}\)'
matches = re.findall(pattern, charString)
print(matches)

numPattern = r'\d{1,3}'
matchesString = ''.join(matches)  #converting from list to string
numbers = re.findall(numPattern, matchesString)

numbersInt = [int(num) for num in numbers] #converting to integer list

#print(numbersInt)

for i in range(0,len(numbersInt)-1,2):
    value = (numbersInt[i] * numbersInt[i+1])
    print(value)
    #print(value)
    sum += value
print(sum)
