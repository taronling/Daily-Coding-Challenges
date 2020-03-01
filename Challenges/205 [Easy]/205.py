"""
This problem was asked by IBM.

Given an integer, find the next permutation of it in absolute order. For example, given 48975, the next permutation would be 49578.
"""

def foo(input):
    print(len(input)+1)
    for first in range(1, len(input)+1):
        # print(first)
        for second in range(first, len(input)+1):
            print(input[-second], input[-first])
            if input[-second] < input[-first]: # swap elements from index first and index second
                print("^")
                new_first = input[-second]
                new_second = input[-first]
                input[-second] = new_second
                input[-first] = new_first
                print(input)
                new_array = input[0:-second+1] + sorted(input[-second+1:], reverse = True)
                return new_array


if __name__ == "__main__":
    input = [3,4,2,1]
    # answer = foo(input)
    # print(answer)
    second_test = [1,2,4,3]
    print(foo(second_test))