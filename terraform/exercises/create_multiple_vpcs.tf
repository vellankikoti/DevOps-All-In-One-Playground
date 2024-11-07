provider "aws" {
  region = "us-west-2"
}

resource "aws_vpc" "vpc" {
  count      = 2
  cidr_block = "10.${count.index}.0.0/16"
  tags = {
    Name = "VPC-${count.index + 1}"
  }
}

output "vpc_ids" {
  value = aws_vpc.vpc[*].id
}
