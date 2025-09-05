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
    print(f"Enter the left node {data}: ")
    node.left = insert()
    print(f"Enter the right node {data}: ")
    node.right = insert()
    return node

def inorder(root):
    if root:
        inorder(root.left)
        print(root.data, end=" ")
        inorder(root.right)

if __name__ == "__main__":
        root=insert()
        print("\nInorder traversal: ")
        inorder(root)