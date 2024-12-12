arr = []
xmasCount = 0


with open("/Users/edenlittlefair/Downloads/adventofcode/day4/puzzle4.txt", "r") as f:
    for line in f:
        arr.append(list(line.strip()))

print(arr[0])

    
for i in range(len(arr[0])): #for rotation east
    for j in range(len(arr)-3):
        if arr[i][j] == "X" and arr[i][j+1] == "M" and arr[i][j+2] == "A" and arr[i][j+3] == "S":
            xmasCount += 1

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

for i in range(len(arr[0])): #for rotation west
    for j in range(3,len(arr)):
        if arr[i][j] == "X" and arr[i][j-1] == "M" and arr[i][j-2] == "A" and arr[i][j-3] == "S":
            xmasCount += 1

for i in range(3,len(arr[0])): #for rotation north
    for j in range(len(arr)):
        if arr[i][j] == "X" and arr[i-1][j] == "M" and arr[i-2][j] == "A" and arr[i-3][j] == "S":
            xmasCount += 1

for i in range(3,len(arr[0])): #for rotation north-west
    for j in range(3,len(arr)):
        if arr[i][j] == "X" and arr[i-1][j-1] == "M" and arr[i-2][j-2] == "A" and arr[i-3][j-3] == "S":
            xmasCount += 1

for i in range(3,len(arr[0])): #for rotation north-east
    for j in range(len(arr)-3):
        if arr[i][j] == "X" and arr[i-1][j+1] == "M" and arr[i-2][j+2] == "A" and arr[i-3][j+3] == "S":
            xmasCount += 1

print("XMAS count:",xmasCount)
#print(arr)