def main():
    print sum_square_diff(1, 100)

def sum_square_diff(lower, upper):
    if lower <= 0:
        return None
    else:
        return square_sums(lower, upper) - sum_squares(lower, upper)

def sum_squares(lower, upper):
    sum = 0
    for i in range(lower, upper + 1):
        sum += i**2
    return sum

def square_sums(lower, upper):
    sum = 0
    for i in range(lower, upper + 1):
        sum += i
    return sum ** 2

def test_sum_square_diff():
    assert sum_square_diff(0, 1)  == None
    assert sum_square_diff(1, 10) == 2640

def test_sum_squares():
    assert sum_squares(0, 1)  == 1
    assert sum_squares(1, 4)  == 30
    assert sum_squares(2, 4)  == 29
    assert sum_squares(1, 10) == 385

def test_square_sums():
    assert square_sums(0, 1)  == 1
    assert square_sums(0, 2)  == 9
    assert square_sums(1, 4)  == 100
    assert square_sums(2, 4)  == 81
    assert square_sums(1, 10) == 3025

if __name__ == "__main__":
    main()