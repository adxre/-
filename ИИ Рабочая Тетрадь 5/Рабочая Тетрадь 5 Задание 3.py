class Tree:
    def __init__(self, data):
        self.left = None
        self.right = None
        self.data = data

    def insert(self, value):
        if value < self.data:
            if self.left is None:
                self.left = Tree(value)
            else:
                self.left.insert(value)
        elif value > self.data:
            if self.right is None:
                self.right = Tree(value)
            else:
                self.right.insert(value)

    def print_tree(self):
        if self.left:
            self.left.print_tree()
        print(self.data)
        if self.right:
            self.right.print_tree()

# Пример использования:
root = Tree(10)
root.insert(5)
root.insert(15)
root.insert(3)
root.insert(7)
root.insert(12)
root.insert(18)

root.print_tree()
