from langchain.document_loaders.pdf import PyPDFDirectoryLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter


class Speratetext:
    def __init__(self, filepath):
        self.filepath = filepath
        self.

    def run(self):
        self.model.load_data()
        self.view.show_data(self.model.data)
    
        
    def load_pdf(self, filepath):
        # load pdf 
        document_loader = PyPDFDirectoryLoader(filepath)
        return document_loader.load()

    def pdf_to_chucks(self):
            text_splitter = RecursiveCharacterTextSplitter(
            chunk_size=800,
            chunk_overlap=80,
            length_function=len,
            is_separator_regex=False,
            )
        return text_splitter.split_documents(documents)

    def 
    

