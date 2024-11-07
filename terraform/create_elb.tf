provider "aws" {
  region = "us-west-2"
}

resource "aws_elb" "main_elb" {
  name               = "main-elb"
  availability_zones = ["us-west-2a", "us-west-2b"]
  listener {
    instance_port     = 80
    instance_protocol = "HTTP"
    lb_port           = 80
    lb_protocol       = "HTTP"
  }

  health_check {
    target              = "HTTP:80/"
    interval            = 30
    timeout             = 5
    healthy_threshold   = 2
    unhealthy_threshold = 2
  }

  tags = {
    Name = "Main-ELB"
  }
}

output "elb_name" {
  value = aws_elb.main_elb.name
}
