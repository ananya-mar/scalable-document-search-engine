import os

def load_documents(folder_path):
    documents = {}
    doc_id = 0

    for filename in os.listdir(folder_path):
        if filename.endswith(".txt"):
            path = os.path.join(folder_path, filename)
            with open(path, "r", encoding="utf-8", errors="ignore") as f:
                documents[doc_id] = f.read()
                doc_id += 1

    return documents
