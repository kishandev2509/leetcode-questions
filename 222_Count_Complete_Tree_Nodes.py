# 222. Count Complete Tree Nodes
from TreeNodeModule import TreeNode, create_tree


def countNodes(root: TreeNode | None) -> int:
    def get_left_height(root: TreeNode) -> int:
        height = 1
        while root.left is not None:
            height += 1
            root = root.left
        return height

    def get_right_height(root: TreeNode) -> int:
        height = 1
        while root.right is not None:
            height += 1
            root = root.right
        return height

    if root is None:
        return 0
    left_height = get_left_height(root)
    right_height = get_right_height(root)

    if left_height == right_height:
        return 2**left_height - 1
    else:
        return 1 + countNodes(root.left) + countNodes(root.right)
        



def main():
    tests = [[1,2,3,4,5,6],[],[1]]
    for test in tests:
        print(f"{test} = {countNodes(create_tree(test))}")

if __name__ == "__main__":
    main()
