#design with inputs 4 and 7 as rows and columns respectively

def pattern(rows, cols):
    for c in range(rows):
            print("  ___     ", end="")
    print()
    for r in range(rows):
        
        for c in range(rows):
            print(" /   \\ ", end="")
            if c!=cols-rows:  
             print("___",end="")
        print()
        
        for c in range(rows):
            print(" \\___/ ", end="")
            break
        for c in range(rows-1):
            print("    \\___/ ", end="")
        print()
        
rows = 4
cols = 7
pattern(rows, cols)
                
