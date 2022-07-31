class TreeNode:
    def __init__(self, name, desig):
        self.name = name
        self.desig = desig
        self.parent = None
        self.children = []

    def add_child(self, child):
        self.children.append(child)
        child.parent = self

    def get_level(self):
        level = 0
        p = self.parent
        while p:
            level += 1
            p = p.parent
        return level

    def print_tree(self, type):
        prefix = ' ' * self.get_level() * 2
        if type == 'name':
            prt = self.name
        elif type == 'desig':
            prt = self.desig
        elif type == 'both':
            prt = f"{self.name} ( {self.desig} )"
        print(prefix + prt)
        if self.children:
            for i in self.children:
                i.print_tree(type)

    def print_tree(self, level=100, type='both'):
        prefix = ' ' * self.get_level() * 2
        if type == 'name':
            prt = self.name
        elif type == 'desig':
            prt = self.desig
        elif type == 'both':
            prt = f"{self.name} ( {self.desig} )"
        print(prefix + prt)
        if self.children and int(level) > 0:
            for i in self.children:
                i.print_tree(level-1)


def make_tree():
    root = TreeNode('xyz', 'CEO')

    a1 = TreeNode('abc', "CTO")
    a1.add_child(TreeNode("abc1", "Designer"))
    a21 = TreeNode("abc2", "Developer")
    a21.add_child( TreeNode( 'abc21',"Junior Dev"))
    a21.add_child( TreeNode( 'abc22',"Junior Dev"))
    a1.add_child(a21)
    a1.add_child(TreeNode("abc3", "Developer"))

    b1 = TreeNode('pqr', "CFO")
    b1.add_child(TreeNode("pqr1", 'BDM'))
    b1.add_child(TreeNode("pqr2", 'BDM'))
    b1.add_child(TreeNode("pqr3", 'BDM'))

    root.add_child(a1)
    root.add_child(b1)

    return root


if __name__ == "__main__":
    root = make_tree()
    root.print_tree(2, 'both') # level , type
    # "name" , "desig" , "both"

# LINKS https://www.youtube.com/watch?v=4r_XR9fUPhQ
