# 9. Palindrome Number

def isPalindrome(x: int) -> bool:
    if x < 0:
        return False
    num = x
    reverse_num = 0
    while num!=0:
        digit = num%10
        num = num//10
        reverse_num = (reverse_num*10)+digit

    return x == reverse_num

def main():
    tests = [121,-121,10]
    for test in tests:
        print(f"{test} = {isPalindrome(test)}")

if __name__ == "__main__":
    main()