# -----------
# User Instructions
#
# Modify the card_ranks() function so that cards with
# rank of ten, jack, queen, king, or ace (T, J, Q, K, A)
# are handled correctly. Do this by mapping 'T' to 10,
# 'J' to 11, etc...

def card_ranks(cards):
    "Return a list of the ranks, sorted with higher first."

    # My solution
    # ranks = [r for r,s in cards]
    # for i in range(0, len(ranks)):
    #     if ranks[i] == 'T':
    #         ranks[i] = '10'
    #     if ranks[i] == 'J':
    #         ranks[i] = '11'
    #     if ranks[i] == 'Q':
    #         ranks[i] = '12'
    #     if ranks[i] == 'K':
    #         ranks[i] = '13'
    #     if ranks[i] == 'A':
    #         ranks[i] = '14'
    #     ranks[i] = int(ranks[i])

    # Suggest solution
    ranks = ['--23456789TJQKA'.index(r) for r, s in cards]

    ranks.sort(reverse=True)
    return ranks

print card_ranks(['AC', '3D', '4S', 'KH']) #should output [14, 13, 4, 3]
