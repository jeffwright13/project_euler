def main():
    # Enumerate all 3-digit numbers
    threes = enumerate_3s()

    # Find products of all pairs of 3-digit numbers
    p = products(threes)

    # Find which products are palindromes
    palindromes = []
    for item in p:
        if is_palindrome(item):
            palindromes.append(item)
    print max(palindromes)

def is_palindrome(num):
    numstr = str(num)
    return (numstr == numstr[::-1])

def enumerate_3s():
    threes = []
    for i in range (111, 1000):
        if len(str(i)) == 3:
            threes.append(i)
    return threes

def products(nums):
    prods = []
    for i in nums:
        for j in nums:
            prods.append(i * j)
    return prods

def test_is_palindrome():
    assert is_palindrome(1)    == True
    assert is_palindrome(11)   == True
    assert is_palindrome(21)   == False
    assert is_palindrome(131)  == True
    assert is_palindrome(133)  == False
    assert is_palindrome(2111) == False
    assert is_palindrome(2112) == True

def test_products():
    assert products([]) == []
    assert products([1]) == [1]
    assert products([1, 2]) == [1, 2, 2, 4]
    assert products([1, 2, 3]) == [1, 2, 3, 2, 4, 6, 3, 6, 9]

def test_enumerate_3s():
    assert 111 in enumerate_3s()
    assert 999 in enumerate_3s()

if __name__ == "__main__":
    main()