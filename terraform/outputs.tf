output "cluster_name" {
  value = aws_eks_cluster.devops_cluster.name
}

output "kubeconfig" {
  value = <<EOT
apiVersion: v1
clusters:
- cluster:
    server: ${aws_eks_cluster.devops_cluster.endpoint}
  name: eks
contexts:
- context:
    cluster: eks
  name: eks
current-context: eks
EOT
}
