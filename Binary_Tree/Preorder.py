class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

def insert():
    data = int(input("Enter data (-1 for no node): "))
    if data == -1:
        return None
    
    node = Node(data)
    print(f"Enter the left node{data}: ")
    node.left = insert()
    print(f"Enter the right node{data}: ")
    node.right = insert()
    return node

def preorder(root):
    if root:
        print(root.data, end=" ")
        preorder(root.left)
        preorder(root.right)
    
if __name__ == "__main__":
    root = insert()
    print("\n Preorder Traverse: ")
    preorder(root) 
    