# --------------
# User Instructions
#
# Write a function, compile_word(word), that compiles a word
# of UPPERCASE letters as numeric digits. For example:
# compile_word('YOU') => '(1*U + 10*O +100*Y)'
# Non-uppercase words should remain unchaged.

def compile_word(word):
    """Compile a word of uppercase letters as numeric digits.
    E.g., compile_word('YOU') => '(1*U+10*O+100*Y)'
    Non-uppercase words unchanged: compile_word('+') => '+'"""
    # Suggest solution
    if word.isupper():
        terms = [('%s*%s' % (10**i, d))
                  for (i, d) in enumerate(word[::-1])]
        return '(' + '+'.join(terms) + ')'

    # My solution
    if not re.search('[A-Z]', word):
        return word
    ans = '('
    N = len(word)
    for i in range(N, 0, -1):
        if i < N:
            ans += '+'
        ans += (str(10**(i-1))+'*'+word[N-i])
    ans += ')'
    return ans

print compile_word('YOU')
print compile_word('+')
