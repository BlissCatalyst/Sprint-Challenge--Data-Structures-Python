class RingBuffer:
    def __init__(self, capacity):
        self.capacity = capacity
        self.current = 0
        self.storage = [None]*capacity

    def append(self, item):
        # Starts with the next oldest space, evaluates, then advances pointer to next space.
        # Pointer resets to 0 when pointer is greater than capacity.
        self.storage.pop(self.current)
        self.storage.insert(self.current, item)
        self.current += 1
        if self.current > self.capacity - 1:
            self.current = 0

    def get(self):
        # ** Does not affect self.storage **
        no_nones = []
        for item in self.storage:
            if item:
                no_nones.append(item)
        return no_nones
