
length = int(input("Enter the side of the square  : "))
ch = input("Enter the character to use in the square : ")

for row in range(length):
    for column in range(length):
        if(row == 0 or row == length - 1 or column == 0 or column == length - 1):
            print(ch, end = ' ')
        else:
            print(' ', end = ' ')
    print()
    
    