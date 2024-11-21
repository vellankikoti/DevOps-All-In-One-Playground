# Backend - DevOps-All-In-One-Playground

The **backend** for the DevOps-All-In-One-Playground is built using **Python** and **Flask**. It serves as the core engine of the interactive quiz application, managing user data, storing questions, and evaluating responses.

---

## Folder Structure

```plaintext
backend/
├── app.py               # Main application file
├── requirements.txt     # Python dependencies
├── Dockerfile           # Dockerfile for backend
├── questions.json       # Questions for the quiz application
├── tests/               # Unit tests for backend
│   └── test_app.py      # Example test file
└── README.md            # Documentation for backend
```

---

## Features

1. **Interactive Quiz Engine**:
   - Handles user authentication (name, email, phone).
   - Dynamically fetches random questions from the database or JSON file.
   - Validates user responses and calculates scores.

2. **Scalability**:
   - Questions are stored in a `questions.json` file for easy customization and scalability.
   - Randomized question delivery ensures unique experiences for each user.

3. **REST API**:
   - Provides endpoints for the frontend to interact with the backend.

4. **Dockerized**:
   - The backend is containerized for easy deployment in any environment.

---

## Prerequisites

1. **Python**: Version 3.9+ installed.
2. **Pip**: Python package installer.
3. **Docker**: Installed for containerized deployment.

---

## Setup Instructions

### Run Locally

1. Navigate to the backend directory:
   ```bash
   cd sample-app/backend
   ```

2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

3. Start the server:
   ```bash
   python app.py
   ```

4. The server will start on `http://127.0.0.1:5000`.

---

## Docker Setup

1. Build the Docker image:
   ```bash
   docker build -t devops-backend .
   ```

2. Run the container:
   ```bash
   docker run -p 5000:5000 devops-backend
   ```

---

## Endpoints

### 1. **GET /questions/{topic}**
   - Fetches questions for the specified topic.
   - Example:
     ```bash
     curl http://127.0.0.1:5000/questions/linux
     ```
   - Response:
     ```json
     [
       {
         "question": "What does the 'ls' command do?",
         "options": ["List files", "Delete files", "Copy files", "Move files"],
         "answer": "List files"
       }
     ]
     ```

### 2. **POST /submit**
   - Submits user responses and calculates the score.
   - Example:
     ```bash
     curl -X POST http://127.0.0.1:5000/submit \
       -H "Content-Type: application/json" \
       -d '{"username": "John", "responses": {"linux": ["List files", "Move files"]}}'
     ```
   - Response:
     ```json
     {
       "username": "John",
       "score": 80,
       "next_topic": "python"
     }
     ```

---

## Customization

1. **Add Questions**:
   - Update the `questions.json` file with new questions and topics.

2. **Change Configurations**:
   - Modify `app.py` for additional routes or logic.

---

## Testing

1. Run the tests:
   ```bash
   python -m unittest discover tests
   ```

2. Example output:
   ```
   ----------------------------------------------------------------------
   Ran 5 tests in 0.014s

   OK
   ```

---

## Contribution

1. Fork the repository.
2. Create a new branch:
   ```bash
   git checkout -b feature/backend-improvements
   ```
3. Commit your changes:
   ```bash
   git commit -m "Improved backend scalability"
   ```
4. Push to the branch:
   ```bash
   git push origin feature/backend-improvements
   ```
5. Open a pull request.

---

## License

This backend is part of the **DevOps-All-In-One-Playground** and is licensed under the MIT License.

