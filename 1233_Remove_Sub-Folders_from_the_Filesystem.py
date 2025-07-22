# 1233. Remove Sub-Folders from the Filesystem

def removeSubfolders(folder: list[str]) -> list[str]:
    folder.sort()
    result = [folder[0]]
    for i in range(1, len(folder)):
        if not folder[i].startswith(result[-1] + "/"):
            result.append(folder[i])
    return result
    
    


def main():
    tests = [["/a","/a/b","/c/d","/c/d/e","/c/f"],["/a","/a/b/c","/a/b/d"],["/a/b/c","/a/b/ca","/a/b/d"]]
    for test in tests:
        print(f"{test} = {removeSubfolders(test)}")

if __name__ == "__main__":
    main()