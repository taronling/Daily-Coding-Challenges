"""
This problem was asked by Facebook.

Given a number in Roman numeral format, convert it to decimal.

The values of Roman numerals are as follows:

{
    'M': 1000,
    'D': 500,
    'C': 100,
    'L': 50,
    'X': 10,
    'V': 5,
    'I': 1
}
In addition, note that the Roman numeral system uses subtractive notation for numbers such as IV and XL.

For the input XIV, for instance, you should return 14.
"""
import array
import itertools

def foo():
    # roman_input = input("Enter roman numerals: ").upper()
    roman_input = "XCL" #1090
    roman_numerals = {'M': 0, 'D': 1, 'C': 2, 'L': 3, 'X': 4, 'V': 5, 'I': 6}
    values = [1000]
    values.extend([500, 100, 50, 10, 5, 1])
    print(values)
    answer = 0
    prev_input = "M"
    for i, c in enumerate(roman_input):
        if roman_numerals[c] < roman_numerals[prev_input]:
            answer -= values[roman_numerals[c]]
            print(answer)
        else:
            answer += values[roman_numerals[c]]
            print(answer)
        prev_input = c
    try:
        return
    except:
        print("Invalid Roman Numeral")
        return


if __name__ == "__main__":
    foo()
