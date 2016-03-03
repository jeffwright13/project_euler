def main():
    print sum_square_diff(1, 100)

def sum_square_diff(lower, upper):
    if lower <= 0:
        return None

    
def test_sum_square_diff():
    assert sum_square_diff(0, 1)    == None
    assert sum_square_diff(1, 3)    == 6
    assert sum_square_diff(2, 4)    == 12
    assert sum_square_diff(1, 10)   == 2520

if __name__ == "__main__":
    main()