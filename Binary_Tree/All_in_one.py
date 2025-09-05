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
    print(f"Enter the left {data}: ")
    node.left = insert()
    print(f"Enter the Right {data}: ")
    node.right = insert()
    return node

def preorder(root):
    if root:
        print(root.data, end=" ")
        preorder(root.left)
        preorder(root.right)

def inorder(root):
    if root:
        inorder(root.left)
        print(root.data, end=" ")
        inorder(root.right)

def postorder(root):
    if root:
        postorder(root.left)
        postorder(root.right)
        print(root.data, end=" ")
        
def l_o(root):
    if not root:
        return
    
    q= [root]
    while q:
        current = q.pop(0)
        print(current.data, end=" ")
        if current.left:
            q.append(current.left)
        if current.right:
            q.append(current.right)

def l_o_b_l(root):
    if not root:
        return
    q = [root]
    while q:
        level_size = len(q)
        for _ in range(level_size):
            current = q.pop(0)
            print(current.data, end=" ")
            if current.left:
                q.append(current.left)
            if current.right:
                q.append(current.right)
        print()
        
if __name__ == "__main__":
    root = insert()
    print("\n Preorder Traversal: ")
    preorder(root)    
    print("\n Inorder Traversal: ")
    inorder(root)    
    print("\n Postorder Traversal:")
    postorder(root) 
    print("\n Order By Traverssal: ") 
    l_o(root)  
    print("\n Level Order By Level Traversal: ")
    l_o_b_l(root)

