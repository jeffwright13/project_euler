def main():
    import pytest
    print function(1000)

def function(max):
    pass

def test_function():
    assert function(10)   == 23
    assert function(1000) == 233168

if __name__ == "__main__":
    main()