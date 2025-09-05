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

def n_at_d(root, k):
    if not root:
        return None
    
    if k == 0:
        print(root.data, end=" ")
        return
    
    n_at_d(root.left, k-1)
    n_at_d(root.right, k-1)
    
if __name__ == "__main__":
    root = insert()
    k = int(input("\n Enter distance k: "))
    print("\n Node At Distance K: ")
    n_at_d(root, k)