def main():
    f = fibb(50)
    print f
    
    f2 = []
    for elem in f:
        if elem <= 4000000:
            f2.append(elem)
    print sum_evens(f2)

def fibb(max):
    if max <=2:
        raise ValueError("Fibb seq seed must be >= 2")

    fibb = [1, 2]
    last = fibb[0]
    this = fibb[1]

    for i in range(max-2):
        next = last + this
        fibb.append(next)
        last = this
        this = next

    return fibb

def sum_evens(seq):
    sum = 0
    for elem in seq:
        if elem % 2 == 0:
            sum += elem
            
    return sum

def test_fibb():
    #assert fibb(0)    == "Fibb seed must be >= 2"
    assert fibb(3)   == [1, 2, 3]
    assert fibb(10)  == [1, 2, 3, 5, 8, 13, 21, 34, 55, 89]

def test_sum_evens():
    assert sum_evens([1, 2, 3, 5, 8, 13, 21, 34, 55]) == 44
    assert sum_evens([0, 1, 0])                       == 0
    assert sum_evens([0, 4, 55, 8])                   == 12

if __name__ == "__main__":
    main()