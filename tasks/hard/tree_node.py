"""
Реализовать алгоритм двоичного дерево поиска

Бинарное дерево поиска (BST) — это дерево, в котором все узлы следуют указанным
ниже свойствам. Левое поддерево узла имеет ключ, меньший или равный ключу его
родительского узла. Правое поддерево узла имеет ключ больше, чем ключ его
родительского узла. Таким образом, BST делит все свои поддеревья на два сегмента:
левое поддерево и правое поддерево и может быть определено как -
left_subtree (keys)  ≤  node (key)  ≤  right_subtree (keys)


https://tproger.ru/translations/binary-search-tree-for-beginners/
"""


class Node:
    parent: "Node"
    left_child: "Node"
    right_child: "Node"
    value: int

    def __init__(self, value: int):
        self.parent = None
        self.left_child = None
        self.right_child = None
        self.value = value


class Tree:
    root: Node

    def __init__(self, root: Node = None):
        self.root = root

    def insert(self, node: Node) -> None:
        if self.root is None:
            self.root = node
        else:
            current_node = self.root
            while True:
                if node.value > current_node.value:
                    if current_node.right_child:
                        current_node = current_node.right_child
                    else:
                        current_node.right_child = node
                        node.parent = current_node
                        break
                else:
                    if current_node.left_child:
                        current_node = current_node.left_child
                    else:
                        current_node.left_child = node
                        node.parent = current_node
                        break
