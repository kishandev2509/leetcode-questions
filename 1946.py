# Largest Number After Mutating Substring


# def maximumNumber(num: str, change: list[int]) -> str:
#     new_num = ""
#     changed, missed = False, False
#     for digit in num:
#         if change[int(digit)] == int(digit):
#             new_num += digit
#             continue
#         if change[int(digit)] > int(digit) and not missed:
#             new_num += str(change[int(digit)])
#             changed = True
#         else:
#             if changed:
#                 missed = True
#             new_num += digit
#     return new_num

def maximumNumber(num: str, change: list[int]) -> str:
    new_num = []
    changed = False
    changes = {str(i) : str(change[i]) for i in range(10)}
    
    for digit in num:
        if changed:
            if changes[digit] >= digit:
                new_num.append(changes[digit])
            else:
                return "".join(new_num) + num[len(new_num):]
        elif changes[digit] > digit:
            new_num.append(changes[digit])
            changed = True
        else:
            new_num.append(digit)
    return "".join(new_num)

def main():
    tests = [
        ["334111", [0, 9, 2, 3, 3, 2, 5, 5, 5, 5]],
        ["214010", [6, 7, 9, 7, 4, 0, 3, 4, 4, 7]],
        ["132", [9, 8, 5, 0, 3, 6, 4, 2, 6, 8]],
        ["021", [9, 4, 3, 5, 7, 2, 1, 9, 0, 6]],
        ["5", [1, 4, 7, 5, 3, 2, 5, 6, 9, 4]],
    ]
    for test in tests:
        print(f"{test} = {maximumNumber(test[0], test[1])}")


if __name__ == "__main__":
    main()
