#Name:
#Date:
#See handout for exercises. 5 problems to complete.

def sumDigits(n):

    # base case
    if n//10==0:
        return n

    #recursive case
    else:
        return n%10+sumDigits(n//10)


def main():
    print(sumDigits(524))

main()
