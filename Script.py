"ok this is my first mechanism to save things but what things :O"


# start = open("Saves.txt", "w+")

# for i in range(10):
#     start.write("This is line %d\n" % (i+1))

# start.close()

print("\nWelcome to Lines Editor\n")
answer = input(
    "what you want to do:\n\n1. Create new line\n2. Edit exist line\n3. Delete exist line\n4. Nothing\n")


if answer == "1":
    append = open("Saves.txt", "a+")
    newLine = input("Type your new line: ")
    append.write(newLine + "\n")
    append.close()

if answer == "2":
    print("Ok so those are your lines: ")

    file1 = open("Saves.txt", "r")
    existLines = file1.readlines()

    countedLines = (len(existLines))
    clearedList = []
    for i in existLines:
        clearedList.append(i.strip())

    numberList = []
    x = 1
    while x <= countedLines:
        for line in clearedList:
            numberList.append({x: line})
            x = x+1
    print(numberList)
    file1.close()
    lineToEdit = int(input("Which line you want to edit?: "))
    if lineToEdit <= countedLines:
        editLines = clearedList[(lineToEdit-1)]
        changedLine = input(
            "Please type new line insted of previous one :) : ")
        clearedList[(lineToEdit-1)] = changedLine
        print(clearedList)
        file2 = open("Saves.txt", "w+")
        for i in clearedList:
            file2.write(i+"\n")
        file2.close()

    else:
        print("bye")

if answer == "3":
    print("Ok so those are your lines: ")

    file1 = open("Saves.txt", "r")
    existLines = file1.readlines()

    countedLines = (len(existLines))
    clearedList = []
    for i in existLines:
        clearedList.append(i.strip())

    numberList = []
    x = 1
    while x <= countedLines:
        for line in clearedList:
            numberList.append({x: line})
            x = x+1
    print(numberList)
    file1.close()

    lineToDelete = int(input("Ok so which line you want to delete?: "))
    if lineToDelete <= countedLines:
        clearedList.remove(clearedList[(lineToDelete-1)])
        print(clearedList)
        file2 = open("Saves.txt", "w+")
        for i in clearedList:
            file2.write(i+"\n")
        file2.close()

    else:
        print("bye")
else:
    None
