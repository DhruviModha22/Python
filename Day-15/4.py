class Box:
    def __init__(self, items):
        self.items = items  # List of integers

    def __getitem__(self, index):
        return self.items[index]

    def __setitem__(self, index, value):
        self.items[index] = value

box = Box([1, 2, 3, 4, 5])
print(box[2])  # Output: 3
box[2] = 10
print(box[2])  # Output: 10
