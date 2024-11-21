# Interactive DevOps Quiz Platform - Frontend

## Overview
This is the frontend for the Interactive DevOps Quiz Platform, designed to provide a fun and interactive learning experience for DevOps professionals and enthusiasts. The platform challenges users with quizzes on Linux, Python, Git, Jenkins, Ansible, Docker, Kubernetes, and Terraform.

## Features
- **Interactive Quiz Interface:** Section-wise quizzes with dynamic question loading.
- **Real-time Progress Tracking:** Tracks scores and progress across sections.
- **Responsive Design:** Optimized for desktop and mobile.
- **Customizable Themes:** Styled with a clean blue, white, and black theme for intuitive use.
- **Integration Ready:** Communicates seamlessly with the Python Flask backend.

## Prerequisites
Ensure you have the following installed:
- Node.js (16.x or higher)
- Docker (for containerized deployment)

## Installation

### Local Setup
1. Clone the repository:
   ```bash
   git clone https://github.com/yourusername/DevOps-All-In-One-Playground.git
   cd DevOps-All-In-One-Playground/frontend
   ```

2. Install dependencies:
   ```bash
   npm install
   ```

3. Start the development server:
   ```bash
   npm start
   ```

4. Open your browser and navigate to `http://localhost:3000`.

### Docker Setup
1. Build the Docker image:
   ```bash
   docker build -t devops-quiz-frontend .
   ```

2. Run the Docker container:
   ```bash
   docker run -p 3000:80 devops-quiz-frontend
   ```

3. Access the application at `http://localhost:3000`.

## Environment Variables
Configure the backend API URL by creating a `.env` file:
```
REACT_APP_API_URL=http://localhost:5000
```

## File Structure
```
src/
├── App.js            # Main application file
├── Home.js           # Landing page component
├── Progress.js       # Progress tracking component
├── Result.js         # Result display component
├── components/       # Additional reusable components
│   ├── Header.js     # Header for navigation
│   ├── Challenge.js  # Quiz component for each section
├── styles/           # CSS files for styling
│   ├── App.css       # Global styles
│   ├── Header.css    # Header-specific styles
│   ├── Progress.css  # Progress tracker styles
├── api/              # API utility functions
│   ├── api.js        # Functions for backend interaction
├── index.js          # Entry point for React application
├── public/           # Static files
│   ├── index.html    # Main HTML file
```

## Running Tests
1. Run the test suite:
   ```bash
   npm test
   ```

2. Ensure all tests pass before deployment.

## Contribution
Contributions are welcome! Fork the repository, create a new branch, and submit a pull request with your changes.

## License
This project is licensed under the MIT License.

