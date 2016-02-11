#Name:
#Date:
# Practice creating and iterating through two-dimentional lists. (2D arrays)

'''
Complete the following problems in the Console.
create an empty list named L
add a number to it usign .append()
add another number to it.
add an empty list to it
add the numbers from 5 to 30 counting by 5 to the empty list using a loop
add your name as the last element of L
think about the length of L, and the list inside L.
'''

def printArray(list):
    ''' Print out a 2d list in chart form
    :param list: a 2D list
    :return: None
    '''
    for i in range(len(list)):
        for j in range(len(list[i])):
            print(list[i][j],end="\t")
        print()

# 2dLists Exercises: Goal: become familiar on how to iterate through 2 dimentional lists and solve problems.
# be aware of the index values of the loop, and the position in the 2d list.

#Q1 Create a 3 by 5 2dlist with the elements from 1 to 15 using a doouble for loop.
def makeList(numRows,numCols):
    '''
    :param numRows: n is an in. the number of rows
    :param numCols: m is an integer. the number of colums
    :return: a list of size n x m containing the numbers from 1 to n*m
    '''
    L=[]
    #create a list of numRows empty lists
    for i in range(numRows):
        L.append([])
    #create the 2d list and fill it with the integers from 1 to n*m
    for i in range(numRows):
        for j in range(numCols):
            L[i].append(i*numCols+j+1)

#Q2 add the elements in each row. print the sum. Add the sum to the end of each row.

# add the elements of the row. track it in a vriable. reset the variable each time. then append it.
for i in range(len(L)):
    rowSum=0
    for j in range(len(L[i])):
        rowSum+=L[i][j]
    L[i].append(rowSum)

#Q3 Add up the elements in each column. Pring the sum. Add the sum to the end of each column.
L.append([])
for i in range(6):
    L[3].append([])
for i in range(6):
    colSum=0
    for j in range(3):
        colSum+=L[j][i]
    L[3][i]=colSum
printArray(L)