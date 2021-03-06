#Name: ICS4U class
# Date: Jan 18, 2016

def selectionSort(n):
    '''
    :param n: n is a list of non-negative integers
    :return:None. But sorts n in ascending order using selection sort
    '''

    # start searching for the smallest element
    for i in range(0,len(n)-1):
        # minpos is the index of the smallest element
        minpos=i
        # j is index of the next element in the list to be compared
        for j in range(i+1,len(n)):
            # if the next value is lower than minpos's value, update minpos
            if n[j] < n[minpos] :
                minpos=j
        print(" pass {0}:".format(i), n)

        #Swap the values at index i and minpos
        temp=n[i]
        n[i]=n[minpos]
        n[minpos]=temp




def bubbleSort(n):
    '''
    :param n: n is a list of non-negative integers
    :return: None. But sorts n in ascending order using bubble sort
    '''

    # add comments to explain how i, j, and temp are being used.
    # add comments to demonstrate your understanding of how bubble sort works.
    for i in range(0,len(n)):

        for j in range(0,len(n)-i-1):
            numcomparisons=0
            if n[j] > n[j+1] :
                numcomparisons+=1
                temp=n[j]
                n[j]=n[j+1]
                n[j+1]=temp
        print(" pass {0}:".format(i),n)



def insertionSort(n):
     ''' This method will take a small sub list which is sorted, and add the next element in the correct position of the sorted lsit.
     Each pass of the list will make the sorted sublist larger and the unsorted sublist smaller by 1.
    :param n: n is a list of non-negative integers
    :return: None.  but sorts n in ascending order using insertion sort
    '''
     for i in range(len(n)):
         value=n[i]
         #pos will start at index i. it will seperate the sorted and unsorted sublists
         pos=i
         while pos>0 and n[pos-1]>value :
             # move it down the sorted list so that value is in the correct position
             n[pos]=n[pos-1]
             pos-=1
         n[pos]=value
         print(" pass {0}:".format(i),n)



#*BONUS*
def mergeSort(n):
    '''
    :param n: n is a list of non-negative integers
    :return: None, but sorts n in ascending order using merge sort
    '''

    if len(n)>1:
        mid = len(n)//2
        # create right and left sublists this makes copies of lists
        lefthalf = n[:mid]
        righthalf = n[mid:]

        mergeSort(lefthalf)
        mergeSort(righthalf)

        # lefthalf and righthalf are sorted lists. Merge them.
        i=0 # index for lefthalf
        j=0 # index for righthalf
        k=0 # index for n
        while i < len(lefthalf) and j < len(righthalf):
            if lefthalf[i] < righthalf[j]:
                n[k]=lefthalf[i]
                i=i+1
            else:
                n[k]=righthalf[j]
                j=j+1
            k=k+1

        #add the rest of the lefthalf to n
        while i < len(lefthalf):
            n[k]=lefthalf[i]
            i=i+1
            k=k+1

        #add the rest of the righthalf to n
        while j < len(righthalf):
            n[k]=righthalf[j]
            j=j+1
            k=k+1


def main():
    test1=[92,97,81,27,22,17,85,8,73,12]
    test2=[31,83,81,7,56,71,43,63,13,49]
    test3=[90,86,75,83,62,86,89,46,70,14]

    insertionSort(test3)



main()