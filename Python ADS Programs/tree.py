class TreeNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

def sorted_list_to_bst(arr):
    if not arr:
        return None

    mid = len(arr) // 2
    root = TreeNode(arr[mid])
    root.left = sorted_list_to_bst(arr[:mid])
    root.right = sorted_list_to_bst(arr[mid + 1:])
    return root

def preorder_traversal(root):
    if root is None:
        return []
    return [root.value] + preorder_traversal(root.left) + preorder_traversal(root.right)

# Example usage:
sorted_array = [1, 2, 3, 4, 5, 6, 7, 8]
bst_root = sorted_list_to_bst(sorted_array)
preorder_array = preorder_traversal(bst_root)
print(preorder_array)  # Output: [4, 2, 1, 3, 6, 5, 7]
