# 13. Roman to Integer


def romanToInt(s: str) -> int:
    roman_values = {"I": 1, "V": 5, "X": 10, "L": 50, "C": 100, "D": 500, "M": 1000}
    i = 0
    num = 0
    while i < len(s):
        if i + 1 < len(s) and roman_values[s[i]] < roman_values[s[i + 1]]:
            num += roman_values[s[i + 1]] - roman_values[s[i]]
            i += 2
        else:
            num += roman_values[s[i]]
            i += 1
    return num
    
    


def main():
    tests = ["III","LVIII","MCMXCIV"]
    for test in tests:
        print(f"{test} = {romanToInt(test)}")

if __name__ == "__main__":
    main()