class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None
    
def insert():
    data = int(input("Enter the data (-1 for no node): "))
    if data == -1:
        return None
    
    node = Node(data)
    print(f"Enter the left node {data}: ")
    node.left = insert()
    print(f"Enter the right node {data}: ")
    node.right = insert()
    return node

def h_o_b(root):
    if not root:
        return 0
    return h_o_b(root.left) + h_o_b(root.right) + 1

if __name__ == "__main__":
    root = insert()
    print(f"The height of Binary Tree is: ", h_o_b(root))