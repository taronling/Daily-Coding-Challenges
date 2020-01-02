'''
This problem was asked by Microsoft.

Given a string and a pattern, find the starting indices of all occurrences of the pattern in the string. For example, given the string "abracadabra" and the pattern "abr", you should return [0, 7].
'''
answer = []
def index_occurrences(string, pattern, n):
    index = string.find(pattern)
    if index == -1:
        return
    else:
        answer.append(index + n)
        index_occurrences(string[index + len(pattern):], pattern, index + len(pattern) + n)

if __name__ == "__main__":
    string = "tarontarontaron"
    pattern = "tar"
    index_occurrences(string, pattern, 0)
    print(answer)