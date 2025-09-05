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

def s_o_b(root):
    if not root:
        return 0    
    else:
        return 1 + s_o_b(root.left) + s_o_b(root.right)
    
if __name__ == "__main__":
    root = insert()
    print("\n Size of a binary tree is: ",s_o_b(root))
    