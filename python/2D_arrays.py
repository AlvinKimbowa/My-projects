num_grid = [
   [1, 2, 3, 4],
   [5, 6, 7, 8],
   [9, 0] 
]

#print(num_grid[1])
#print(num_grid[1][3])

#for i in range(len(num_grid[1])):
#    print(num_grid[1][i])

for row in num_grid:
    for col in row:
        print(col)
