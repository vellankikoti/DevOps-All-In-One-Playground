provider "aws" {
  region = "us-west-2"
}

resource "aws_s3_bucket" "secure_bucket" {
  bucket = "secure-versioned-bucket-123456"
  acl    = "private"

  versioning {
    enabled = true
  }

  server_side_encryption_configuration {
    rule {
      apply_server_side_encryption_by_default {
        sse_algorithm = "AES256"
      }
    }
  }

  tags = {
    Name        = "SecureBucket"
    Environment = "Production"
  }
}
