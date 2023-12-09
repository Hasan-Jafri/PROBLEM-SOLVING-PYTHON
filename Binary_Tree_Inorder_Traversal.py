# Definition for a binary tree node.


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def build_binary_tree():
    root_value = int(input("Enter Root Value: "))
    root = TreeNode(root_value)

    queue = [root]

    while queue:
        current = queue.pop(0)

        left_value = int(input(f"Enter Left Child of {current.val} (Enter -1 if none): "))
        if left_value != -1:
            left_child = TreeNode(left_value)
            current.left = left_child
            queue.append(left_child)

        right_value = int(input(f"Enter Right Child of {current.val} (Enter -1 if none): "))
        if right_value != -1:
            right_child = TreeNode(right_value)
            current.right = right_child
            queue.append(right_child)

    return root

def inorderTraversal( root):
    result = []
    Inorder(root,result)
    return result

def Inorder(root,result):
    if root is not None:
        Inorder(root.left,result)
        result.append(root.val)
        Inorder(root.right,result)


root = build_binary_tree()
print(inorderTraversal(root=root))