from collections import deque
class Node:
    def __init__(self,data):
        self.data= data
        self.left= None
        self.right= None

def insert():
    data = int(input("Enter the data (-1 for no node): "))
    if data == -1:
        return None
    node = None(data)
    print(f"Enter the left Node {data}: ")
    node.left = insert()
    print(f"Enter the right Node {data}: ")
    node.right = insert()
    return node

def top_view(root):
    if root is None:
        return
    # bounce 