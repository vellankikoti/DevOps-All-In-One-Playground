```markdown
# Terraform - DevOps All-In-One Playground

This folder contains Terraform configurations for provisioning infrastructure on AWS. It includes an EKS cluster setup for deploying the DevOps-All-In-One Playground application and additional exercises to help DevOps engineers practice essential Terraform use cases.

## Overview

The `main.tf` file provisions an Elastic Kubernetes Service (EKS) cluster on AWS, which forms the backbone for hosting the application. Additionally, the `terraform/exercises/` folder provides various scenarios for learning and practicing Terraform, covering everything from provisioning EC2 instances to creating S3 buckets.

---

## Prerequisites

To get started, ensure you have the following installed:

1. **Terraform**: Install the latest version from [terraform.io](https://www.terraform.io/downloads).
2. **AWS CLI**: Install and configure the AWS CLI with credentials having sufficient permissions to manage AWS resources.
3. **IAM Roles**: IAM roles with policies allowing resource provisioning for EKS, VPC, EC2, S3, and related services.
4. **kubectl**: For managing Kubernetes resources on the EKS cluster.

---

## Main EKS Configuration

The main Terraform configuration (`main.tf`) provisions:

- A VPC with public and private subnets across multiple availability zones.
- An EKS cluster and managed node groups for scalable and secure Kubernetes workloads.
- IAM roles and policies for the EKS cluster and worker nodes.
- Security groups for controlled access to the cluster resources.

---

## Setup Steps

### Step 1: Initialize Terraform

Navigate to the `terraform/` folder and initialize Terraform:
```bash
terraform init
```

### Step 2: Configure Variables

Create a `terraform.tfvars` file to define the required variables:
```hcl
eks_role_arn      = "arn:aws:iam::123456789012:role/eks-cluster-role"
eks_node_role_arn = "arn:aws:iam::123456789012:role/eks-node-role"
subnet_ids        = ["subnet-0bb1c79de3EXAMPLE", "subnet-0bb1c79de4EXAMPLE"]
region            = "us-west-2"
```

### Step 3: Apply Terraform

Review the execution plan:
```bash
terraform plan
```

Apply the configuration to create the resources:
```bash
terraform apply
```

### Step 4: Configure kubectl

Once the EKS cluster is provisioned, configure `kubectl`:
```bash
aws eks --region us-west-2 update-kubeconfig --name devops-cluster
kubectl get nodes
```

### Step 5: Clean Up

To destroy all resources, run:
```bash
terraform destroy
```

---

## Terraform Exercises

The `terraform/exercises/` folder contains configurations for learning and practicing Terraform:

1. **List EC2 Instances**: Lists all EC2 instances in a region.
   - **File**: `list_ec2_instances.tf`
2. **Create Single EC2 Instance**: Provisions a single EC2 instance.
   - **File**: `create_single_ec2.tf`
3. **Create Multiple EC2 Instances**: Provisions 3 or more EC2 instances.
   - **File**: `create_three_ec2_instances.tf`
4. **Create VPC with Subnets**: Provisions a custom VPC with subnets.
   - **File**: `create_vpc.tf`
5. **S3 Bucket with Versioning**: Sets up an S3 bucket with versioning enabled.
   - **File**: `create_s3_bucket.tf`
6. **Motivational EC2 Instance**: Creates an EC2 instance with a motivational message in `/motivation.txt`.
   - **File**: `motivational_greeting_ec2.tf`
7. **Random Compliment EC2 Instance**: Provisions an EC2 instance with a random compliment in `/compliment.txt`.
   - **File**: `random_compliment_ec2.tf`

---

## Outputs

Upon successful execution of the main Terraform configuration, the following outputs are available:

- **VPC ID**: Identifier for the created VPC.
- **EKS Cluster Name**: Name of the Kubernetes cluster.
- **EKS Endpoint**: URL for accessing the Kubernetes API.
- **Node Role ARN**: IAM role ARN for worker nodes.

---

## Troubleshooting

1. **Error: Required attribute `name` not specified**:
   Ensure that all resource names are correctly defined in `main.tf` and variable files.

2. **Permission Denied**:
   Verify your AWS IAM credentials have necessary permissions.

3. **State Lock Issues**:
   If a state lock occurs, use:
   ```bash
   terraform force-unlock <lock-id>
   ```

4. **EKS Cluster Not Reachable**:
   Ensure `kubectl` is configured correctly and check your security group rules.

---

## Contributing

We welcome contributions! Open an issue or submit a pull request for suggestions or improvements.

---

## License

This repository is licensed under the MIT License. See the [LICENSE](../LICENSE.md) file for more details.
```