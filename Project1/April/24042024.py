class Node:
    def __init__(self, val):
        self.val = val
        self.right = None
        self.left = None

class Tree:
    def __init__(self):
        self.root = None
    
    def append(self, val):
        if self.root is None:
            self.root = Node(val)
        else:
            self._append(self.root, val)

    def _append(self, node, val):
        if node.val > val:
            if node.left is None:
                node.left = Node(val)
            else:
                self._append(node.left, val)
        elif node.val < val:
            if node.right is None:
                node.right = Node(val)
            else:
                self._append(node.right, val)
        # If node.val == val, we don't insert it to avoid duplicates

    def search(self, val):
        return self._search(self.root, val)

    def _search(self, node, val):
        if node is None:
            return False
        elif node.val == val:
            return True
        elif node.val > val:
            return self._search(node.left, val)
        else:
            return self._search(node.right, val)

    def preorder(self):
        if self.root is None:
            return False
        else:
            arr=[]
            return self._preorder(self.root,arr)
    def _preorder(self,node,arr):
        if node:
            arr.append(node.val)
        else:
            return 
        self._preorder(node.left,arr)
        self._preorder(node.right,arr)
        return arr

    def postorder(self):
        if self.root is None:
            return False
        else:
            arr=[]
            return self._postorder(self.root,arr)
    
    def _postorder(self,node,arr):
        if not node:
            return
        self._postorder(node.left,arr)
        self._postorder(node.right,arr)
        arr.append(node.val)
        return arr

    def inorder(self):
        if self.root is None:
            return False
        else:
            arr=[]
            return self._inorder(self.root,arr)

    def _inorder(self,node,arr):
        if not node:
            return False
        self._inorder(node.left,arr)
        arr.append(node.val)
        self._inorder(node.right,arr)    
    
    def levelorder(self):
        if self.root is None:
            return False
        else:
            arr=[]
            return self._levelorder(self.root,arr)

    def _levelorder(self,node,arr):
        curr= node
        queue = []
        queue.append(curr)
        while queue:
            popped = queue.pop(0)
            arr.append(popped.val)
            if popped.left:
                queue.append(popped.left)
            if popped.right:
                queue.append(popped.right)
        
        return arr

    def diameter(self):
        if self.root is None:
            return False
        else:
            arr=[]
            return self.__diameter(self.root,arr)

    def __diameter(self,node,arr):
        curr= node
        queue = []
        queue.append(curr.val)
        while queue:
            arr.append(queue)
            for i in queue:
                queue.pop(0)
                if i.left:
                    queue.append(i.left)
                if i.right:
                    queue.append(i.right)
            
        
        return arr


    
# Example usage
tree = Tree()
tree.append(10)
tree.append(5)
tree.append(15)
print(tree.search(10))  # True
print(tree.search(5))   # True
print(tree.search(15))  # True
print(tree.search(20))  # False
# print(tree.preorder())
# print(tree.postorder())
print(tree.diameter())