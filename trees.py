class TreeNode:
    def __init__(self,key,val):
        self.key = key
        self.val = val
        self.balance_factor = 0
        self.parent = None
        self.left = None
        self.right = None

class Tree:

    def print(self):
        pass
    
    pass

class AVLTree(Tree):
    root = None

    def __init__(self,A):
        Tree.__init__(self)
        self.build_tree(A)

    def build_tree(self,A):
        for i in A:
            self.add(i)

    def add(self,key, val):
        self._put(self.root,key,val)

    def _put(self,node,key,val):
        if node is None:
            node = TreeNode(key,val)
        else:
            if key < node.key:
                if node.left:
                    self._put(node.left,key,val)
                else:
                    node.left = TreeNode(key,val)
                    node.left.parent = node
                    self.update_balancing(node.left.parent)
            else:
                if node.right:
                    self._put(node.right,key,val)
                else:
                    node.right = TreeNode(key,val)
                    node.right.parent = node
                    self.update_balancing(node.right.parent)

    def update_balancing(self, node,left):
        if node.balance_factor > 1 or node.balance_factor < -1:
            self.rebalance(node)
            return
        if node.parent != None:
            if left:
                node.parent.balance_factor += 1
            else:
                node.parent.balance_factor -= 1

            if node.parent.balanceFactor != 0:
                self.update_balancing(node.parent, True)


    def rebalance(self, node):



