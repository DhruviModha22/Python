class Sentence:
    def __init__(self, text):
        self.text = text

    def __len__(self):
        return len(self.text.split())

s = Sentence("Hello world, this is Python.")
print(len(s))  # Output: 5
