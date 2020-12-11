def fibonacciSimpleSum(number):
    if number <= 4:
        return True

    numbers = {x for x in range(4)}

    last_number = 3
    this_number = 5

    while this_number <= number:
        target = number - this_number

        if target in numbers or target == this_number:
            return True
        else:
            numbers.add(this_number)

        next_number = last_number + this_number
        last_number = this_number
        this_number = next_number

    return False
