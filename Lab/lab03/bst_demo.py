class node:
    def __init__(self,data=None,lchildNode = None, rchildNode = None, depth =None):
        self.data = data
        self.lchildNode= lchildNode
        self.rchildNode = rchildNode
        self.depth = depth

class binarySearchTree:
    def __init__(self, root= None):
        self.root = root

    def insertNode(self, inode):
        if( self.root == None):
            self.root = inode
            self.root.depth =0
        elif (inode.data < self.root.data):
            if(self.root.lchildNode == None):
                self.root.lchildNode = inode
                self.root.lchildNode.depth = self.root.depth + 1
            else:
                nextNode = binarySearchTree(self.root.lchildNode)
                nextNode.insertNode(inode)

        elif( inode.data > self.root.data ):
            if(self.root.rchildNode == None):
                self.root.rchildNode = inode
                self.root.rchildNode.depth = self.root.depth + 1
            else:
                nextNode = binarySearchTree(self.root.rchildNode)
                nextNode.insertNode(inode)

    def showBST(self):
        if(self.root.data != None):
            print(self.root.data, ", depth: ",self.root.depth)
        if(self.root.lchildNode != None):
            nextNode = binarySearchTree(self.root.lchildNode)
            nextNode.showBST()
        if (self.root.rchildNode != None):
            nextNode = binarySearchTree(self.root.rchildNode)
            nextNode.showBST()



    def findNode(self,data):
        if(self.root == None):
            print("not found")
            return False

        elif(self.root.data == data):
            print("The value(" , data ,") is found, depth : ",self.root.depth)
        elif ( self.root.data > data):
            nextNode = binarySearchTree(self.root.lchildNode)
            nextNode.findNode(data)
        elif ( self.root.data < data):
            nextNode = binarySearchTree(self.root.rchildNode)
            nextNode.findNode(data)
        else :
            print("not found")

        return False

def main():
    bst = binarySearchTree()
    while 1:
        print("1 :  Insert   2 : search    3 :  deletion  4 : End")
        x = int(input())
        if x == 1:
            print("Enter the insert key : ")
            i = int(input())
            bst.insertNode(node(i))
            bst.showBST()

        if x == 2:
            print("Enter the insert key : ")
            i = int(input())
            bst.findNode(i)

        if x == 3:
            print("Enter the Deletion key : ")
            i = int(input())
            #bst.deleteNode(i)
            #bst.showBST()
        if x == 4:
            break

main()
