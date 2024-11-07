
# Step-by-Step Setup Guide for DevOps-All-In-One-Playground

## Overview

This guide will help you set up the **DevOps-All-In-One-Playground** on your local machine or an EC2 instance on AWS. By following these instructions, you will have the frontend and backend applications running, along with the necessary monitoring tools.

### Prerequisites

Before you begin, ensure you have the following:

1. **Amazon Web Services (AWS) Account**: If you don’t have one, [sign up here](https://aws.amazon.com/free/).
2. **Basic knowledge of command-line interface**: You'll be using commands in a terminal.
3. **Internet Connection**: Required for downloading software and packages.

## Step 1: Launch an EC2 Instance

1. **Log in to AWS Console**:
   - Go to the [AWS Management Console](https://aws.amazon.com/console/).
   - Log in with your AWS account credentials.

2. **Navigate to EC2**:
   - In the AWS Management Console, search for "EC2" in the services menu and select it.

3. **Launch Instance**:
   - Click on the **Launch Instance** button.

4. **Choose an Amazon Machine Image (AMI)**:
   - Select the **Ubuntu Server 20.04 LTS (HVM), SSD Volume Type**.

5. **Select Instance Type**:
   - Choose the **t2.micro** instance type (this is eligible for the free tier).
   - Click **Next: Configure Instance Details**.

6. **Configure Instance Details**:
   - You can leave the default settings.
   - Click **Next: Add Storage**.

7. **Add Storage**:
   - The default storage (8 GiB) is usually sufficient. Click **Next: Add Tags**.

8. **Add Tags**:
   - (Optional) You can add tags for organization, but it’s not necessary for setup. Click **Next: Configure Security Group**.

9. **Configure Security Group**:
   - Create a new security group and add the following rules:
     - **Type**: SSH | **Protocol**: TCP | **Port Range**: 22 | **Source**: My IP
     - **Type**: HTTP | **Protocol**: TCP | **Port Range**: 80 | **Source**: Anywhere
     - **Type**: Custom TCP Rule | **Protocol**: TCP | **Port Range**: 3000 | **Source**: Anywhere
     - **Type**: Custom TCP Rule | **Protocol**: TCP | **Port Range**: 5000 | **Source**: Anywhere
     - **Type**: Custom TCP Rule | **Protocol**: TCP | **Port Range**: 5432 | **Source**: Anywhere
     - **Type**: Custom TCP Rule | **Protocol**: TCP | **Port Range**: 9090 | **Source**: Anywhere
     - **Type**: Custom TCP Rule | **Protocol**: TCP | **Port Range**: 3001 | **Source**: Anywhere
   - Click **Review and Launch**.

10. **Launch Instance**:
    - Click the **Launch** button.
    - Select or create a new key pair (make sure to download it; you will need it to connect to your instance).
    - Click **Launch Instances**.

11. **Access the Instance**:
    - Once your instance is running, go back to the **Instances** section.
    - Select your instance and find the **Public IP** address. You’ll use this to connect to your instance.

## Step 2: Connect to Your EC2 Instance

1. **Open Terminal** (Linux/Mac) or **Command Prompt** (Windows).
2. **Navigate to the folder** where your key pair (.pem file) is stored.

3. **Connect to your instance**:
   - Run the following command (replace `your-key-file.pem` with your key file name and `ec2-user@your-public-ip` with the public IP of your instance):
     ```bash
     ssh -i "your-key-file.pem" ubuntu@your-public-ip
     ```

   - If prompted, type "yes" to confirm the connection.

## Step 3: Install Required Software

Once connected to your EC2 instance, run the following commands:

1. **Update the package list**:
   ```bash
   sudo apt update
   ```

2. **Install Docker**:
   ```bash
   sudo apt install docker.io -y
   ```

3. **Install Docker Compose**:
   ```bash
   sudo apt install docker-compose -y
   ```

4. **Start Docker service**:
   ```bash
   sudo systemctl start docker
   sudo systemctl enable docker
   ```

5. **Install Git** (to clone the repository):
   ```bash
   sudo apt install git -y
   ```

## Step 4: Clone the Repository

1. **Clone the repository**:
   ```bash
   git clone https://github.com/vellankikoti/DevOps-All-In-One-Playground.git
   cd DevOps-All-In-One-Playground
   ```

## Step 5: Run the Application

1. **Start the services using Docker Compose**:
   ```bash
   docker-compose up -d
   ```

   - This command will start the `frontend`, `backend`, and `database` services.

2. **Access the Applications**:
   - The frontend is accessible at: `http://your-public-ip:3000`
   - The backend API is available at: `http://your-public-ip:5000`
   - The PostgreSQL database runs on port `5432` but is not directly accessed by users.

## Step 6: Set Up Observability Tools (Optional)

1. **Install Prometheus and Grafana**:
   - You can run Prometheus and Grafana using Docker by following the instructions in the `observability/` folder.

2. **Run Prometheus**:
   - Ensure that the Prometheus configuration file is correctly set up to scrape metrics from the frontend and backend applications.

3. **Run Grafana**:
   - Access Grafana at `http://your-public-ip:3001` and import the dashboard configuration.

## Step 7: Verify and Monitor

1. **Verify that the applications are running**:
   - Use a web browser to navigate to the frontend and backend URLs.
   - Ensure that Prometheus and Grafana are correctly collecting and displaying metrics.

2. **Monitor Logs**:
   - Use the Docker logs to monitor any errors or important messages:
   ```bash
   docker-compose logs
   ```

## Step 8: Clean Up

When you're finished testing, you can stop the services and remove the containers:

```bash
docker-compose down
```

And you can terminate the EC2 instance from the AWS Management Console to avoid any charges.

---

By following these steps, you should be able to set up and test the **DevOps-All-In-One-Playground** project successfully.
