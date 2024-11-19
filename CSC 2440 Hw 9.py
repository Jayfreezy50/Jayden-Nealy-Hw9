class TreeNode:
    def __init__(self, n):
        self.value = n
        self.left = None
        self.right = None

def input_tree_nodes():
    root_node = int(input("Enter the value for the root node: "))
    root = TreeNode(root_node)
    queue = [root]

    while queue:
        current = queue.pop(0)
        left_node = input(f"Enter the left child of {current.value} ('None' if no child): ")

        if left_node != 'None':
            left_node = int(left_node)
            current.left = TreeNode(left_node)
            queue.append(current.left)

        right_node = input(f"Enter the right child of {current.value} ('None' if no child): ")

        if right_node != 'None':
            right_node = int(right_node)
            current.right = TreeNode(right_node)
            queue.append(current.right)
    return root

def print_tree_nodes(root):
    if root is None:
        return
    print_tree_nodes(root.left)
    print(root.value, end=" ")
    print_tree_nodes(root.right)

def sum_divisible_values(root):
    if root is None:
        return 0
    return (root.value if root.value % 5 == 0 else 0) + sum_divisible_values(root.left) + sum_divisible_values(
        root.right)

if __name__ == "__main__":
    root = input_tree_nodes()
    print(f"The sum of values divisible by 5 is: {sum_divisible_values(root)}")
    print("Tree values in order:")
    print_tree_nodes(root)



