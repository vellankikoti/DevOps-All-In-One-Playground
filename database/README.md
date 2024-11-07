
# Database - DevOps All-In-One Playground

This is the PostgreSQL database for the DevOps All-In-One Playground application. It stores records with fields for `id`, `name`, `description`, and `created_at`.

## 📦 Installation

### Prerequisites
- **PostgreSQL** installed locally (if running outside of Docker)

### Run with Docker

The easiest way to run the database is through Docker, using the provided Docker Compose setup.

1. Start the database service with Docker Compose:
   ```bash
   docker-compose up -d database
   ```

This will start a PostgreSQL database accessible at `localhost:5432`.

### Run Locally (Without Docker)

1. Install PostgreSQL and set up the database:
   - Create a new database named `devops_db`.
   - Create a user with username `devops` and password `password`.
   - Grant privileges on the database to this user.

2. Run the SQL initialization script:
   ```bash
   psql -U devops -d devops_db -f database/init.sql
   ```

### Database Configuration

- **Database Name**: `devops_db`
- **User**: `devops`
- **Password**: `password`
- **Port**: `5432`

The schema will be created automatically when the database starts.

---

This PostgreSQL database setup is compatible with both Docker and local environments, making it adaptable for any development workflow.

---

