# 367. Valid Perfect Square


def isPerfectSquare(num: int) -> bool:
    if num < 2:
        return True
    left, right = 0, num // 2
    while left < right:
        mid = left + (right - left) 
        if mid * mid == num:
            return True
        elif mid * mid > num:
            right = mid
        else:
            left = mid + 1
    return False



def main():
    tests = [16,14]
    for test in tests:
        print(f"{test} = {isPerfectSquare(test)}")

if __name__ == "__main__":
    main()