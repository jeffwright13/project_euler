def main():
    pass

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

def test_is_palindrome():
    assert is_palindrome(1)    == None
    assert is_palindrome(11)   == True
    assert is_palindrome(21)   == False
    assert is_palindrome(2111) == False
    assert is_palindrome(2112) == True

if __name__ == "__main__":
    main()