# Each number can not be duplicated
# 9x9 grid of numbers
# numbers in row and column

sudoku = [[0, 0, 0, 0, 0, 0, 0, 0, 0],
          [0, 0, 0, 0, 0, 0, 0, 0, 0],
          [0, 0, 0, 0, 0, 0, 0, 0, 0],
          [0, 0, 0, 0, 0, 0, 0, 0, 0],
          [0, 0, 0, 0, 0, 0, 0, 0, 0],
          [0, 0, 0, 0, 0, 0, 0, 0, 0],
          [0, 0, 0, 0, 0, 0, 0, 0, 0],
          [0, 0, 0, 0, 0, 0, 0, 0, 0],
          [0, 0, 0, 0, 0, 0, 0, 0, 0]]

blanksudoku = [[0, 0, 0, 0, 0, 0, 0, 0, 0],
               [0, 0, 0, 0, 0, 0, 0, 0, 0],
               [0, 0, 0, 0, 0, 0, 0, 0, 0],
               [0, 0, 0, 0, 0, 0, 0, 0, 0],
               [0, 0, 0, 0, 0, 0, 0, 0, 0],
               [0, 0, 0, 0, 0, 0, 0, 0, 0],
               [0, 0, 0, 0, 0, 0, 0, 0, 0],
               [0, 0, 0, 0, 0, 0, 0, 0, 0],
               [0, 0, 0, 0, 0, 0, 0, 0, 0]]

checked = []
validnum = []
cubenum = []


def compareval():
    global checked
    global validnum
    for a in range(0, 9):
        if (a + 1) in checked:
            print("%d already exists" % (a + 1))
        else:
            validnum.append(a + 1)
    print("These numbers can be placed: ", validnum)
    validnum = []


def crosscheck(row, col):
    global checked
    global validnum
    global sudoku
    for a in range(0, 9):
        if sudoku[row][a] > 0:
            print("Number %d in Row: %d Column: %d" % (sudoku[row][a], (row + 1), (a + 1)))
            if sudoku[row][a] not in checked:
                checked.append(sudoku[row][a])
    for c in range(0, 9):
        if sudoku[c][col] > 0:
            print("Number %d in Row: %d Column: %d" % (sudoku[c][col], (c + 1), (col + 1)))
            if sudoku[c][col] not in checked:
                checked.append(sudoku[c][col])
    if row >= 0 and row <= 2 and col >= 0 and col <= 2:
        checkcube(0)
    elif row >= 0 and row <= 2 and col >= 3 and col <= 5:
        checkcube(1)
    elif row >= 0 and row <= 2 and col >= 6 and col <= 8:
        checkcube(2)
    elif row >= 3 and row <= 5 and col >= 0 and col <= 2:
        checkcube(3)
    elif row >= 3 and row <= 5 and col >= 3 and col <= 5:
        checkcube(4)
    elif row >= 3 and row <= 5 and col >= 6 and col <= 8:
        checkcube(5)
    elif row >= 6 and row <= 8 and col >= 0 and col <= 2:
        checkcube(6)
    elif row >= 6 and row <= 8 and col >= 3 and col <= 5:
        checkcube(7)
    elif row >= 6 and row <= 8 and col >= 6 and col <= 8:
        checkcube(8)
    for b in range(0, 9):
        if not checked:
            validnum.append(b + 1)
        elif (b + 1) not in checked:
            validnum.append(b + 1)
    print("Used Numbers:", checked)
    print("Valid Numbers:", validnum)


def solve2(row, col):
    global checked
    global sudoku
    global validnum
    if row >= 0 and row <= 2 and col >= 0 and col <= 2:
        solvecube(0)
    elif row >= 0 and row <= 2 and col >= 3 and col <= 5:
        solvecube(1)
    elif row >= 0 and row <= 2 and col >= 6 and col <= 8:
        solvecube(2)
    elif row >= 3 and row <= 5 and col >= 0 and col <= 2:
        solvecube(3)
    elif row >= 3 and row <= 5 and col >= 3 and col <= 5:
        solvecube(4)
    elif row >= 3 and row <= 5 and col >= 6 and col <= 8:
        solvecube(5)
    elif row >= 6 and row <= 8 and col >= 0 and col <= 2:
        solvecube(6)
    elif row >= 6 and row <= 8 and col >= 3 and col <= 5:
        solvecube(7)
    elif row >= 6 and row <= 8 and col >= 6 and col <= 8:
        solvecube(8)


def cubesolving(a, b, c):
    global checked
    global validnum
    global sudoku
    global cubenum
    if sudoku[b][c] == 0:
        if sudoku[b][c] > 0:
            if sudoku[b][c] not in checked:
                checked.append(sudoku[b][c])
            if sudoku[b][c] not in cubenum:
                cubenum.append(sudoku[b][c])
        for d in range(0, 9):
            if sudoku[b][d] > 0:
                print("Number %d in Row: %d Column: %d" % (sudoku[b][d], (b + 1), (d + 1)))
                if sudoku[b][d] not in checked:
                    checked.append(sudoku[b][d])
        for d in range(0, 9):
            if sudoku[d][c] > 0:
                print("Number %d in Row: %d Column: %d" % (sudoku[d][c], (d + 1), (c + 1)))
                if sudoku[d][c] not in checked:
                    checked.append(sudoku[d][c])
        print("Cube %d Row: %d Column: %d Value: %d" % ((a + 1), (b + 1), (c + 1), sudoku[b][c]))
        for e in range(1, 10):
            if e not in cubenum:
                if e not in checked:
                    validnum.append(e)
        print("Numbers Used", checked)
        print("Valid Numbers", validnum)
        if validnum:
            sudoku[b][c] = validnum[0]
    checked = []
    validnum = []


def checkpuzzel():
    global sudoku
    for a in range(0, 9):
        for b in range(0, 9):
            if sudoku[a][b] == 0:
                print("Sudoku puzzle is not correct")
                return a, b
            else:
                print("Sudoku puzzle is solved")


def cubesearch():
    global checked
    global validnum
    global sudoku
    for a in range(0, 9):
        for b in range(0, 9):
            if sudoku[a][b] == 0:
                for c in range(0, 9):
                    if sudoku[a][c] > 0 and sudoku[a][c] not in checked:
                        checked.append(sudoku[a][c])
                for c in range(0, 9):
                    if sudoku[c][b] > 0 and sudoku[c][b] not in checked:
                        checked.append(sudoku[c][b])
                for c in range(1, 10):
                    if c not in checked:
                        validnum.appened(c)
                sudoku[a][b] = validnum[0]
            checked = []
            validnum = []


def solvecube(a):
    global cubenum
    if a == 0:
        for b in range(0, 3):
            for c in range(0, 3):
                cubesolving(a, b, c)
    elif a == 1:
        for b in range(0, 3):
            for c in range(3, 6):
                cubesolving(a, b, c)
    elif a == 2:
        for b in range(0, 3):
            for c in range(6, 9):
                cubesolving(a, b, c)
    elif a == 3:
        for b in range(3, 6):
            for c in range(0, 3):
                cubesolving(a, b, c)
    elif a == 4:
        for b in range(3, 6):
            for c in range(3, 6):
                cubesolving(a, b, c)
    elif a == 5:
        for b in range(3, 6):
            for c in range(6, 9):
                cubesolving(a, b, c)
    elif a == 6:
        for b in range(6, 9):
            for c in range(0, 3):
                cubesolving(a, b, c)
    elif a == 7:
        for b in range(6, 9):
            for c in range(3, 6):
                cubesolving(a, b, c)
    elif a == 8:
        for b in range(6, 9):
            for c in range(6, 9):
                cubesolving(a, b, c)
    cubenum = []


def checkcube(a):
    global checked
    global sudoku
    if a == 0:
        for b in range(0, 3):
            for c in range(0, 3):
                print("Cube %d Row: %d Column: %d Value: %d" % ((a + 1), (b + 1), (c + 1), sudoku[b][c]))
                if sudoku[b][c] > 0:
                    if sudoku[b][c] not in checked:
                        checked.append(sudoku[b][c])
    elif a == 1:
        for b in range(0, 3):
            for c in range(3, 6):
                print("Cube %d Row: %d Column: %d Value: %d" % ((a + 1), (b + 1), (c + 1), sudoku[b][c]))
                if sudoku[b][c] > 0:
                    if sudoku[b][c] not in checked:
                        checked.append(sudoku[b][c])
    elif a == 2:
        for b in range(0, 3):
            for c in range(6, 9):
                print("Cube %d Row: %d Column: %d Value: %d" % ((a + 1), (b + 1), (c + 1), sudoku[b][c]))
                if sudoku[b][c] > 0:
                    if sudoku[b][c] not in checked:
                        checked.append(sudoku[b][c])
    elif a == 3:
        for b in range(3, 6):
            for c in range(0, 3):
                print("Cube %d Row: %d Column: %d Value: %d" % ((a + 1), (b + 1), (c + 1), sudoku[b][c]))
                if sudoku[b][c] > 0:
                    if sudoku[b][c] not in checked:
                        checked.append(sudoku[b][c])
    elif a == 4:
        for b in range(3, 6):
            for c in range(3, 6):
                print("Cube %d Row: %d Column: %d Value: %d" % ((a + 1), (b + 1), (c + 1), sudoku[b][c]))
                if sudoku[b][c] > 0:
                    if sudoku[b][c] not in checked:
                        checked.append(sudoku[b][c])
    elif a == 5:
        for b in range(3, 6):
            for c in range(6, 9):
                print("Cube %d Row: %d Column: %d Value: %d" % ((a + 1), (b + 1), (c + 1), sudoku[b][c]))
                if sudoku[b][c] > 0:
                    if sudoku[b][c] not in checked:
                        checked.append(sudoku[b][c])
    elif a == 6:
        for b in range(6, 9):
            for c in range(0, 3):
                print("Cube %d Row: %d Column: %d Value: %d" % ((a + 1), (b + 1), (c + 1), sudoku[b][c]))
                if sudoku[b][c] > 0:
                    if sudoku[b][c] not in checked:
                        checked.append(sudoku[b][c])
    elif a == 7:
        for b in range(6, 9):
            for c in range(3, 6):
                print("Cube %d Row: %d Column: %d Value: %d" % ((a + 1), (b + 1), (c + 1), sudoku[b][c]))
                if sudoku[b][c] > 0:
                    if sudoku[b][c] not in checked:
                        checked.append(sudoku[b][c])
    elif a == 8:
        for b in range(6, 9):
            for c in range(6, 9):
                print("Cube %d Row: %d Column: %d Value: %d" % ((a + 1), (b + 1), (c + 1), sudoku[b][c]))
                if sudoku[b][c] > 0:
                    if sudoku[b][c] not in checked:
                        checked.append(sudoku[b][c])


def solve():
    global sudoku
    global checked
    global validnum
    solving = True
    while solving:
        for a in range(0, 9):
            for b in range(0, 9):
                if sudoku[a][b] == 0:
                    print("Row: %d Column: %d" % ((a + 1), (b + 1)))
                    crosscheck(a, b)
                    if validnum:
                        print("Number: %d was places in Row: %d Column: %d" % (validnum[0], (a + 1), (b + 1)))
                        sudoku[a][b] = validnum[0]
                    checked = []
                    validnum = []
        if 0 not in sudoku:
            solving = False


def attempt2(puzzle):
    return


adding = True
while adding:
    action = input("[add], [solve], [solve2], [checkall], [check], [checkcube], [show], [done]?")
    if action == "add":
        row = int(input("What Row?"))
        slot = int(input("What Column?"))
        number = int(input("What numbers do you want to add 1 - 9, 0 is empty?"))
        if not isinstance(number, int):
            print("You did not Type a number")
        else:
            sudoku[(row - 1)][(slot - 1)] = number
            print("Number:%d was added to Row:%d Column:%d" % (number, row, slot))
    elif action == "solve":
        solve()
    elif action == "solve2":
        for a in range(0, 9):
            for b in range(0, 9):
                if sudoku[a][b] == 0:
                    solve2(a, b)
    elif action == "checkall":
        for a in range(0, 9):
            for b in range(0, 9):
                if sudoku[a][b] > 0:
                    crosscheck(a, b)
                    checked = []
                    validnum = []
    elif action == "done":
        adding = False
    elif action == "show":
        for a in range(0, 9):
            print(sudoku[a])
    elif action == "check":
        checkpuzzel()
    else:
        print("Wrong value")
