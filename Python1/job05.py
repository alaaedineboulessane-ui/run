def alphabet():
    abc = "abcdefghijklmnopqrstuvwxyz"
    cba = ""
    for i in range(len(abc)):
        cba += abc[len(abc)-1-i]
    return cba
"""print(alphabet())"""

string = "Je suis une string"
print(string)