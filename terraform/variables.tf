variable "aws_region" {
  description = "The AWS region to deploy resources."
  default     = "us-east-1"
}

variable "cluster_name" {
  description = "EKS cluster name."
  default     = "devops-playground-cluster"
}

variable "vpc_cidr" {
  description = "VPC CIDR block."
  default     = "10.0.0.0/16"
}
