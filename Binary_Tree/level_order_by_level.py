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
    print(f"Ente the left node {data}: ")
    node.left = insert()
    print(f"Ente the right node {data}: ")
    node.right = insert()
    return node

def l_o_b_l(root):
    if not root:
        return
    
    q = [root]
    while q:
        level_size = len(q)
        for _ in range (level_size):
            current = q.pop(0)
            print(current.data, end=" ")
            if current.left:
                q.append(current.left)
            if current.right:
                q.append(current.right)
        print()        
            
if __name__ == "__main__":
    root = insert()
    print("\n Level Order By Level Traversal: ")
    l_o_b_l(root)
    