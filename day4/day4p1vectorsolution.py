'''
arr = []
xmasCount = 0

# Load the grid
with open("/Users/edenlittlefair/Downloads/adventofcode/day4/puzzle4.txt", "r") as f:
    for line in f:
        arr.append(list(line.strip()))

def count_xmas_in_direction(dx, dy):
    """Count occurrences of 'XMAS' in a specific direction defined by dx, dy."""
    count = 0
    rows, cols = len(arr), len(arr[0])
    for i in range(rows):
        for j in range(cols):
            # Check boundaries
            if 0 <= i + 3 * dx < rows and 0 <= j + 3 * dy < cols:
                if (
                    arr[i][j] == "X" and
                    arr[i + dx][j + dy] == "M" and
                    arr[i + 2 * dx][j + 2 * dy] == "A" and
                    arr[i + 3 * dx][j + 3 * dy] == "S"
                ):
                    count += 1
    return count

# Directions: (dx, dy) pairs
directions = [
    (0, 1),   # East
    (1, 1),   # Southeast
    (1, 0),   # South
    (1, -1),  # Southwest
    (0, -1),  # West
    (-1, 0),  # North
    (-1, -1), # Northwest
    (-1, 1)   # Northeast
]

# Count XMAS in all directions
for dx, dy in directions:
    xmasCount += count_xmas_in_direction(dx, dy)

print("XMAS count:", xmasCount)
'''
arr = [list(line.strip()) for line in open("/Users/edenlittlefair/Downloads/adventofcode/day4/puzzle4.txt")]
xmasCount = sum(0 <= i + 3 * dx < len(arr) and 0 <= j + 3 * dy < len(arr[0]) and
                arr[i][j] == "X" and arr[i + dx][j + dy] == "M" and
                arr[i + 2 * dx][j + 2 * dy] == "A" and arr[i + 3 * dx][j + 3 * dy] == "S"
                for dx, dy in [(0, 1), (1, 1), (1, 0), (1, -1), (0, -1), (-1, 0), (-1, -1), (-1, 1)]
                for i in range(len(arr)) for j in range(len(arr[0])))
print("XMAS count:", xmasCount)
