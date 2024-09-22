import os
from langchain_groq import ChatGroq
from langchain.memory import ConversationBufferMemory
from langchain_huggingface import HuggingFaceEmbeddings
from langchain_chroma import Chroma
from langchain.retrievers import ContextualCompressionRetriever
from langchain.prompts import ChatPromptTemplate
from langchain.retrievers.document_compressors import LLMChainExtractor
from langchain.chains import ConversationalRetrievalChain

from dotenv import load_dotenv
load_dotenv()

os.environ['GROQ_API_KEY'] = os.getenv("GROQ_API_KEY")
groq_api_key=os.getenv("GROQ_API_KEY")

os.environ['HF_TOKEN'] = os.getenv("HF_TOKEN")


# Initialize the LLM
llm = ChatGroq(groq_api_key=groq_api_key, model='Llama3-8b-8192', temperature=0.7, max_tokens=500)


# Initialize memory for conversation
memory = ConversationBufferMemory(memory_key='chat_history', return_messages=True)

# Create embedding model
embeddings=HuggingFaceEmbeddings(model_name="all-MiniLM-L6-V2")

# Initialize the Chroma DB (Vector Database)
vector_db = Chroma(embedding_function=embeddings, collection_name='my_collection', persist_directory='./my_chroma_db')

# Create a ContextualCompressionRetriever
retriever = ContextualCompressionRetriever(
    base_compressor = LLMChainExtractor.from_llm(llm),
    base_retriever = vector_db.as_retriever()
)

# Creating a template for combining the memory, database, and LLM
prompt = ChatPromptTemplate.from_template(
    """
    Context: {context},
    Chat History: {chat_history},
    Human: {question},
    AI: Please provide a detailed, informative answer based on the context and chat history. Elaborate on key points, include examples if relevant, and avoid prefacing the response with phrases like "Based on the context and chat history." Aim for clarity and depth in your response.
    """
)




# Create the ConversationRetrievalChain
conversation_chain = ConversationalRetrievalChain.from_llm(
    llm=llm,
    retriever=retriever,
    memory=memory,
    combine_docs_chain_kwargs = {'prompt':prompt}
)



def chatbot_response(user_input):
    return conversation_chain({"question": user_input})['answer']