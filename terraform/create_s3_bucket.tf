provider "aws" {
  region = "us-west-2"
}

resource "aws_s3_bucket" "bucket" {
  bucket = "my-unique-bucket-name-123456"
  acl    = "private"
  tags = {
    Name        = "MyS3Bucket"
    Environment = "Dev"
  }
}
