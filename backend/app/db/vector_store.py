class VectorStore:
    def __init__(self):
        self.data = []

    def add(self, doc):
        self.data.append(doc)

    def search(self, query):
        return self.data[:2]