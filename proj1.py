# File:        proj1.py
# Written by:  Kyle Fritz
# Date:        11/14/2013
# Lab Section: 10
# UMBC email:  fritzk1@umbc.edu
# Description: This is an autofill program.
############### USE WITH PYTHON 3 ###########
# scl enable python33 bash


def printGreeting():
    print("This is the autofill program!")

# input: The contents of the file, the coordinates, and the maximum values that
#    X and Y can be.
# output: The contents of the file after autofill.
def autoFill(columnList, x, y, maxX, maxY):
    if columnList[y][x] == ".":
        columnList[y][x] = "x"
        if y - 1 >= 0:
            autoFill(columnList, x, y - 1, maxX, maxY)
        if y + 1 <= maxY:    
            autoFill(columnList, x, y + 1, maxX, maxY)
        if x - 1 >= 0:
            autoFill(columnList, x - 1, y, maxX, maxY)
        if x + 1 <= maxX:
            autoFill(columnList, x + 1, y, maxX, maxY)
    else:
        return columnList
    return columnList

# input: The contents of the file and a count of 0.
# output: Displays the contents of the file after autofill.
def displayAutofill(columnList, count):
    for i in columnList:
        for j in i:
            count += 1
            print(j, end = "")
            try:
                i[count]
            except IndexError:
                count = 0
                print()

# input: A non-valid X coordinate and the maximum value that X can be.
# output: A valid X coordinate.
def getXCoordinates(x, maxX):
    while x < 0 or x > maxX:
        try:
            x = int(input("Type in a valid X coordinate: "))
        except ValueError:
            x = -1
    return x

# input: A non-valid Y coordinate and the maximum value that Y can be.
# output: A valid Y coordinate.
def getYCoordinates(y, maxY):
   while  y < 0 or y > maxY:
       try:
           y = int(input("Type in a valid Y coordinate: "))
       except ValueError:
           y = -1
   return y
        
# input: The file that was read.
# output: The contents of the file and a list of lists of the contents.
def readFile(theFile):
    columnList = []
    for i in theFile:
        print(i)
        # k makes a list of the X values.
        k = list(i)
        for j in k:
            if j == "\n":
                k.remove(j)
        columnList.append(k)
    return columnList

# input: List of contents in the file.
# output: Maximum values for X and Y coordinates.
def maxCoordinates(columnList):
    maxX = 0
    maxY = 0
    for i in columnList:
        maxY += 1
        for j in i:
            maxX += 1
    # The number of js divided by the number of lines in the file will 
    #   give number of characters in each line.
    maxX = maxX/maxY
    # Length - 1 will give actual maximum values.
    maxX, maxY = maxX - 1, maxY - 1
    return maxX, maxY

def main():
    printGreeting()
    # Set filename
    fileName = "a"
    # Maximum coordinates
    maxX = 0
    maxY = 0
    while fileName.lower() != "quit" and fileName.lower() != "q":
        # List for contents of the file
        columnList = []
        # Non-valid X and Y values
        x = -1
        y = -1
        try:
            print("Type in the name of the file that you would")
            fileName = input("like to open up or type 'quit' to exit: ")
            if fileName.lower() != "quit" and fileName.lower() != "q":
                theFile = open(fileName, "r")
                print("\nThis is what your file looks like before autofill:")
                # Get contents of the file to columnList and display what is 
                #   on the file before autofill
                columnList = readFile(theFile)
                maxX, maxY = maxCoordinates(columnList)
                x = getXCoordinates(x, maxX)
                y = getYCoordinates(y, maxY)
                columnList = autoFill(columnList, x, y, maxX, maxY)
                count = 0
                print("This is what the file looks like after autofill")
                displayAutofill(columnList, count)
                theFile.close()
        except FileNotFoundError:
            print("Please type in a valid file name.")
            #  Change fileName to something that isn't 'quit' or a .txt file
            fileName = "a"
main()
