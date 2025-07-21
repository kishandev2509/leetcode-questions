# 3479. Fruits Into Baskets III


def numOfUnplacedFruits(fruits: list[int], baskets: list[int]) -> int:
    visited = [False] * len(baskets)
    unplaced = 0
    for fruit in fruits:
        placed = False
        for i in range(len(baskets)):
            if not visited[i] and baskets[i] >= fruit:
                visited[i] = True
                placed = True
                break
        if not placed:
            unplaced += 1
    return unplaced


def main():
    tests = [
        [[3, 6, 1], [6, 4, 7]],
        [[4, 2, 5], [3, 5, 4]],
    ]
    for test in tests:
        print(f"{test} = {numOfUnplacedFruits(test[0], test[1])}")


if __name__ == "__main__":
    main()
