class Node:
    def __init__(self, data):
        self.left = None
        self.right = None
        self.data = data
        
def insert(node, data):
    if node is None:
        return Node(data)
    else:
        if data <= node.data:
            node.left = insert(node.left, data)
        else:
            node.right = insert(node.right, data)
    return node


def second_visit_traversal(root):
    if root is None:
        return
    
    second_visit_traversal(root.left)    
    print(root.data,end=" ")
    second_visit_traversal(root.right)


# 创建二叉搜索树
input_sequence = input("请输入一个由空格分隔的数字序列来构建二叉搜索树: ").split()
sequence = [int(num) for num in input_sequence]
root = None
for data in sequence:
    root = insert(root, data)
    

second_visit_traversal(root)