from string import ascii_uppercase
n = int(input())
alphabet = ascii_uppercase * (n**2//26+1)
alphabet = alphabet[:n**2]
ln = len(alphabet)
print("+ " + "="*((n*2)-1) + " +")
grid = []
for _ in range(n):
    grid.append([' ']*n)
min_row = 0
min_col = 0
max_row = n
max_col = n
i = 0
while i < ln:
    #left to right
    row = min_row
    for col in range(min_col, max_col):
        if i == ln:
            break
        if col == min_col:
            grid[row][col] = " \\" + alphabet[i]
        elif col == max_col - 1 and row == 0:
            grid[row][col] = alphabet[i]# + " |"
        else:
            grid[row][col] = alphabet[i]
        i += 1
    min_row += 1
    #top to bottom
    col = max_col-1
    for row in range(min_row, max_row):
        if i == ln:
            break
        if row == max_row - 1:
            grid[row][col] = " \\" + alphabet[i]
        elif i in range (max_col - 1, max_col + n):
            grid[row][col] = alphabet[i]# + " |"
        else:
            grid[row][col] = alphabet[i]
        i += 1
    max_col -= 1
    #right to left
    row = max_row-1
    for col in range(max_col-1, min_col-1, -1):
        if i == ln:
            break
        grid[row][col] = " "
        i += 1
    max_row -= 1
    #bottom to top
    col = min_col
    for row in range(max_row-1, min_row-1, -1):
        if i == ln:
            break
        grid[row][col] = " "
        i += 1
    min_col += 1
#print grid
for row in range(n):
    for col in range(n):
        print(grid[row][col], end=' ')
    print("|")
print(" "*(n*2+2) + '+')