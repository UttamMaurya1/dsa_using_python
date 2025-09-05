class Node:
    def __init__(self,data):
        self.data = data
        self.left = None
        self.right = None
        
def insert():
    data = int(input("Enter the data (-1 for no data): "))
    if data == -1:
        return
    node = Node(data)
    print(f"Enter the left node {data}: ")
    node.left =insert()
    print(f"Enter the right node {data}: ")
    node.right =insert()
    return node

def right_view(root, level, max_level):
    if root is None:
        return
    if level > max_level[0]:
        print(root.data, end=" ")
        max_level[0] = level
    right_view(root.right, level+1, max_level)
    right_view(root.left, level+1, max_level)
    
def right(root):
    max_level = [0]
    right_view(root, 1, max_level)
    
if __name__=="__main__":
    root =insert()
    print("\n The right view of BT is: ")
    right(root)
    