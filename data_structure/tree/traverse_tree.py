class Node : 
    def __init__(self, data) :
        self.data = data
        self.left_child = None
        self.right_child = None
    

root_node = Node(1)
node1 = Node(3)
node2 = Node(5)
node3 = Node(7)
node4 = Node(9)
node5 = Node(11)

root_node.left_child = node1
root_node.right_child = node2

node1.left_child = node3
node1.right_child = node4

node2.left_child = node5


def traverse_preorder(node) :
    if node is not None :
        print(node.data)
        traverse_preorder(node.left_child)
        traverse_preorder(node.right_child)

traverse_preorder(root_node)
print()

def traverse_postorder(node) :
    if node is not None :
        traverse_preorder(node.left_child)
        traverse_preorder(node.right_child)
        print(node.data)

traverse_postorder(root_node)
print()

def traverse_inorder(node) :
    if node is not None :
        traverse_preorder(node.left_child)
        print(node.data)
        traverse_preorder(node.right_child)

traverse_inorder(root_node)
