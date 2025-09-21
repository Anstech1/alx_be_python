# pattern_drawing.py

# Prompt user for pattern size
size = int(input("Enter the size of the pattern: "))

# Initialize row counter for while loop
row = 0

# Outer loop (while) for rows
while row < size:
    # Inner loop (for) for columns
    for col in range(size):
        print("*", end="")  # print * without new line
    print()  # move to the next row after each line
    row += 1
