class Node:
    def __init__(self,val):
        self.val = val

class Tree:
    def __init__(self):
        self.root = root

    def append(self,val):
        if self.root is none:
            self.root = Node(val)
            return
        self._append(node,val)

    def _append(self,node,val):
        if node.val>val:
            if node.left is None:
                node.left = Node(val)
            else:
                self._append(node.left,val)
        if node.val<val:
            if node.right is None:
                node.right = val
            else:
                self._append(node.right,val)

    def search(self,val):
        if self.root is None:
            return False
        
    def _search(self,node,val):
        if node is None:
            return 
        if node.val == val:
            return True
        if node.val>val:
            return _search(node.left,val)
        elif node.val<val:
            return _search(node.right,val)
    
    def pathsum(self,node,s):
        if node is None:
            return False
        s+=node.val
        if s==Targetsum and node.left is None and node.right is None:
            return True
        return (pathsum(node.left,s) or pathsum(node.right,s))
