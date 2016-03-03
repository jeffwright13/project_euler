def main():
    # By listing the first six prime numbers: 2, 3, 5, 7, 11, and 13,
    # we can see that the 6th prime is 13.
    # What is the 10001st prime number?
    print gen_prime(10001)

def gen_prime(num):
    count = 0
    candidate = 1
    while count < num:
        candidate += 1
        if is_prime(candidate):
            count += 1
    return candidate

def is_prime(num):
    for i in range(2, num):
        if num % i == 0:
            return False
    return True

def test_gen_prime():
    assert gen_prime (1)   == 2
    assert gen_prime (6)   == 13
    assert gen_prime (7)   == 17
    assert gen_prime (100) == 541

def test_is_prime():
    assert is_prime(2)     == True
    assert is_prime(3)     == True
    assert is_prime(4)     == False
    assert is_prime(6)     == False
    assert is_prime(13195) == False

if __name__ == "__main__":
    main()
    