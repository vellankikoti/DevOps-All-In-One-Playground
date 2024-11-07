
# Backend - DevOps All-In-One Playground

This is the backend for the DevOps All-In-One Playground, built with Node.js and Express. It provides CRUD API endpoints for managing records in a PostgreSQL database.

## 📦 Installation

### Prerequisites
- **Node.js** and **npm**
- **PostgreSQL** (if running locally without Docker)

### Run Locally
1. Install dependencies:
   ```bash
   npm install
   ```
2. Set environment variables:
   - `DATABASE_URL`: Connection string for PostgreSQL
3. Start the server:
   ```bash
   npm start
   ```

The backend will run on `http://localhost:5000`.

### Run with Docker
1. Build the Docker image:
   ```bash
   docker build -t devops-backend .
   ```
2. Run the Docker container:
   ```bash
   docker run -p 5000:5000 -e DATABASE_URL='your_database_url' devops-backend
   ```

## API Endpoints

- `POST /api/records` - Create a new record
- `GET /api/records` - Retrieve all records
- `GET /api/records/:id` - Retrieve a specific record by ID
- `PUT /api/records/:id` - Update a record by ID
- `DELETE /api/records/:id` - Delete a record by ID

---

This backend service is Docker-compatible and ready for deployment on Kubernetes or other container orchestration platforms.

---

