# Use the official PostgreSQL image
FROM postgres:14

# Set environment variables for default database setup
ENV POSTGRES_DB=quiz
ENV POSTGRES_USER=quiz_user
ENV POSTGRES_PASSWORD=quiz_password

# Copy the initialization SQL script
COPY init.sql /docker-entrypoint-initdb.d/

# Expose PostgreSQL port
EXPOSE 5432
