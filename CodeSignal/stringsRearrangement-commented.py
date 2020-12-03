# CodeSignal problem: https://app.codesignal.com/arcade/intro/level-7/PTWhv2oWqd6p4AHB9
# This solution on CodeSignal: https://app.codesignal.com/arcade/intro/level-7/PTWhv2oWqd6p4AHB9/solutions?solutionId=cNGxjcQ9Mti5fmTNe
# Time complexity O(n!)
# Space complexity O(n^2)
# Uncommented solution: stringsRearrangement.py


# We could have used Python's itertools.permutations function to avoid
# a recursive solution, but I prefer this version, and I think it is a
# little clearer.
def stringsRearrangement(inputArray):
    """Given an array of equal-length strings, return true if they can be
    arranged in any order such that each string is exactly one
    character different than the one before it.
    """

    # Try every word to see whether it can be the first word of a list
    # that matches the conditions. Return True immediately the first
    # time we find a matching list.
    for this_word in inputArray:
        remaining = inputArray[:]
        remaining.remove(this_word)
        if test_remaining(this_word, remaining):
            return True

    return False


def almost_same(this_word, next_word):
    """Return true if two words are exactly one character different"""

    different = False  # we haven't found any differences yet
    for i in range(len(this_word)):
        if this_word[i] != next_word[i]:
            if different:
                # we were already different, now we are too different
                return False
            else:
                # we are just different enough
                different = True

    return different


def test_remaining(this_word, remaining):
    """Without changing the first word, test if the rest of the list can
    be arranged in an order that satisfies the requirements
    """

    # This is the terminating condition for the recursive
    # function, we only have one word left in the list, return
    # whether it meets the conditions
    if len(remaining) == 1:
        return almost_same(this_word, *remaining)

    # Check every remaining word to see if it is one different
    # from the first word
    for next_word in remaining:
        if almost_same(this_word, next_word):
            # Make a new list that doesn't have the next word,
            # then test it with the next word as the first word of
            # the new test
            rest = remaining[:]
            rest.remove(next_word)
            if test_remaining(next_word, rest):
                # Once we find a passing list, we don't have to
                # run any more tests because the conditions only
                # require us to return whether or not there is a
                # passing list, not count how many there are. They
                # also don't require us to return the list we
                # found.
                return True

    # We got through the whole loop without finding a passing list
    return False
