class BinarySearchTree:
    def __init__(self, name):
        self.name = name
        self.left = None
        self.right = None

    def insert(self, new_name):
        if new_name < self.name[0]:
            if not self.left:
                self.left = BinarySearchTree(new_name)
            else:
                # recursive to keep going until we find an empty spot
                self.left.insert(new_name)
        else:
            if not self.right:
                self.right = BinarySearchTree(new_name)
            else:
                self.right.insert(new_name)

    def contains(self, target):
        if target == self.name:
            return True
        if not self.left and not self.right:
            return False
        if self.left:
            if target < self.name:
                # we know to go left
                if not self.left:
                    return False
                else:
                    return self.left.contains(target)
            else:
                # we know to go right
                if not self.right:
                    return False
                else:
                    return self.right.contains(target)

    def get_max(self):
        if not self:
            return None
        if not self.right:
            return self.name
        else:
            return self.right.get_max()

    def for_each(self, cb):
        cb(self.name)

        if self.left:
            self.left.for_each(cb)
        if self.right:
            self.right.for_each(cb)
