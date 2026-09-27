# Task Manager

A full-stack task management app — React frontend, FastAPI backend, PostgreSQL database.

## Project Structure

task-management/
├── backend/ # FastAPI REST API (PyCharm project)

└── frontend/ # React + Vite app (VS Code project)


## Features

- Register / Login / Logout (session-based auth)
- Create, view, edit, and delete tasks
- Mark a task as completed
- Shows the date a task was created



## Backend Setup

1. Go to the backend folder:
   
   cd backend

   
2. Create a virtual environment and activate it:
   
   python -m venv venv
   
   venv\Scripts\activate # Windows
   
   source venv/bin/activate # Mac/Linux


3. Install dependencies:
   
   pip install -r requirements.txt


4. Create a `.env` file in `backend/`:
   
   DATABASE_URL=postgresql+psycopg://username:password@host:port/database_name
   
   SECRET_KEY=your-secret-key


5. Make sure PostgreSQL is running and database exists.

6. Run the server:
    
   uvicorn src.main:app --reload --port 8000
    
   API runs at `http://localhost:8000`


## Frontend Setup

1. Go to the frontend folder:
   
   cd frontend


2. Install dependencies:
   
   npm install


3. Create a `.env` file in `frontend/`:


4. Run the dev server:
   
   npm run dev
   
   App runs at `http://localhost:5173`


## Tech Stack

- **Frontend:** React, Vite
- **Backend:** FastAPI, SQLAlchemy
- **Database:** PostgreSQL


   
