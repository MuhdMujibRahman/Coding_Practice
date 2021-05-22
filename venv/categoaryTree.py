class CategoryTree:

    def __init__(self):
        self.cateory = {}

    def add_category(self, category, parent):
        if parent is None:
            self.cateory[category] = {}
        else:
            self.cateory[parent] = {category}


    def get_children(self, parent):
        return self.category[parent]['child']
class Node:
    def __init__(self, value):
        self.children = []
        self.value = value

    def add_child(self, value):
        self.children.append(Node(value))

    def __repr__(self):
        classname = type(self).__name__
        return (f'{classname}({self.value!r}, {self.children})' if self.children else
                f'{classname}({self.value!r})')

    def print_stat(self):
        print(self.children)
        print(self.value)


class CategoryTree:
    def __init__(self):
        self.list_of_category = {}

    def add_category(self, category, parent=None):
        if not parent:
            list_of_category = category
            self.list_of_category[category] = Node(category)
        else:
            list_of_category = self.list_of_category.get(parent, None)
            if not list_of_category:
                raise KeyError(f'No continent named {parent} exists')
            list_of_category.add_child(category)

    def get_children(self, parent):
        child = []
        list_of_category = self.list_of_category.get(parent, None)
        if not continent:
            raise KeyError(f'No continent named {parent} exists')
        for eachNode in list_of_category.children:
            child.append(eachNode.value)
        return child

if __name__ == "__main__":
    c = CategoryTree()
    c.add_category('A', None)
    c.add_category('B', 'A')
    c.add_category('C', 'A')
    print(','.join(c.get_children('A') or []))