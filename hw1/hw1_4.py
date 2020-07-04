import sys
class biTree:

    def __init__(self, data, left=None, right=None):
        self.data=data
        self.left=left
        self.right=right

    def preorder(self):
        print(self.data, end="\n")
        if self.left:
            self.left.preorder()
        if self.right:
            self.right.preorder()

    def inorder(self):
        if self.left:
            self.left.inorder()
        print(self.data, end="\n")
        if self.right:
            self.right.inorder()

    def postorder(self):
        if self.left:
            self.left.postorder()
        if self.right:
            self.right.postorder()
        print(self.data, end="\n")

BT = biTree(15,biTree(1,biTree(61,None,None),biTree(26,None,None)),
biTree(37,biTree(59,None,None),biTree(48,None,None)))

print("Preorder Traverse")
BT.preorder()
print("Inorder Traverse")
BT.inorder()
print("Postorder Traverse")
BT.postorder()