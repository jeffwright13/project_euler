def main():
    # Enumerate all palindromes less than 999*999
    palindromes = []
    for candidate in range(998001, 12321, -1):
        if is_palindrome(candidate):
            palindromes.append(candidate)
    print palindromes

    # Find which are the products of two 3-digit numbers
    factors = []
    for elem in palindromes:
        if is_product(elem):
            factors.append(elem)
    print factors

def is_palindrome(num):
    numstr = str(num)
    if len(numstr) % 2 != 0:
        return None

    first = numstr[:len(numstr)/2]
    last  = numstr[len(numstr)/2:]
    if first == last[::-1]:
        return True
    else:
        return False

def is_product(num):
    pass

def test_is_palindrome():
    assert is_palindrome(1)    == None
    assert is_palindrome(11)   == True
    assert is_palindrome(21)   == False
    assert is_palindrome(2111) == False
    assert is_palindrome(2112) == True

def test_is_product():
    assert is_product(997799)  == True
    
if __name__ == "__main__":
    main()