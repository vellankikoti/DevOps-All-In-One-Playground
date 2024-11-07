provider "aws" {
  region = "us-west-2"
}

resource "aws_instance" "hundred" {
  count         = 100
  ami           = "ami-0c55b159cbfafe1f0"  # Amazon Linux 2 AMI
  instance_type = "t2.micro"
  tags = {
    Name = "Batch-Instance-${count.index + 1}"
  }
}

output "instance_ids" {
  value = aws_instance.hundred[*].id
}
