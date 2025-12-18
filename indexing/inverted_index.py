from collections import defaultdict

def postings_dict():
    return defaultdict(list)

class InvertedIndex:
    def __init__(self):
        # word -> {doc_id: [positions]}
        self.index = defaultdict(postings_dict)
        self.doc_lengths = {}

    def add_document(self, doc_id, tokens):
        self.doc_lengths[doc_id] = len(tokens)
        for pos, word in enumerate(tokens):
            self.index[word][doc_id].append(pos)

    def get_postings(self, word):
        return self.index.get(word, {})
