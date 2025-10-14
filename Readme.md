# RAG AI Chatbot  
This is a RAG AI Chatbot that can answer questions related to Ferrari's recent financial results.  

## General flow of the RAG pipeline:  
1. Import a news article of Ferrari's recent financial results, split the article into chunks, embed each chunk using an encoder, and store them in a vector DB (ChromaDB)  
2. Take a prompt from the user, embed it, and return the most similar embedding stored in the vector DB  
3. Pass a query to an LLM containing the prompt as a question and recently returned embedings from the vector DB as content  
4. Return the results of the query to the front end  

## Tips to run the project
This project users Docker to ensure minimal compatability issues between machines. Ensure that Docker is installed. It does take a while to build the Docker image and have it running    

Follow these steps to run the project:  
1. Open your command line  
2. Clone the github repo to your local machine  
3. Ensure that Docker is running  
4. Enter `docker built -t rag-llm .` to build the Docker file  
5. Enter `docker run -p 8501:8501 rag-llm` to run the image  
6. Open your browser and visit `localhost:8501` to interact with the chat bot  

