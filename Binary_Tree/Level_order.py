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
    print(f"Enter the left child node {data}: ")
    node.left = insert()
    print(f"Enter the right child node {data}: ")
    node.right = insert()
    return node

def l_o(root):
    if not root:
        return
    
    q = [root]
    while q:
        current = q.pop(0)
        print(current.data, end=" ")
        
        if current.left:
            q.append(current.left)
        if current.right:
            q.append(current.right)
            
if __name__ == "__main__":
    root = insert()
    print("\n Level Order traversal: ")
    l_o(root)