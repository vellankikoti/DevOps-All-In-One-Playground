provider "aws" {
  region = "us-west-2"
}

resource "aws_launch_configuration" "app_launch_config" {
  name          = "app-launch-configuration"
  image_id      = "ami-0c55b159cbfafe1f0"
  instance_type = "t2.micro"
  security_groups = [aws_security_group.app_sg.id]
  lifecycle {
    create_before_destroy = true
  }
}

resource "aws_autoscaling_group" "app_asg" {
  desired_capacity     = 2
  max_size             = 4
  min_size             = 1
  vpc_zone_identifier  = ["subnet-0bb1c79de3EXAMPLE", "subnet-0bb1c79de4EXAMPLE"]
  launch_configuration = aws_launch_configuration.app_launch_config.name

  tags = [
    {
      key                 = "Name"
      value               = "AppInstance"
      propagate_at_launch = true
    },
  ]
}
