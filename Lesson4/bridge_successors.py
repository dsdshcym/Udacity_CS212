# -----------------
# User Instructions
#
# Write a function, bsuccessors(state), that takes a state as input
# and returns a dictionary of {state:action} pairs.
#
# A state is a (here, there, t) tuple, where here and there are
# frozensets of people (indicated by their times), and potentially
# the 'light,' t is a number indicating the elapsed time.
#
# An action is a tuple (person1, person2, arrow), where arrow is
# '->' for here to there or '<-' for there to here. When only one
# person crosses, person2 will be the same as person one, so the
# action (2, 2, '->') means that the person with a travel time of
# 2 crossed from here to there alone.

LEFT_ARROW = '<-'
RIGHT_ARROW = '->'
LIGHT = 'light'

def bsuccessors(state):
    """Return a dict of {state:action} pairs. A state is a (here, there, t) tuple,
    where here and there are frozensets of people (indicated by their times) and/or
    the 'light', and t is a number indicating the elapsed time. Action is represented
    as a tuple (person1, person2, arrow), where arrow is '->' for here to there and
    '<-' for there to here."""
    here, there, t = state

    # if 'light' in here:
    #     return dict(((here - frozenset([a, b, 'light'])),
    #                  (there | frozenset([a, b, 'light']),
    #                   t + max(a, b)),
    #                  (a, b, '->'))
    #                 for a in here if a is not 'light'
    #                 for b in here if b is not 'light')
    # else:
    #     return dict(((here | frozenset([a, b, 'light'])),
    #                  (there - frozenset([a, b, 'light']),
    #                   t + max(a, b)),
    #                  (a, b, '<-'))
    #                 for a in there if a is not 'light'
    #                 for b in there if b is not 'light')

    # my solution
    ans = {}
    if LIGHT in here:
        arrow = RIGHT_ARROW
        here = set(here) - {LIGHT}
        there = set(there) | {LIGHT}
        for person1 in here:
            for person2 in here:
                new_here = frozenset(here - {person1, person2})
                new_there = frozenset(there | {person1, person2})
                time = max(person1, person2)
                new_state = (new_here, new_there, t+time)
                new_action = (person1, person2, arrow)
                ans[new_state] = new_action
    else:
        arrow = LEFT_ARROW
        here = set(here) | {LIGHT}
        there = set(there) - {LIGHT}
        for person1 in there:
            for person2 in there:
                new_here = frozenset(here | {person1, person2})
                new_there = frozenset(there - {person1, person2})
                time = max(person1, person2)
                new_state = (new_here, new_there, t+time)
                new_action = (person1, person2, arrow)
                ans[new_state] = new_action
    return ans

def test():

    assert bsuccessors((frozenset([1, 'light']), frozenset([]), 3)) == {
        (frozenset([]), frozenset([1, 'light']), 4): (1, 1, '->')}

    assert bsuccessors((frozenset([]), frozenset([2, 'light']), 0)) == {
        (frozenset([2, 'light']), frozenset([]), 2): (2, 2, '<-')}

    return 'tests pass'

print test()
