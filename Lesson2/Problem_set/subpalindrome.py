# --------------
# User Instructions
#
# Write a function, longest_subpalindrome_slice(text) that takes
# a string as input and returns the i and j indices that
# correspond to the beginning and end indices of the longest
# palindrome in the string.
#
# Grading Notes:
#
# You will only be marked correct if your function runs
# efficiently enough. We will be measuring efficency by counting
# the number of times you access each string. That count must be
# below a certain threshold to be marked correct.
#
# Please do not use regular expressions to solve this quiz!

def grow(text, start, end):
    while ((start > 0) and (end < len(text))
           and (text[start - 1].upper() == text[end].upper())):
        start -= 1
        end += 1
    return start, end

def longest_subpalindrome_slice(text):
    "Return (i, j) such that text[i:j] is the longest palindrome in text."
    # A nice solution
    text = text.lower()
    pals = newpals = [(i,i+1) for i in range(len(text))] + [(i, i) for i in range(len(text)+1)] 
    while newpals:
        pals = newpals
        newpals = [(i-1, j+1) for i,j in pals
                   if i>0 
                      and j<len(text) 
                      and text[i-1] == text[j]]
    return pals[0]

    # Suggest solution
    if text == '': return 0, 0
    def length(slice): a, b = slice; return b-a
    candidates = [grow(text, start, end)
                  for start in range(len(text))
                  for end in (start, start+1)]
    return max(candidates, key=length)

    # My solution
    end, max_len = 0, 0
    upper_text = str.upper(text)
    N = len(upper_text)
    f = [[1, 1] for i in range(N)]
    for i in range(1, N):
        if (f[i-1][1] != i) and (upper_text[i - f[i-1][1] - 1] == upper_text[i]):
            f[i][1] = f[i-1][1] + 2
        if (f[i-1][0] != i) and (upper_text[i - f[i-1][0] - 1] == upper_text[i]):
            if f[i-1][0] + 2 > f[i][1]:
                f[i][1] = f[i-1][0] + 2
        if (upper_text[i-1] == upper_text[i]):
                f[i][0] = f[i-1][0] + 1
        if f[i][1] > max_len:
            end, max_len = i+1, f[i][1]
        if f[i][0] > max_len:
            end, max_len = i+1, f[i][0]
    return end - max_len, end

def test():
    L = longest_subpalindrome_slice
    assert L('racecar') == (0, 7)
    assert L('Racecar') == (0, 7)
    assert L('RacecarX') == (0, 7)
    assert L('Race carr') == (7, 9)
    assert L('') == (0, 0)
    assert L('something rac e car going') == (8,21)
    assert L('xxxxx') == (0, 5)
    assert L('xxxxxx') == (0, 6)
    assert L('Mad am I ma dam.') == (0, 15)
    return 'tests pass'

print test()
