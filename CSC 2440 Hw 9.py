#Jayden
class TreeNode:
    def __init__(self, n):
        self.value = n
        self.left = None
        self.right = None

def inputNodes():
    root_node = int(input("Enter value for root node: "))
    root = TreeNode(root_node)
    queue = [root]

    while queue:
        current = queue.pop(0)
        leftNode = input(f"Enter value to the left child of {current.value} (Type 'None' if no child): ")

        if leftNode != 'None':
            leftNode = int(leftNode)
            current.left = TreeNode(leftNode)
            queue.append(current.left)

        rightNode = input(f"Enter value to the right child of {current.value} ('None' if no child): ")

        if rightNode != 'None':
            rightNode = int(rightNode)
            current.right = TreeNode(rightNode)
            queue.append(current.right)
    return root

def printTreeNodes(node):
    if node is None:
        return
    printTreeNodes(node.left)
    print(node.value, end=" ")
    printTReeNodes(node.right)

def divisibleValues(root):
    if root is None:
        return 0
    return (root.value if root.value % 5 == 0 else 0) + divisibleValues(root.left) + divisibleValues(
        root.right)

if __name__ == "__main__":
    root = inputNodes()
    print(f"The sum of divisible values by 5 is: {divisibleValues(root)}")
    print("Tree in order:")
    printNodes(root)

