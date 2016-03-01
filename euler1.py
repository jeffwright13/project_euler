def main():
    import pytest
    print function(1000)

def function(max):
    count = 0
    for i in range(max):
        if i % 3 == 0 or i % 5 == 0:
            count += i
    return count

def test_function():
    assert function(10)   == 23
    assert function(1000) == 233168

if __name__ == "__main__":
    main()