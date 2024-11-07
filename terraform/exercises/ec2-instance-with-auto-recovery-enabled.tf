provider "aws" {
  region = "us-west-2"
}

resource "aws_instance" "recovery_instance" {
  ami           = "ami-0c55b159cbfafe1f0"
  instance_type = "t2.micro"
  tags = {
    Name = "Auto-Recovery-Instance"
  }
}

resource "aws_cloudwatch_metric_alarm" "instance_recovery_alarm" {
  alarm_name          = "EC2InstanceAutoRecovery"
  comparison_operator = "GreaterThanThreshold"
  evaluation_periods  = 2
  metric_name         = "StatusCheckFailed_System"
  namespace           = "AWS/EC2"
  period              = 60
  statistic           = "Minimum"
  threshold           = 1
  alarm_actions       = [aws_instance.recovery_instance.arn]
}
