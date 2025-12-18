import math

class TFIDF:
    def __init__(self, inverted_index, total_docs):
        self.index = inverted_index
        self.N = total_docs

    def score(self, query_terms):
        scores = {}

        for term in query_terms:
            postings = self.index.get_postings(term)
            if not postings:
                continue

            df = len(postings)
            idf = math.log((self.N + 1) / (df + 1)) + 1

            for doc_id, positions in postings.items():
                tf = len(positions) 
                scores.setdefault(doc_id, 0.0)
                scores[doc_id] += tf * idf

        return sorted(scores.items(), key=lambda x: x[1], reverse=True)
