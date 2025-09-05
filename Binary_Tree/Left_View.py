class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None
        
def insert():
    data = int(input("Enter the data (-1) for no node: "))
    if data == -1:
        return
    node = Node(data)
    print(f"Enter the left node {data}: ")
    node.left = insert()
    print(f"Enter the right node {data}: ")
    node.right = insert()
    return node

def left_view(root, level, max_level):
    if root is None:
        return
    if level > max_level[0]:
        print(root.data, end=" ")
        max_level[0]= level
    left_view(root.left, level+1, max_level)    
    left_view(root.right, level+1, max_level)
    
def left(root):
    max_level = [0]
    left_view(root, 1, max_level)
    
if __name__ == "__main__":    
    root = insert()
    print("\n The left view of BT is: ")
    left(root)