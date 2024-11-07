# Use official Node.js image
FROM node:14

# Create app directory
WORKDIR /app

# Install app dependencies
COPY package.json ./
RUN npm install

# Copy app source code
COPY . .

# Expose port and start app
EXPOSE 5000
CMD ["node", "src/server.js"]

