provider "aws" {
  region = "us-west-2"
}

data "aws_instances" "all" {}

output "instance_ids" {
  value = data.aws_instances.all.ids
}
