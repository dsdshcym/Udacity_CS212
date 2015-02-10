#------------------
# User Instructions
#
# Hopper, Kay, Liskov, Perlis, and Ritchie live on
# different floors of a five-floor apartment building.
#
# 1. Hopper does not live on the top floor.
# 2. Kay does not live on the bottom floor.
# 3. Liskov does not live on either the top or the bottom floor.
# 4. Perlis lives on a higher floor than does Kay.
# 5. Ritchie does not live on a floor adjacent to Liskov's.
# 6. Liskov does not live on a floor adjacent to Kay's.
#
# Where does everyone live?
#
# Write a function floor_puzzle() that returns a list of
# five floor numbers denoting the floor of Hopper, Kay,
# Liskov, Perlis, and Ritchie.

import itertools

def adjacent(a, b):
    if abs(a-b) == 1:
        return True
    return False

def floor_puzzle():
    # Suggest solution
    floors = bottom, _, _, _, top = [1, 2, 3, 4, 5]
    orderings = list(itertools.permutations(floors))
    for (Hopper, Kay, Liskov, Perlis, Ritchie) in orderings:
        if (Hopper is not top
            and Kay is not bottom
            and Liskov is not top
            and Liskov is not bottom
            and Perlis > Kay
            and not adjacent(Ritchie, Liskov)
            and not adjacent(Liskov, Kay)):
            return [Hopper, Kay, Liskov, Perlis, Ritchie]

    # My solution
    for Hopper, Kay, Liskov, Perlis, Ritchie in itertools.permutations(range(1, 6)):
        if Liskov != 1 and Liskov != 5:
            if Hopper != 5:
                if Kay != 1:
                    if Perlis > Kay:
                        if not adjacent(Ritchie, Liskov):
                            if not adjacent(Liskov, Kay):
                                return [Hopper, Kay, Liskov, Perlis, Ritchie]

print floor_puzzle()
