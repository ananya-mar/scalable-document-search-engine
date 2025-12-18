from preprocessing.tokenizer import tokenize
from ranking.tfidf import TFIDF

class QueryProcessor:
    def __init__(self, inverted_index, total_docs):
        self.index = inverted_index
        self.ranker = TFIDF(inverted_index, total_docs)

    def phrase_search(self, phrase_tokens):
        postings = [self.index.get_postings(t) for t in phrase_tokens]
        if not postings or any(not p for p in postings):
            return []

        common_docs = set(postings[0].keys())
        for p in postings[1:]:
            common_docs &= set(p.keys())

        results = {}
        for doc_id in common_docs:
            count = 0
            first_positions = postings[0][doc_id]

            for pos in first_positions:
                if all((pos + i) in postings[i][doc_id] for i in range(1, len(phrase_tokens))):
                    count += 1

            if count > 0:
                results[doc_id] = count

        return sorted(results.items(), key=lambda x: x[1], reverse=True)

    def search(self, query):
        query = query.strip()

        if query.startswith('"') and query.endswith('"'):
            phrase = query.strip('"')
            tokens = tokenize(phrase)
            return self.phrase_search(tokens)

        tokens = tokenize(query)
        return self.ranker.score(tokens)
