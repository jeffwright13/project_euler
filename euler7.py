def main():
	pass

def is_prime(num):
    for i in range(2, num):
        if num % i == 0:
            return False
    return True

def test_is_prime():
    assert is_prime(2)     == True
    assert is_prime(3)     == True
    assert is_prime(4)     == False
    assert is_prime(6)     == False
    assert is_prime(13195) == False

if __name__ == "__main__":
    main()