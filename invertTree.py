class InvertTree(object):
    def invertTree(self, root):
        # base case
        if root == None:
            return root
        # swaps
        root.left, root.right = root.right, root.left
        # call for left subtree
        self.invertTree(root.left)
        # call for right subtree
        self.invertTree(root.right)
        return root
