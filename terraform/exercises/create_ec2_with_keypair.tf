provider "aws" {
  region = "us-west-2"
}

resource "aws_key_pair" "my_key" {
  key_name   = "my-key-pair"
  public_key = file("~/.ssh/id_rsa.pub")
}

resource "aws_instance" "with_key" {
  ami           = "ami-0c55b159cbfafe1f0"  # Amazon Linux 2 AMI
  instance_type = "t2.micro"
  key_name      = aws_key_pair.my_key.key_name
  tags = {
    Name = "EC2-Instance-With-Key"
  }
}

output "instance_id" {
  value = aws_instance.with_key.id
}
