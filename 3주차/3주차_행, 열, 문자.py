def printPattern(rows=5, clse=5, char="*"):
                 for _ in range(rows):
                     for _ in range(cols):
                         print(char, end="")
                     print()

printPattern(3,10,"%")
