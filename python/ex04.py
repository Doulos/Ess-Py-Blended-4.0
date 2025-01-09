def compare(a, b):
    assert type(a) is list and type(b) is list
    assert len(a) == len(b)
    result = []
    for i in range(len(a)):
        if a[i] == b[i]:
            result.append(1)
        else:
            result.append(0)
    return result


assert compare([1, 2], [1, 2]) == [1, 1]
assert compare([1, 2], [3, 4]) == [0, 0]
assert compare([1, 2, 3], [4, 2, 6]) == [0, 1, 0]
print("All tests passed :)")
