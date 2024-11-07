variable "eks_role_arn" {
  description = "IAM role ARN for EKS cluster"
  type        = string
}

variable "eks_node_role_arn" {
  description = "IAM role ARN for EKS node group"
  type        = string
}

variable "subnet_ids" {
  description = "List of VPC subnet IDs"
  type        = list(string)
}
