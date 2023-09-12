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






root = Tree('root')
n1 = Tree('n1')
n2 = Tree('n2')
n3 = Tree('n3')
n4 = Tree('n4')
n5 = Tree('n5')
n6 = Tree('n6')
n7 = Tree('n7')
n8 = Tree('n8')
n9 = Tree('n9')

def print_tree():
    print('         root')
    print('    1             2')
    print(' 3    4        5     6')
    print('     7          8   9')

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