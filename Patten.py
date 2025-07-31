"""
*         *
 *      *
   *  *
    *
   *  *
 *      *
*         *
"""
n = 4  
for i in range(n):
    for j in range(n):
        print(" " if j != i else "*", end="")
    for j in range(n - 1, -1, -1):
        print(" " if j != i else "*", end="")
    print()
for i in range(n - 2, -1, -1):
    for j in range(n):
        print(" " if j != i else "*", end="")
    for j in range(n - 1, -1, -1):
        print(" " if j != i else "*", end="")
    print()
