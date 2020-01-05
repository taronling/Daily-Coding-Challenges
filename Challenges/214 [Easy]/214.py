'''
This problem was asked by Stripe.

Given an integer n, return the length of the longest consecutive run of 1s in its binary representation.

For example, given 156, you should return 3.
'''

def binary_interpreter(n):
    binary_val = ""
    while n > 0:
        binary_val = str(n % 2) + binary_val
        n = n/2
    # print("Binary conversion of base 10 value:", n, "is:", binary_val)
    return binary_val

def longest_sequence(binary_val):
    longest_seq = 0
    for i, c in enumerate(binary_val):
        counter = 0
        while ((i+counter) < len(binary_val)) and binary_val[i+counter] == "1":
            counter += 1
        if counter > longest_seq:
            longest_seq = counter
    return longest_seq

def main(n):
    longest_len = longest_sequence(binary_interpreter(n))
    print(longest_len)

if __name__ == "__main__":
    input = int(input("Enter integer n: "))
    main(input)
