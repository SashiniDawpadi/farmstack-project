# FARM Stack Project

A simple Task Manager application built using the **FARM stack**:  
**FastAPI** (backend), **React** (frontend), and **MongoDB** (database).

## 📁 Project Structure

.
├── backend/
│ ├── database.py
│ ├── main.py
│ ├── model.py
│ ├── Pipfile
│ ├── Pipfile.lock
│ └── requirements.txt
├── frontend/
│ ├── node_modules/
│ ├── package.json
│ ├── package-lock.json
│ ├── public/
│ └── src/
├── .gitignore
├── README.md

## Features

- Add, view, and delete tasks
- FastAPI backend with MongoDB for data storage
- React frontend with Bootstrap styling
- RESTful API

## Getting Started

### Prerequisites

- Python 3.10+
- Node.js & npm
- MongoDB running locally on default port (`mongodb://localhost:27017/`)

---

### Backend Setup

1. **Install dependencies:**
    ```sh
    cd backend
    pip install -r requirements.txt
    ```

2. **Run the FastAPI server:**
    ```sh
    uvicorn main:app --reload
    ```
    The API will be available at [http://localhost:8000](http://localhost:8000).

---

### Frontend Setup

1. **Install dependencies:**
    ```sh
    cd frontend
    npm install
    ```

2. **Start the React app:**
    ```sh
    npm start
    ```
    The app will open at [http://localhost:3000](http://localhost:3000).

---

## API Endpoints

- `GET /api/todo` — Get all todos
- `GET /api/todo{title}` — Get a todo by title
- `POST /api/todo` — Create a new todo
- `PUT /api/todo{title}` — Update a todo's description
- `DELETE /api/todo{title}` — Delete a todo by title

---

## Folder Details

- **backend/**: FastAPI app and MongoDB integration (main.py, database.py, model.py)
- **frontend/**: React app (src/App.js, src/components/TodoListView.js, src/components/Todo.js)

---

## License

This project is licensed under the MIT License.

---

## Acknowledgements

- [FastAPI](https://fastapi.tiangolo.com/)
- [React](https://react.dev/)
-