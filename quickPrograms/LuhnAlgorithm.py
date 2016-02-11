#1. Accept any number to check
#2. reverse the digits
#3. add all the digits in the odd positions. call thsi sum A
#4. double each of the remainin digits
#5. find the sum of the remaining digits. call thsi sum B
#6. calculate C=A+B
#7 if C ends in a 0, then the number is valid, otherwise it is invalid

def luhnAlgorithm(cardNUmber):
    ''' Perform the luhn algorithm to determine if a number is valid.
    :param cardNUmber: any integer that represents a check number.
    :return: True or False, depending on if the number is valid or not
    '''
    