# -----------
# User Instructions
#
# Write a function, deal(numhands, n=5, deck), that
# deals numhands hands with n cards each.
#

import random # this will be a useful library for shuffling

# This builds a deck of 52 cards. If you are unfamiliar
# with this notation, check out Andy's supplemental video
# on list comprehensions (you can find the link in the
# Instructor Comments box below).

mydeck = [r+s for r in '23456789TJQKA' for s in 'SHDC']

def deal(numhands, n=5, deck=mydeck):
    # Suggest solution
    random.shuffle(deck)
    return [deck[n * i:n * (i + 1)] for i in range(0, numhands)]

    # My solution
    random.shuffle(deck)
    ans = []
    for i in range(0, numhands):
        ans.append([deck[j] for j in range(i, i + n)])
    return ans

print deal(1)

