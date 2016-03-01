def main():
    print max(prime_factors(9))

def prime_factors(num):
    pf = primes = []

    # Get primes to use as possible factors
    for i in range(2, (num+1)/2):
        if is_prime(i):
            primes.append(i)
    print "done 1st:", primes

    # Find which primes are actually factors
    for elem in primes:
        if num % elem == 0:
            print "elem, pf:", elem, pf
            pf.append(num)
    print "done 2nd:", pf
    return pf

def is_prime(num):
    for i in range(2, num):
        if num % i == 0:
            return False
    return True

def test_prime_factors():
    assert prime_factors(1)     == []
    assert prime_factors(2)     == [2]
    assert prime_factors(3)     == [3]
    assert prime_factors(4)     == [2]
    assert prime_factors(12)    == [2, 3]
    assert prime_factors(17)    == [17]
    assert prime_factors(147)   == [3, 7]
    assert prime_factors(13195) == [5, 7, 13, 29]

def test_is_prime():
    assert is_prime(2)     == True
    assert is_prime(3)     == True
    assert is_prime(4)     == False
    assert is_prime(6)     == False
    assert is_prime(13195) == False

if __name__ == "__main__":
    main()