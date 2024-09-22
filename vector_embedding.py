import os
from langchain_huggingface import HuggingFaceEmbeddings
from langchain_chroma import Chroma
from langchain_community.document_loaders import TextLoader
from langchain.text_splitter import CharacterTextSplitter

# Embeddings
embeddings = HuggingFaceEmbeddings(model_name="all-MiniLM-L6-V2")

# Vector Database
vector_db = Chroma(
    embedding_function=embeddings,
    collection_name="my_collection",
    persist_directory="./my_chroma_db"
)

def add_document_to_chroma(file_path):
    loader = TextLoader(file_path)
    documents = loader.load()

    # Split the document into chunks
    text_splitters = CharacterTextSplitter(chunk_size=1000, chunk_overlap=0)
    texts = text_splitters.split_documents(documents)

    # Add documents to Chroma DB
    vector_db.add_documents(texts)

    print(f"Added {len(texts)} text chunks from {file_path} to Chroma DB")


def main():
    while True:
        file_path = input("Enter the path to a text file (or 'q' to quit): ")
        if file_path.lower() == 'q':
            break
        if os.path.exists(file_path):
            add_document_to_chroma(file_path)
        else:
            print(f"File {file_path} not found.")


if __name__ == "__main__":
    main()