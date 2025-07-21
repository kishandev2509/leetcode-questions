def totalNumbers(digits: list[int]) -> int:
    s = set()
    for i, a in enumerate(digits):
        if a & 1:
            continue
        for j, b in enumerate(digits):
            if i == j:
                continue
            for k, c in enumerate(digits):
                if c == 0 or k in (i, j):
                    continue
                s.add(c * 100 + b * 10 + a)
    return len(s)


def main():
    tests = [
        [1, 2, 3, 4],
        [0, 2, 2],
        [6, 6, 6],
        [0, 1, 2],
        [6, 6, 6, 2],
        [6, 6, 6, 1],
        [0, 2, 2, 1],
        [1, 2, 2],
        [1, 2, 2, 3],
        [1, 1, 2, 3],
        [1, 2, 2, 3, 4],
        [1, 2, 3, 4, 5],
        [1, 2, 2, 3, 4],
        [1, 2, 3, 4, 6],
        [1, 1, 2, 3, 4],
        [1,2,3,4,5,6],
        [1,1,2,2,3,4],
        [1,1,2,2,3,3],
    ]
    for test in tests:
        print(f"{test} = {totalNumbers(test)}")
        


if __name__ == "__main__":
    main()
