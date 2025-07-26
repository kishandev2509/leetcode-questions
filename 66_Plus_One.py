def plusOne(digits: list[int]) -> list[int]:
    curr_digit = len(digits) - 1
    carry = 1
    while carry and curr_digit >= 0:
        digits[curr_digit] = digits[curr_digit] + 1
        carry = digits[curr_digit] // 10
        digits[curr_digit] = digits[curr_digit] % 10
        curr_digit = curr_digit - 1
    if carry:
        digits.insert(0, 1)
    return digits


def main():
    tests = [[1, 2, 3], [4, 3, 2, 1], [9]]
    for test in tests:
        print(f"{test} = {plusOne(test)}")


if __name__ == "__main__":
    main()
