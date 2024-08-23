class Node:
    def __init__(self, val):
        self.val = val
        self.right = None
        self.left = None

class Tree:
    def __init__(self, root=None):
        self.root = root
    
    def append(self, val):
        if self.root is None:
            self.root = Node(val)
        else:
            self.recAppend(val, self.root)
    
    def recAppend(self, val, node):
        if node.val > val:
            if node.left is None:
                node.left = Node(val)
            else:
                self.recAppend(val, node.left)
        elif node.val < val:
            if node.right is None:
                node.right = Node(val)
            else:
                self.recAppend(val, node.right)

    def search(self, val):
        return self.recsearch(self.root, val)

    def recsearch(self, node, val):
        if node is None:
            return -1
        elif node.val == val:
            return 1
        elif node.val > val:
            return self.recsearch(node.left, val)
        elif node.val < val:
            return self.recsearch(node.right, val)

    def preorder(self, node):
        if node:
            print(node.val)
            self.preorder(node.left)
            self.preorder(node.right)

    def postorder(self, node):
        if node:
            self.postorder(node.left)
            self.postorder(node.right)
            print(node.val)

    def inorder(self, node):
        if node:
            self.inorder(node.left)
            print(node.val)
            self.inorder(node.right)

    def levelorder(self):
        if not self.root:
            return []
        queue = [self.root]
        arr = []
        self.LL(queue, arr)
        return arr
    
    def LL(self, queue, arr):
        while queue:
            node = queue.pop(0)
            arr.append(node.val)
            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)

# Usage example
if __name__ == "__main__":
    t = Tree()
    t.append(10)
    t.append(5)
    t.append(15)
    t.append(3)
    t.append(7)
    t.append(12)
    t.append(18)
    print("Level order traversal:")
    print(t.levelorder())  # Output the level order traversal

## Maximum depth in Binary tree
def Maxdepth(self):
    curr = self.root
    val=0
    return MD(self,node,val)

def MD (self,node,val):
    if node.left:
        m1 = MD(node.left,val+1)
    else:
        m1=0
    if node.right:
        m2 = MD(node.right,val+1)
    else:
        m2 = 0
    return max(m1,m2)
 