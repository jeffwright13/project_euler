def main():
    pass

def is_palindrome(num):
    if len(num) % 2 != 0:
        return False

def test_is_palindrome():
    assert is_palindrome(1)  == True
    assert is_palindrome(11) == True
    assert is_palindrome(21) == False

if __name__ == "__main__":
    main()