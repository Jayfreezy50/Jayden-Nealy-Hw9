#Jayden
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

        left_node = input(f"Enter left child of {current.value} (or 'none'): ")
        if left_node != 'none':
            current.left = TreeNode(int(left_node))
            queue.append(current.left)

        right_node = input(f"Enter right child of {current.value} (or 'none'): ")
        if right_node != 'none':
            current.right = TreeNode(int(right_node))
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
    node = inputNodes()
    print(f"\nSum of values divisible by 5: {sumDivisibleByFive(node)}")
    print("\nIn-order traversal of the tree:")
    printTreeNodes(node)
