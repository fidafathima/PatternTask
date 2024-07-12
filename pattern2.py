#design with inputs 3 and 5 as rows and columns respectively


def pattern2(rows, cols):
    for c in range(rows):
            print("  ___     ", end="")
    print()
    for r in range(rows):
        
        for c in range(rows):
            print(" /   \ ", end="")
            if c!=cols-rows:  
             print("___",end="")
        print()
        
        for c in range(rows):
            print(" \___/ ", end="")
            break
        for c in range(rows-1):
            print("    \___/ ", end="")
        print()
        
rows = 3
cols = 5
pattern2(rows, cols)