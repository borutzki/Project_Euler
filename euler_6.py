def sumsquaredif(n):
    sum_of_squares = 0
    for i in range(1, n + 1):
        sum_of_squares += i ** 2

    print(f"Sum of squares: {sum_of_squares}")

    sum = 0
    for i in range(1, n + 1):
        sum += i

    square_of_sum = sum ** 2
    print(f"Square of sum: {square_of_sum}")

    difference = square_of_sum - sum_of_squares
    print(f"Difference: {difference}")


sumsquaredif(100)
