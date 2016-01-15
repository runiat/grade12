#Name:
#Date:
#See handout for exercises. 5 problems to complete.

# Question 1
def sumDigits(n):
    # base case
    if n//10==0:
        return n
    #recursive case
    else:
        return n%10 + sumDigits(n//10)

#Question 2
def triangle(n):
    if n==0:
        return 0
    else:
        return n + triangle(n-1)

# Question 3
def binaryConvert(n):
    if n==0:
        return ""
    else:
        return binaryConvert(n//2) + str(n%2)

# Question 4
def convert(n,b):
    if n==0:
        return ""
    else:
        symbols=["0","1","2","3","4","5","6","7","8","9","A","B","C","D","E","F"]
        return convert(n//b, b) + symbols[n%b]


#Question 5
def isPalindrome(s):
    #base case: The string has 0 or 1 letters, then it must be a palindrome
    if len(s)==0:
        return True
    elif len(s)==1:
        return True
    else:
        # check if the first and last are the same, and check if the middle substring is a palindrome
        return isPalindrome(s[1:-1]) and s[0]==s[-1]





def main():
  print(triangle(4))

main()
