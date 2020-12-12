def fibonacciSimpleSum(number):
    """Determine if a number is the sum of two Fibonacci numbers. Return
True if it is, otherwise return False."""

    # 0, 1, 2, and 3 are Fibonacci numbers, and all Fibonacci numbers
    # pass because 0 is a Fibonacci number, and x + 0 = x, 4 passes
    # because 2 + 2 = 4, etc. 12 is the first number that is not the
    # sum of 2 Fibonacci numbers.
    if number < 12:
        return True

    # Store all the Fibonacci numbers that we have found so far. Seed
    # the set with Fibonacci numbers up to 5. Note: these are all the
    # Fibonacci numbers up to 5, but they are not the Fibonacci set,
    # which has 1 twice. For our purposes we don't need the actual
    # Fibonacci set because we only need a list of numbers we can
    # check. There is no reason to check a number twice. Only storing
    # 1 once allows us to use the very efficient Python set
    # collection.
    numbers = {0, 1, 2, 3, 5}

    # The first Fibonacci number we will actually add to the starting
    # set is 8.
    last_number = 5
    this_number = 8

    while this_number <= number:
        # Store this number and see what number we have to add to get
        # the target
        numbers.add(this_number)
        target = number - this_number

        # Check if the target number is a Fibonacci number we've
        # already found. If it is return True, otherwise, add it to
        # our set of Fibonacci numbers.
        if target in numbers or target == this_number:
            return True

        # advance to the next Fibonacci number.
        next_number = last_number + this_number
        last_number = this_number
        this_number = next_number

    # The loop exited without finding a match, so return False
    return False
