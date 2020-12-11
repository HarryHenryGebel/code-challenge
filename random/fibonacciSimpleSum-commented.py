def fibonacciSimpleSum(number):
    # 0, 1, 2, and 3 are Fibonacci numbers, and all Fibonacci numbers
    # pass because 0 is a Fibonacci number, and x + 0 = x, 4 passes
    # because 2 + 2 = 4
    if number <= 5:
        return True

    # store all the numbers that we haven't matched yet
    # 0 .. 3 are all Fibonacci numbers
    numbers = {x for x in range(4)}

    # the first Fibonacci number we will actually check is 5
    last_number = 3
    this_number = 5

    while this_number <= number:
        # see what number we have to add to get the target
        target = number - this_number

        # Check if the target number is a Fibonacci number we've
        # already found, or if the current Fibonacci number can add
        # with itself, if it is return True, otherwise, add it to our
        # set of Fibonacci numbers.
        if target in numbers or target == this_number:
            return True
        else:
            numbers.add(this_number)

        # advance to the next Fibonacci number.
        next_number = last_number + this_number
        last_number = this_number
        this_number = next_number

    # The loop exited without finding a match, so return False
    return False
