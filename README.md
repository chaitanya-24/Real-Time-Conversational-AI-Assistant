# AI Conversational Assistant with Flask, LangChain, and Streamlit

An interactive AI-powered chatbot that uses LangChain to integrate large language models, Flask for the backend, and Streamlit for the frontend. The chatbot allows dynamic, context-aware conversations and uses ChromaDB for efficient document storage and retrieval.

## Features

- **Real-time AI Chat**: Engage in real-time conversations with an AI model powered by LangChain.
- **Contextual Memory**: The chatbot remembers previous exchanges in the conversation, creating a natural and dynamic dialogue.
- **Interactive Frontend**: A clean, user-friendly interface built with Streamlit for seamless interaction.
- **Efficient Document Retrieval**: Utilizes ChromaDB to retrieve relevant documents during conversations.
- **Scalable Backend**: Flask-based backend to handle user requests and communicate with the AI model.

## Technologies Used

- **Flask**: Backend framework to handle requests and manage the chatbot logic.
- **LangChain**: For integrating the large language models (LLMs) and managing contextual chat.
- **Streamlit**: Used to create an interactive frontend for real-time chatbot conversations.
- **ChromaDB**: Vector database for document storage and retrieval.
- **HuggingFace**: Embeddings model for natural language understanding.
- **LLMs**: Utilized models like `Llama3-8b-8192` via Groq API for generating human-like responses.


## Folder Structure

```
.
├── data
  ├── data.txt               # Custom data                   
├── app.py                   # Flask backend
├── chatbot.py               # Chatbot logic using LangChain and ChromaDB
├── chatbot_ui.py            # Streamlit frontend interface
├── vector_embedding.py      # Script for adding documents to ChromaDB
├── requirements.txt         # Python dependencies
├── .env                     # Environment variables
└── README.md                # Project documentation
```


## Installation and Setup

### Prerequisites

- Python 3.8 or higher
- Pip (Python package manager)

### 1. Clone the Repository

```bash
git clone https://github.com/your-username/ai-conversational-assistant.git
cd ai-conversational-assistant
```

### 2. Set Up a Virtual Environment

```bash
python -m venv venv
source venv/bin/activate   # On Windows: venv\Scripts\activate
```

### 3. Install the Required Packages

```bash
pip install -r requirements.txt
```

### 4. Set Up Environment Variables

Create a `.env` file in the root directory and add the necessary environment variables:

```
GROQ_API_KEY=your_groq_api_key
HF_TOKEN=your_huggingface_token
```

### 5. Start the Flask Backend

Run the Flask server that will handle chatbot requests:

```bash
python app.py
```

### 6. Convert Text into Vectors and Store in ChromaDB

Run the `vector_embedding.py` script to convert your text data into vectors and store them in ChromaDB. You'll need to provide the file path of the text document(s):

```bash
python vector_embedding.py
```

You will be prompted to enter the path to a text file, which will then be processed and stored in the Chroma vector database.

Example:

```
Enter the path to a text file (or 'q' to quit): ./data/sample_text.txt
Added 10 text chunks from ./data/sample_text.txt to Chroma DB
```

### 7. Start the Streamlit Frontend

Open a new terminal, activate the virtual environment, and start the Streamlit app for the frontend interface:

```bash
streamlit run chatbot_ui.py
```

### 8. Interact with the Chatbot

Open your browser and navigate to the Streamlit app (usually at `http://localhost:8501`). Start chatting with the AI-powered assistant!

## Usage

1. **Start a conversation**: Type your message in the Streamlit interface, and the chatbot will respond based on context and the current conversation.
2. **Add documents to ChromaDB**: Use the `vector_embedding.py` script to add documents to the vector database for enhanced contextual retrieval.

[Video](https://github.com/user-attachments/assets/69f6fed3-51da-424c-9bfb-643151ae4d43)


## Future Enhancements

- **Support for Multiple LLMs**: Integrate more language models to improve the quality and scope of the chatbot’s responses.
- **Advanced UI**: Further refine the user interface for a more engaging experience.
- **Additional Features**: Add functionalities like speech-to-text and more customizable conversation flows.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
