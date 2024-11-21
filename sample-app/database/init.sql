-- Create database and user
CREATE DATABASE devops_quiz;
CREATE USER quiz_user WITH ENCRYPTED PASSWORD 'secure_password';

-- Grant privileges
GRANT ALL PRIVILEGES ON DATABASE devops_quiz TO quiz_user;

-- Create questions table
CREATE TABLE questions (
    id SERIAL PRIMARY KEY,
    category VARCHAR(255) NOT NULL,
    question TEXT NOT NULL,
    options JSONB NOT NULL,
    answer VARCHAR(255) NOT NULL
);

-- Insert sample data (for testing)
INSERT INTO questions (category, question, options, answer)
VALUES
    ('Linux', 'What is the command to list files in a directory?', '{"a": "ls", "b": "pwd", "c": "cd"}', 'a'),
    ('Python', 'Which keyword is used to create a function in Python?', '{"a": "function", "b": "def", "c": "lambda"}', 'b');
