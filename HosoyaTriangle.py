# James Bebarski
# November 2, 2022
# Project: Hosoya's Triangle

def hosoyaTriangle(levels):
    
    # Default list.
    triangle = []
    
    # One level/row
    if levels == 1:
        triangle = [[1]]
    
    # Two levels/rows
    elif levels == 2:
        triangle = [[1], 
                    [1, 1]]
    
    # Three levels/rows
    elif levels == 3:
        triangle = [[1], 
                    [1, 1], 
                    [2, 1, 2]]
    
    # If requested triangle has more than 3 rows, we call levelBuilder to calculate the additional levels/rows. 
    elif levels > 3:
        triangle = levelBuilder(
            [[1], 
             [1, 1], 
             [2, 1, 2]], levels - 1)
    
    return triangle
    
# Function that recursively builds Hosoya Triangle rows/levels.
def levelBuilder(working_triangle_list, level):
    
    # Calculates new levels while level is above base cases. 
    while level >= 3: 
        
        # Recursive call to build the levels of the triangle. 
        working_triangle_list = levelBuilder(working_triangle_list, level - 1)
        
        # Default row list 
        row = []
        
        # Depending on value locations, we use either recurrance relation 1 or 2.
        for i in range(level + 1):
            
            # Reccurance Relation 1: H(n, j) = H(n - 1, j) + H(n - 2, j)
            if i < level - 1:
                row.append(working_triangle_list[level - 1][i] + working_triangle_list[level - 2][i])
            
            # Reccurance Relation 2: H(n, j) = (n - 1, j - 1) + H(n - 2, j - 2)
            else:
                row.append(working_triangle_list[level - 1][i - 1] + working_triangle_list[level - 2][i - 2])
        
        # Append new row to working list.        
        working_triangle_list.append(row)
        
        # On to next row.
        return working_triangle_list
    
    else:
        
        return working_triangle_list

# Prints list in a visually pleasing way.
def getFormat(unformatted_triangle):
    
    # Prints each sublist/row/level, without brackets, on it's own line. 
    for i in range(len(unformatted_triangle)):
        for j in unformatted_triangle[i]:
            print(j, end = " ")
        print("")
        
    return 

def main():
    
    # User input, enters requested number of rows in triangle. 
    requested_levels = int(input("Enter the requested number of levels for Hosoya's Triangle.\n>>> "))
    
    # Requested triangle, with rows/levels given as list of lists.
    unformatted_triangle = hosoyaTriangle(requested_levels)
    
    # Calls getFormat to print our formatted list for presentation. 
    getFormat(unformatted_triangle)
    
if __name__ == "__main__":    
    main()
