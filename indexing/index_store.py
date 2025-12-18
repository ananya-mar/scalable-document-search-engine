from storage.serializer import save_object, load_object

def save_index(index, path="index.pkl"):
    save_object(index, path)

def load_index(path="index.pkl"):
    return load_object(path)
