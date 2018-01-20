class Node():
    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None

class AVLTree:
    def __init__(self):
        self.node = None
        self.height = -1
        self.balance = 0 #회전 여부

    def insert(self, key):
        tree = self.node
        newnode = Node(key)

        if tree == None:
            self.node = newnode
            self.node.left = AVLTree()
            self.node.right = AVLTree()

        elif tree.key > key:
            self.node.left.insert(key)
            self.node.left
        elif tree.key < key:
            self.node.right.insert(key)
        else:
            print("The key is already in tree")

        self.update()

    def update(self):
        self.update_heights()
        self.update_balance()

        while self.balance < -1 or self.balance > 1:
            if self.balance < -1 :
                self.lrotate()
                self.update_heights()
                self.update_balance()
            if self.balance > 1:
                self.rrotate()
                self.update_heights()
                self.update_balance()

    def lrotate(self):
        print("lrotate")


    def rrotate(self):
        A = self.node  # current node
        B = self.node.left.node  # left child
        T = B.right.node

        self.node = B
        B.right.node = A
        A.left.node = T

    def update_heights(self):
        if not self.node == None:
            if self.node.left != None:
                self.node.left.update_heights()
            if self.node.right != None:
                self.node.right.update_heights()
            self.height = max(self.node.left.height,self.node.right.height) + 1
        else:
            self.height = 0

    def update_balance(self):
        if not self.node == None:
            if self.node.left != None:
                self.node.left.update_balance()
            if self.node.right != None:
                self.node.right.update_balance()
            self.balance = self.node.left.height - self.node.right.height
        else:
            self.balance = 0
    def display(self, level=0, pref=''):
        if (self.node != None):
            print('-' * level * 2, pref, self.node.key, "[" + str(self.height) + ":" + str(self.balance) + "]")
            if self.node.left != None:
                self.node.left.display(level + 1, '<')
            if self.node.right != None:
                self.node.right.display(level + 1, '>')




# main
avl_tree = AVLTree()
print("----- Inserting -------")
inlist = [3, 2, 1]
for i in inlist:
    avl_tree.insert(i)
avl_tree.display()
