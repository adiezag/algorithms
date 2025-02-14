def inOrderTraverse(tree, array):
    def traverse(tree):
        if tree == None:
            return
        if tree != None:
            traverse(tree.left)
            array.append(tree.value)
            traverse(tree.right)
        
    traverse(tree)
    return array
    


def preOrderTraverse(tree, array):
    # Write your code here.
    def traverse(tree):
        if tree == None:
            return
        if tree != None:
            array.append(tree.value)
            traverse(tree.left)
            traverse(tree.right)
        
    traverse(tree)
    return array


def postOrderTraverse(tree, array):
    # Write your code here.
    def traverse(tree):
        if tree == None:
            return
        if tree != None:
            traverse(tree.left)
            traverse(tree.right)
            array.append(tree.value)
        
    traverse(tree)
    return array
