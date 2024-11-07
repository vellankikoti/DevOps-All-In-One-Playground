provider "aws" {
  region = "us-west-2"
}

resource "aws_s3_bucket" "lifecycle_bucket" {
  bucket = "my-lifecycle-bucket-123456"
  acl    = "private"
}

resource "aws_s3_bucket_lifecycle_configuration" "lifecycle_rule" {
  bucket = aws_s3_bucket.lifecycle_bucket.id

  rule {
    id     = "log"
    status = "Enabled"

    expiration {
      days = 30
    }
  }
}

output "bucket_name" {
  value = aws_s3_bucket.lifecycle_bucket.bucket
}
