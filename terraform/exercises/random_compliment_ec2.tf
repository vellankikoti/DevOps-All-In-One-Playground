provider "aws" {
  region = "us-west-2"
}

locals {
  compliments = [
    "You're the Terraform of my cloud.",
    "You automate like no one else!",
    "The cloud bows to your skills.",
    "You're the hero Kubernetes deserves.",
    "Your YAML files are poetry in motion."
  ]
  random_compliment = element(local.compliments, random_pet.compliment_suffix.id % length(local.compliments))
}

resource "random_pet" "compliment_suffix" {}

resource "aws_instance" "compliment_instance" {
  ami           = "ami-0c55b159cbfafe1f0"  # Amazon Linux 2 AMI
  instance_type = "t2.micro"

  user_data = <<-EOF
              #!/bin/bash
              echo "${local.random_compliment}" > /compliment.txt
              EOF

  tags = {
    Name = "ComplimentInstance"
  }
}

output "compliment_location" {
  value = "SSH to ${aws_instance.compliment_instance.public_ip} and view /compliment.txt for a personalized compliment!"
}
