# 69. Sqrt(x)

def mySqrt(x: int) -> int:
    left,right=0,x
    while left<right:
        mid = left + (right-left) // 2
        # print(f"{left=}, {right=}, {mid=} ")
        if mid*mid>x:
            right=mid
        else:
            left=mid+1
    return left-1 if left > 0 else 0


def main():
    tests = [0,4,9,16,8,25,36,24,20]
    for test in tests:
        print(f"{test} = {mySqrt(test)}")

if __name__ == "__main__":
    main()