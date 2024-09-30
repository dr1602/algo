class TreeNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

if __name__ == '__main__':
    from seven_binary_trees import TreeNode
    
    root = TreeNode(1)
    root.left = TreeNode(2)
    root.right = TreeNode(3)
    root.left.left = TreeNode(4)
    root.left.right = TreeNode(5)
    
    print(root)
    # <seven_binary_trees.TreeNode object at 0x7f7e2b01bf40>
    print(root.left)
    # <seven_binary_trees.TreeNode object at 0x7f7e2b01bee0>