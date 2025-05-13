from langchain.document_loaders.pdf import PyPDFDirectoryLoader


def load_pdf(path):
    loader = PyPDFDirectoryLoader(path)
    return loader.load()

def split_pdf(path):
    loader = PyPDFDirectoryLoader(path)
    return loader.load_and_split()

def create_propmt(chunks):
    flashcards = []
    for chunk in chunks:
        prompt = f"Question: {chunk.page_content}\nAnswer: "
        flashcards.append(prompt)
    return flashcards

def generate_flashcard(prompt):
    




    