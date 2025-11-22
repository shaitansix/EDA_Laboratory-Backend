# 🔬 EDA Laboratory
*Interactive platform for performing Exploratory Data Analysis (EDA) using modern frontend and backend technologies.*

---
## 🚀 Quick Setup Guide

### 1. Create a folder for the project and open cmd in this folder

### 2. Clone the Repository
```bash
git clone https://github.com/shaitansix/EDA_Laboratory-Backend.git
cd EDA_Laboratory-Backend
```

### 3. Create and activate a virtual environment
```bash
pip install virtualenv
virtualenv venv
.\venv\Scripts\activate # Windows
```

### 4. Install dependencies
```bash
pip install -r requirements.txt
```

### 5. Configure environment variables: 
**Create an account on [Ollama](https://ollama.com)**  
**Add an API key to your account**  
**Create an .env file in the EDA_Laboratory-Backend folder**  
**Create an environment variable called "OLLAMA_API_KEY" with the API Key obtained from ollama**
```bash
OLLAMA_API_KEY=<your API Key>
```

### 6. Run the FastAPI server; you can use any of the following commands
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