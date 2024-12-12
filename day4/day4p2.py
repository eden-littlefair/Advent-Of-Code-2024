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

#for ["S", "", "S"
#     "", "A", ""
#     "M", "", "M"]

for i in range(len(arr)-2): 
    for j in range(len(arr)-2):
        if arr[i][j] == "S" and arr[i][j+2] == "S" and arr[i+1][j+1] == "A" and arr[i+2][j] == "M" and arr[i+2][j+2] == "M":
            xmasCountp2 += 1

#for ["S", "", "M"
#     "", "A", ""
#     "S", "", "M"]

for i in range(len(arr)-2): 
    for j in range(len(arr)-2):
        if arr[i][j] == "S" and arr[i][j+2] == "M" and arr[i+1][j+1] == "A" and arr[i+2][j] == "S" and arr[i+2][j+2] == "M":
            xmasCountp2 += 1

#for ["M", "", "S"
#     "", "A", ""
#     "M", "", "S"]

for i in range(len(arr)-2): 
    for j in range(len(arr)-2):
        if arr[i][j] == "M" and arr[i][j+2] == "S" and arr[i+1][j+1] == "A" and arr[i+2][j] == "M" and arr[i+2][j+2] == "S":
            xmasCountp2 += 1

print("XMAS count part 2:",xmasCountp2)
#print(arr) 