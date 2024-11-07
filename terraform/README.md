
# Terraform - DevOps All-In-One Playground

This folder contains Terraform configurations for provisioning infrastructure on AWS. It includes exercises to help DevOps engineers practice commonly used Terraform setups and scenarios.

## Overview

The `main.tf` file provisions an EKS (Elastic Kubernetes Service) cluster on AWS, enabling deployment of the DevOps All-In-One Playground application in a managed Kubernetes environment. Additionally, the `terraform/exercises/` folder contains independent Terraform files that allow you to explore common infrastructure scenarios.

## 📦 Prerequisites

1. **Terraform**: Install Terraform from [terraform.io](https://www.terraform.io/downloads).
2. **AWS CLI**: Install and configure the AWS CLI with credentials that have sufficient permissions for managing AWS resources.
3. **IAM Roles**: Make sure you have necessary IAM roles for provisioning EKS clusters, VPCs, EC2 instances, and other resources.

## Main EKS Configuration

The main Terraform file `main.tf` includes a backend configuration for remote state storage. This EKS configuration uses an S3 bucket for state management, which is essential for collaborative or long-term infrastructure projects.

### Setup Steps

### Step 1: Initialize Terraform

1. Navigate to the `terraform/` folder.
2. Run the following command to initialize Terraform and install necessary plugins:
   ```bash
   terraform init
   ```

### Step 2: Define Variables

1. Create a `terraform.tfvars` file in the `terraform/` folder to define variable values (replace with your actual values):
   ```hcl
   eks_role_arn     = "arn:aws:iam::123456789012:role/eks-cluster-role"
   eks_node_role_arn = "arn:aws:iam::123456789012:role/eks-node-role"
   subnet_ids       = ["subnet-0bb1c79de3EXAMPLE", "subnet-0bb1c79de4EXAMPLE"]
   ```

### Step 3: Apply Terraform

1. Run the following command to review the changes Terraform will apply:
   ```bash
   terraform plan
   ```

2. To create the infrastructure, execute:
   ```bash
   terraform apply
   ```

3. Once applied, Terraform will output the cluster name and `kubeconfig` details.

### Step 4: Configure kubectl

1. Use the generated `kubeconfig` to configure access to the EKS cluster:
   ```bash
   aws eks --region us-west-2 update-kubeconfig --name devops-cluster
   ```

2. Verify the connection to the cluster:
   ```bash
   kubectl get nodes
   ```

### Cleaning Up

To delete the EKS cluster and all associated resources, use:
```bash
terraform destroy
```

## Terraform Exercises

The `terraform/exercises/` folder includes Terraform configurations for the following scenarios:

1. **List EC2 Instances**: Lists all EC2 instances in the specified region.
   - **Filename**: `list_ec2_instances.tf`
2. **Create Single EC2 Instance**: Provisions a single EC2 instance.
   - **Filename**: `create_single_ec2.tf`
3. **Create 3 EC2 Instances**: Provisions three EC2 instances.
   - **Filename**: `create_three_ec2_instances.tf`
4. **Create 100 EC2 Instances**: Provisions a batch of 100 EC2 instances.
   - **Filename**: `create_hundred_ec2_instances.tf`
5. **Create VPC and Subnets**: Provisions a VPC with associated subnets.
   - **Filename**: `create_vpc.tf`
6. **Create S3 Bucket with Versioning**: Sets up an S3 bucket with versioning and encryption enabled.
   - **Filename**: `create_s3_bucket.tf`
7. **Motivational Greeting EC2 Instance**: Creates an EC2 instance with a humorous motivational message in `/motivation.txt`.
   - **Filename**: `motivational_greeting_ec2.tf`
8. **Random Compliment EC2 Instance**: Provisions an EC2 instance with a random compliment in `/compliment.txt`.
   - **Filename**: `random_compliment_ec2.tf`

## How to Use Exercises

1. Navigate to the `terraform/exercises/` folder.
2. Run `terraform init` in the folder for the exercise you want to test.
3. Apply the configuration with `terraform apply`.
4. To clean up, use `terraform destroy`.

---

This Terraform setup offers a comprehensive range of configurations, from creating EC2 instances and VPCs to setting up an EKS cluster. These exercises are designed to help DevOps engineers practice Terraform skills and get comfortable with AWS resource provisioning.

---

