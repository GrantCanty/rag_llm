# RAG AI Chatbot  
This is a RAG AI Chatbot that can answer questions related to Ferrari's recent financial results.  

## General flow of the RAG pipeline:  
1. Import a news article of Ferrari's recent financial results, split the article into chunks, embed each chunk using an encoder, and store them in a vector DB (ChromaDB)  
2. Take a prompt from the user, embed it, and return the most similar embedding stored in the vector DB  
3. Pass a query to an LLM containing the prompt as a question and recently returned embedings from the vector DB as content  
4. Return the results of the query to the front end  

## Tips to run the project
This project users Docker to ensure minimal compatability issues between machines. Ensure that Docker is installed. It does take a while to build the Docker image and have it running  

Create a .`env` file in the `backend` folder before running. It should have the following fields:  

.env   
`EMBEDDING_MODEL=sentence-transformers/all-MiniLM-L6-v2`   

Follow these steps to run the project:  
1. Open your command line  
2. Clone the github repo to your local machine  
3. Clone repo of Qwen3 to local machine using the following command: `git clone https://huggingface.co/Qwen/Qwen3-0.6B qwen_model`. 
4. Ensure that model has properly imported. Inspect the `tokenizer.json` file inside the `qwen_model` folder  
  4.1 If the file starts with something like `{"version": 1.0 ...}`, it has imported correctly  
  4.2 If you see a link, it has not imported correctly. You may need to install `git lfs install` before you clone the model again  
5. Ensure that Docker is running  
6. Enter `docker compose up --build -d` to build and run the Docker file  
7. Open your browser and visit `localhost:8501` to interact with the chat bot  
8. To close the system, enter `docker compose down`  
