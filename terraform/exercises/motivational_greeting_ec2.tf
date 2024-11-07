provider "aws" {
  region = "us-west-2"
}

resource "aws_instance" "motivational_instance" {
  ami           = "ami-0c55b159cbfafe1f0"  # Amazon Linux 2 AMI
  instance_type = "t2.micro"

  user_data = <<-EOF
              #!/bin/bash
              echo "Hello, DevOps Warrior!" > /motivation.txt
              echo "You're doing an amazing job. Keep it up!" >> /motivation.txt
              echo "Here's a quote for you: 'Infrastructure as code is like dating -- you commit, but there’s always room for improvement.'" >> /motivation.txt
              echo "P.S. Remember to hydrate, automate, and celebrate!" >> /motivation.txt
              EOF

  tags = {
    Name = "MotivationalInstance"
  }
}

output "motivation_location" {
  value = "Login to ${aws_instance.motivational_instance.public_ip} and check /motivation.txt for some words of encouragement!"
}
