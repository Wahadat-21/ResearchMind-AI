import chromadb

class MemoryStore:

    def __init__(self):

        self.client = chromadb.Client()
        self.collection = self.client.create_collection(
            name="research_memory"
        )

    def save(self, topic, text):

        self.collection.add(
            documents=[text],
            ids=[topic]
        )

    def retrieve(self, topic):

        return self.collection.get(ids=[topic])
