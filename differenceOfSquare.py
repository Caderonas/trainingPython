def differenceOfSquares(nb):
    output = 1
    for i in range(2, nb+1):
        output += i
    output = output ** 2
    for i in range(1, nb+1):
        output -= i ** 2
    output = -output if output < 0 else output
    return output