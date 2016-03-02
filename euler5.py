def main():
    print smallest_evenly_divisible(1, 20)

def smallest_evenly_divisible(lower, upper):
    if lower <= 0:
        return None

    candidate = upper + 1
    done = False
    while 1:
        for elem in range(lower, upper + 1):
            if candidate % elem != 0:
                break
            else:
                if elem == upper:
                    done = True
                
        if done:
            break
        candidate += 1
    return candidate
    
def test_smallest_evenly_divisible():
    assert smallest_evenly_divisible(0, 1)    == None
    assert smallest_evenly_divisible(1, 3)    == 6
    assert smallest_evenly_divisible(2, 4)    == 12
    assert smallest_evenly_divisible(1, 10)   == 2520

if __name__ == "__main__":
    main()