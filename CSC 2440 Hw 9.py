class TreeNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

def input_tree_nodes():
    root_node = int(input("Enter the value for the root node: "))
    root = TreeNode(root_node)
    queue = [root]
    while queue:
        current = queue.pop(0)
        left_value = input(f"Enter the left child of {current.value} (or 'None' if no child): ")

        if left_value != 'None':
            left_value = int(left_value)
            current.left = TreeNode(left_value)
            queue.append(current.left)
        right_value = input(f"Enter the right child of {current.value} (or 'None' if no child): ")

        if right_value != 'None':
            right_value = int(right_value)
            current.right = TreeNode(right_value)
            queue.append(current.right)
    return root

def sum_divisible_values(root):
    if root is None:
        return 0
    total = 0
    if root.value % 5 == 0:
        total += root.value
    total += sum_divisible_values(root.left)
    total += sum_divisible_values(root.right)
    return total

def print_tree_nodes(root):
    if root is None:
        return
    print_tree_nodes(root.left)
    print(root.value, end=" ")
    print_tree_nodes(root.right)


if __name__ == "__main__":
    root = input_tree_nodes()
    sum_divisible = sum_divisible_values(root)
    print(f"The sum of values divisible by 5 is: {sum_divisible}")
    print("Tree values in order:")
    print_tree_nodes(root)

