def main():
    pass

def prime_factors(num):
    return []

def is_prime(num):
    return None

def test_prime_factors():
    assert prime_factors(1)     == []
    assert prime_factors(2)     == [2]
    assert prime_factors(3)     == [3]
    assert prime_factors(13195) == [5, 7, 13, 29]

def test_is_prime():
    assert is_prime(2)     == 'True'
    assert is_prime(3)     == 'True'
    assert is_prime(6)     == 'False'
    assert is_prime(13195) == 'False'

if __name__ == "__main__":
    main()