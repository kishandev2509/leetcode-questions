from collections import deque

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
        
    def __repr__(self) -> str:
        return f"{self.val}({self.left if self.left else '-'},{self.right if self.left else '-'})"
        

def create_tree(listt:list)-> TreeNode | None:
    if not listt or listt[0] is None:
        return None

    root = TreeNode(listt[0])
    queue = deque()
    queue.append((root, 0))  # (node, index_in_listtay)

    while queue:
        current_node, index = queue.popleft()

        # Calculate child indices
        left_index = 2 * index + 1
        right_index = 2 * index + 2

        # Add left child
        if left_index < len(listt) and listt[left_index] is not None:
            current_node.left = TreeNode(listt[left_index])
            queue.append((current_node.left, left_index))

        # Add right child
        if right_index < len(listt) and listt[right_index] is not None:
            current_node.right = TreeNode(listt[right_index])
            queue.append((current_node.right, right_index))

    return root