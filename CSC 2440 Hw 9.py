class TreeNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

def inputNodes():
    root = TreeNode(int(input("Enter root node value: ")))
    queue = [root]
    while queue:
        current = queue.pop(0)
        left = input(f"Enter left child of {current.value} (or 'None'): ")
        if left != 'None':
            current.left = TreeNode(int(left))
            queue.append(current.left)
        right = input(f"Enter right child of {current.value} (or 'None'): ")
        if right != 'None':
            current.right = TreeNode(int(right))
            queue.append(current.right)
    return root

def printTreeNodes(node):
    if node:
        printTreeNodes(node.left)
        print(node.value, end=" ")
        printTreeNodes(node.right)

def sumDivisibleByFive(node):
    if not node:
        return 0
    return (node.value if node.value % 5 == 0 else 0) + sumDivisibleByFive(node.left) + sumDivisibleByFive(node.right)

if __name__ == "__main__":
    tree = inputNodes()
    print(f"\nSum of values divisible by 5: {sumDivisibleByFive(tree)}")
    print("\nIn-order traversal of the tree:")
    printTreeNodes(tree)
    print()
