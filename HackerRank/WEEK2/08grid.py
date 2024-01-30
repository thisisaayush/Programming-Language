def gridArrange(grid):
    for i in range(len(grid)):
        grid[i] = ''.join(sorted(grid[i]))
    
    for j in range(len(grid[0])):
        for k in range(1,len(grid)):
            if grid[k - 1][j] > grid[k][j]:
                return 'NO'
        
    return 'YES'