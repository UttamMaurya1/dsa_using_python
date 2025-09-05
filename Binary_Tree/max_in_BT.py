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

def find_max(root):
    if root is None:
        return float('-inf') 
    return max(root.data, find_max(root.left), find_max(root.right))

if __name__ == "__main__":
    root = insert()
    print("\n Maximum of BT is: ", find_max(root))