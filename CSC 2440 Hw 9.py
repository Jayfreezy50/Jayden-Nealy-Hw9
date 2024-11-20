# Jayden
class TreeNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

def inputNodes():
    root_value = int(input("Enter root node value: "))
    root = TreeNode(root_value)
    queue = [root]

    while queue:
        current = queue.pop(0)

        left_value = input(f"Enter left child of {current.value} (or 'None'): ")
        if left_value != 'None':
            current.left = TreeNode(int(left_value))
            queue.append(current.left)

        right_value = input(f"Enter right child of {current.value} (or 'None'): ")
        if right_value != 'None':
            current.right = TreeNode(int(right_value))
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
    total = node.value if node.value % 5 == 0 else 0
    return total + sumDivisibleByFive(node.left) + sumDivisibleByFive(node.right)

if __name__ == "__main__":
    tree = inputNodes()
    print(f"\nSum of values divisible by 5: {sumDivisibleByFive(tree)}")
    print("\nIn-order traversal of the tree:")
    printTreeNodes(tree)
    print()
