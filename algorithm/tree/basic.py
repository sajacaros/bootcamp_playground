class Travel:
    @staticmethod
    def travel_preorder(curr_node):
        if curr_node is None:
            return ''
        # print(curr_node.value)
        l = Travel.travel_preorder(curr_node.left_node)
        r = Travel.travel_preorder(curr_node.right_node)
        l_message = '' if l == '' else ' -> ' + l
        r_message = '' if r == '' else ' -> ' + r
        return curr_node.value + l_message + r_message

    @staticmethod
    def travel_inorder(curr_node):
        if curr_node is None:
            return ''
        l = Travel.travel_inorder(curr_node.left_node)
        r = Travel.travel_inorder(curr_node.right_node)
        l_message = '' if l == '' else l + ' -> '
        r_message = '' if r == '' else ' -> ' + r
        return l_message + curr_node.value + r_message

    @staticmethod
    def travel_postorder(curr_node):
        if curr_node is None:
            return ''
        l = Travel.travel_postorder(curr_node.left_node)
        r = Travel.travel_postorder(curr_node.right_node)
        l_message = '' if l == '' else l + ' -> '
        r_message = '' if r == '' else r + ' -> '
        return l_message + r_message + curr_node.value


class Tree:
    def __init__(self, value):
        self._value = value
        self._left_node = None
        self._right_node = None

    @property
    def value(self):
        return self._value

    @property
    def left_node(self):
        return self._left_node

    @property
    def right_node(self):
        return self._right_node

    @left_node.setter
    def left_node(self, node):
        self._left_node = node

    @right_node.setter
    def right_node(self, node):
        self._right_node = node


root = Tree('a')
n1 = Tree('b')
n2 = Tree('c')
n3 = Tree('d')
n4 = Tree('e')
n5 = Tree('f')
n6 = Tree('g')
n7 = Tree('h')
n8 = Tree('i')
n9 = Tree('j')

def print_tree():
    print('          a')
    print('    b             c')
    print(' d    e        f     g')
    print('     h          i   j')

root.left_node = n1
root.right_node = n2
n1.left_node = n3
n1.right_node = n4
n4.left_node = n7
n2.left_node = n5
n2.right_node = n6
n5.right_node = n8
n6.left_node = n9

print_tree()
print('-------- pre order --------')
print(Travel.travel_preorder(root))
print('-------- in order --------')
print(Travel.travel_inorder(root))
print('-------- post order --------')
print(Travel.travel_postorder(root))