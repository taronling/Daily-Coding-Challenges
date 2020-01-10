"""
This problem was asked by Palantir.

Write a program that checks whether an integer is a palindrome. For example, 121 is a palindrome, as well as 888. 678 is not a palindrome. Do not convert the integer into a string.
"""

def is_palindrome(n):
    print((len(n))//2)
    for i in range(0, (len(n))//2):
        if n[i] != n[-i]:
            return False
    return True

if __name__ == "__main__":
    input = "121"
    if is_palindrome(input):
        print("{} is a palindrome.".format(input))
    else:
        print("{} isn't a palindrome.".format(input))