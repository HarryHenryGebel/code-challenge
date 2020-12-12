def fibonacciSimpleSum(number):
    if number < 12:
        return True

    numbers = {0, 1, 2, 3, 5}

    last_number = 5
    this_number = 8

    while this_number <= number:
        numbers.add(this_number)
        target = number - this_number

        if target in numbers:
            return True

        next_number = last_number + this_number
        last_number = this_number
        this_number = next_number

    return False
