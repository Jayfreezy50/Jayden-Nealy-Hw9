#Jayden
class TreeNode:
    def __init__(self, n):
        self.value = n
        self.left = None
        self.right = None

def inputNodes():
    root_value = int(input("Enter value for the root node: "))
    root = TreeNode(root_value)
    queue = [root]

    while queue:
        current = queue.pop(0)

        left_value = input(f"Enter value for the left child of {current.value} ('None' if no child): ")
        if left_value != 'None':
            left_value = int(left_value)
            current.left = TreeNode(left_value)
            queue.append(current.left)

        right_value = input(f"Enter value for the right child of {current.value} ('None' if no child): ")
        if right_value != 'None':
            right_value = int(right_value)
            current.right = TreeNode(right_value)
            queue.append(current.right)

    return root

def printTreeNodes(node):
    if node is None:
        return
    printTreeNodes(node.left)
    print(node.value, end=" ")
    printTreeNodes(node.right)

def divisibleValues(root):
    if root is None:
        return 0

    current_value = root.value if root.value % 5 == 0 else 0
    left_sum = divisibleValues(root.left)
    right_sum = divisibleValues(root.right)
    return current_value + left_sum + right_sum

if __name__ == "__main__":
    root = inputNodes()
    print(f"\nSum of node values divisible by 5: {divisibleValues(root)}")
    print("\nIn-order traversal of the tree:")
    printTreeNodes(root)
    print()
