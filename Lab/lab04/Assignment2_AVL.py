class Node():
    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None

class AVLTree:
    def __init__(self):
        self.node = None
        self.height = -1
        self.balance = 0

    def insert(self, key):
        tree = self.node
        newnode = Node(key)

        if tree == None:
            self.node = newnode
            self.node.left = AVLTree()
            self.node.right = AVLTree()
        elif key < tree.key:
            self.node.left.insert(key)
        elif key > tree.key:
            self.node.right.insert(key)
        else :
                print ("the key is already in tree")

        self.update()

    def update(self):
        self.update_height()
        self.update_balance()

        while self.balance <-1 or self.balance > 1 :
            if self.balance < -1:
                if self.node.right.balance > 0:
                    self.rlrotate()
                else:
                    self.llrotate()

            if self.balance > 1:
                if self.node.left.balance < 0:
                    self.lrrotate()
                else:
                    self.rrotate()

            self.update_height()
            self.update_balance()

    def lrrotate(self):
        self.node.left.llrotate()
        self.rrotate()


    def rlrotate(self):
        self.node.right.rrotate()
        self.llrotate()

    def rrotate(self):

        A = self.node
        B = A.left.node
        T = B.right.node

        self.node = B
        B.right.node = A
        A.left.node = T

    def llrotate(self):

        A = self.node # old_root
        B = A.right.node #new_root
        T = B.left.node # new_left_sub

        self.node = B
        A.right.node = T
        B.left.node = A

    def update_height(self):
        if not self.node == None:
            if self.node.left != None:
                self.node.left.update_height()
            if self.node.right != None :
                self.node.right.update_height()

            self.height = max (self.node.left.height, self.node.right.height)+1
        else :
            self.height=-1


    def update_balance(self):
        if not self.node == None:
            if self.node.left != None:
                self.node.left.update_balance()
            if self.node.right != None :
                self.node.right.update_balance()

            self.balance = self.node.left.height - self.node.right.height
        else :
            self.balance=0

    def display(self, level=0, pref=''):
        if (self.node != None):
            print('-' * level * 2, pref, self.node.key, "[" + str(self.height) + ":" + str(self.balance) + "]")
            if self.node.left != None:
                self.node.left.display(level + 1, '<')
            if self.node.right != None:
                self.node.right.display(level + 1, '>')



# main
avl_tree = AVLTree()

while(True):
    insert_key = int(input("Input key : "))
    if(insert_key == 0):
        break

    avl_tree.insert(insert_key)
    avl_tree.display()

