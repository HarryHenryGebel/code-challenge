def stringsRearrangement(inputArray):
    for this_word in inputArray:
        remaining = inputArray[:]
        remaining.remove(this_word)
        if test_remaining(this_word, remaining):
            return True

    return False


def almost_same(this_word, next_word):
    different = False
    for i in range(len(this_word)):
        if this_word[i] != next_word[i]:
            if different:
                return False
            else:
                different = True

    return different


def test_remaining(this_word, remaining):
    if len(remaining) == 1:
        return almost_same(this_word, *remaining)

    for next_word in remaining:
        if almost_same(this_word, next_word):
            rest = remaining[:]
            rest.remove(next_word)
            if test_remaining(next_word, rest):
                return True

    return False
