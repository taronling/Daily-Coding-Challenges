"""
This problem was asked by YouTube.

Write a program that computes the length of the longest common subsequence of three given strings. For example, given "epidemiologist", "refrigeration", and "supercalifragilisticexpialodocious", it should return 5, since the longest common subsequence is "eieio".
"""

def longest(string_1, string_2, string_3):
    for a in string_1:
        for b in string_2:
            for c in string_3:



if __name__ == "__main__":
    string_1 = "epidemiologist"
    string_2 = "refrigeration"
    string_3 = "supercalifragilisticexpialodocious"
    longest(string_1, string_2, string_3)
