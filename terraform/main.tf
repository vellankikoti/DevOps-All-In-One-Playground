provider "aws" {
  region = "us-west-2"
}

resource "aws_eks_cluster" "devops_cluster" {
  name     = "devops-cluster"
  role_arn = var.eks_role_arn
  vpc_config {
    subnet_ids = var.subnet_ids
  }
}

resource "aws_eks_node_group" "devops_node_group" {
  cluster_name    = aws_eks_cluster.devops_cluster.name
  node_role_arn   = var.eks_node_role_arn
  subnet_ids      = var.subnet_ids
  instance_type   = "t3.medium"
  desired_capacity = 2
}

