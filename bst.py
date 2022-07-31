class Node:
    def __init__(self, val):
        self.right = None
        self.left = None
        self.value = val


def insert_node(root, val):
    if root is None:
        return Node(val)
    else:
        if root.value > val:
            root.left = insert_node(root.left, val)
        else:
            root.right = insert_node(root.right, val)
        return root


def in_order(root):
    if root is None:
        return
    else:
        in_order(root.left)
        print(root.value, end=" ")
        in_order(root.right)


def pre_order(root):
    if root is None:
        return
    else:
        print(root.value, end=" ")
        pre_order(root.left)
        pre_order(root.right)


def post_order(root):
    if root is None:
        return
    else:
        post_order(root.left)
        post_order(root.right)
        print(root.value, end=" ")


def search_bst(root, val):
    if root is None or root.value == val:
        return root
    else:
        if root.value > val:
            return search_bst(root.left, val)
        else:
            return search_bst(root.right, val)


r = Node(5)
r = insert_node(r, 3)
r = insert_node(r, 1)
r = insert_node(r, 4)
r = insert_node(r, 9)
r = insert_node(r, 7)
print('in = ', end=' ')
in_order(r)
print('\npre = ', end=' ')
pre_order(r)
print('\npost = ', end=' ')
post_order(r)
s1 = search_bst(r, 3)
print('\nSearch Data =',s1.value)
