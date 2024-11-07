provider "aws" {
  region = "us-west-2"
}

resource "aws_instance" "single" {
  ami           = "ami-0c55b159cbfafe1f0"  # Amazon Linux 2 AMI
  instance_type = "t2.micro"
  tags = {
    Name = "Single-Instance"
  }
}

output "instance_id" {
  value = aws_instance.single.id
}
