arr = []
xmasCountp2 = 0


with open("/Users/edenlittlefair/Downloads/adventofcode/day4/puzzle4testing.txt", "r") as f:
    for line in f:
        arr.append(list(line.strip()))

print(arr[0])

#for ["M", "", "M"
#     "", "A", ""
#     "S", "", "S"]

for i in range(len(arr)-2): 
    for j in range(len(arr)-2):
        if arr[i][j] == "M" and arr[i][j+2] == "M" and arr[i+1][j+1] == "A" and arr[i+2][j] == "S" and arr[i+2][j+2] == "S":
            xmasCountp2 += 1

for i in range(len(arr)-2): 
    for j in range(len(arr)-2):
        if arr[i][j] == "S" and arr[i][j+2] == "S" and arr[i+1][j+1] == "A" and arr[i+2][j] == "M" and arr[i+2][j+2] == "M":
            xmasCountp2 += 1

for i in range(len(arr)-2): 
    for j in range(len(arr)-2):
        if arr[i][j] == "S" and arr[i][j+2] == "M" and arr[i+1][j+1] == "A" and arr[i+2][j] == "S" and arr[i+2][j+2] == "M":
            xmasCountp2 += 1

for i in range(len(arr)-2): 
    for j in range(len(arr)-2):
        if arr[i][j] == "M" and arr[i][j+2] == "S" and arr[i+1][j+1] == "A" and arr[i+2][j] == "M" and arr[i+2][j+2] == "S":
            xmasCountp2 += 1

'''
for i in range(len(arr[0])-3): #for rotation south-east
    for j in range(len(arr)-3):
        if arr[i][j] == "X" and arr[i+1][j+1] == "M" and arr[i+2][j+2] == "A" and arr[i+3][j+3] == "S":
            xmasCount += 1

for i in range(len(arr[0])-3): #for rotation south
    for j in range(len(arr)):
        if arr[i][j] == "X" and arr[i+1][j] == "M" and arr[i+2][j] == "A" and arr[i+3][j] == "S":
            xmasCount += 1

for i in range(0, len(arr[0])-3): #for rotation south-west
    for j in range(3, len(arr)):
        if arr[i][j] == "X" and arr[i+1][j-1] == "M" and arr[i+2][j-2] == "A" and arr[i+3][j-3] == "S":
            xmasCount += 1
'''

print("XMAS count part 2:",xmasCountp2)
#print(arr) 