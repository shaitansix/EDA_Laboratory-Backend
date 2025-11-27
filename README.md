# 🔬 EDA Laboratory
*Interactive platform for performing Exploratory Data Analysis (EDA) using modern frontend and backend technologies.*

---
## 🚀 Quick Setup Guide

## Using docker

### 1. Configure Ollama: 
**Create an account on [Ollama](https://ollama.com)**  
**Add an API key to your account**

### 2. Download the Docker Hub image
```bash
docker pull shaitansix/eda_laboratory-api:1
```

### 3. Create a Docker container and then initialize it
```bash
docker run --name eda_laboratory-api -e OLLAMA_API_KEY=<your API Key> -e CORS_ORIGINS=http://localhost:5173,http://localhost:5173/,http://localhost:4173,http://localhost:4173/ -p 8000:8000 shaitansix/eda_laboratory-api:1
```

*✔️ Backend available at:
http://localhost:8000/  
✔️ Documentation available at:
http://localhost:8000/docs*

## Using Node Js

### 1. Configure Ollama: 
**Create an account on [Ollama](https://ollama.com)**  
**Add an API key to your account**

### 2. Create a folder for the project and open cmd in this folder

### 3. Clone the Repository
```bash
git clone https://github.com/shaitansix/EDA_Laboratory-Backend.git
```

### 4. Create and activate a virtual environment
```bash
pip install virtualenv
virtualenv venv
.\venv\Scripts\activate # Windows
```

### 5. Install dependencies
```bash
cd EDA_Laboratory-Backend
pip install -r requirements.txt
```

### 6. Configure environment variables: 
**Create an .env.dev file in the EDA_Laboratory-Backend folder**  
**Create an environment variable called "OLLAMA_API_KEY" with the API Key obtained from ollama**
```bash
OLLAMA_API_KEY=<your API Key>
```
**Copy the following environment variable into the .env.dev file**
```bash
CORS_ORIGINS=http://localhost:5173,http://localhost:5173/,http://localhost:4173,http://localhost:4173/
```

### 7. Create a folder called "data" in the EDA_Laboratory-Backend folder

### 8. Run the FastAPI server; you can use any of the following commands
**Using uvicorn**
```bash
uvicorn main:app --reload
```
**Using fastapi**
```bash
fastapi dev main.py
```

*✔️ Backend available at:
http://localhost:8000/  
✔️ Documentation available at:
http://localhost:8000/docs*