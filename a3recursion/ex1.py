# this is an example of a recursive method

def sum_num(num):
    '''
    This function will recursivly determine the sum of the digits in an integer number.
    :param num:  a positive integer
    :return: an integer that is the sum of the digits
    '''
    # base case. if there is only one digit return it.
    if(num//10==0):
        return num

    # recursive case.
    # If there is more than one digit, take off the last digit and call sum_num on a remaining number
    else:
        return num%10 + sum_num(num//10)


def main():
    test_numbers=[4,12,145,54321,8765903]
    for i in range(5):
         print("Test {0} Input {1}. Output: {2}".format(i,test_numbers[i],sum_num(test_numbers[i])))


main()