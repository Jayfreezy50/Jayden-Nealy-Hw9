#Jayden
class TreeNode:
    def __init__(self, n):
        self.value = n
        self.left = None
        self.right = None

def InputNodes():
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

def PrintNodes(root):
    if root is None:
        return
    PrintNodes(root.left)
    print(root.value, end=" ")
    PrintNodes(root.right)

def DivisibleValues(root):
    if root is None:
        return 0
    return (root.value if root.value % 5 == 0 else 0) + DivisibleValues(root.left) + DivisibleValues(
        root.right)

if __name__ == "__main__":
    root = InputNodes()
    print(f"The sum of divisible values by 5 is: {DivisibleValues(root)}")
    print("Tree in order:")
    PrintNodes(root)

