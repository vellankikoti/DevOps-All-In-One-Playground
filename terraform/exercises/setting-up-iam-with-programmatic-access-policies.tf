provider "aws" {
  region = "us-west-2"
}

resource "aws_iam_user" "developer_user" {
  name = "developer-user"
}

resource "aws_iam_access_key" "developer_access_key" {
  user = aws_iam_user.developer_user.name
}

resource "aws_iam_user_policy" "developer_policy" {
  name = "developer-policy"
  user = aws_iam_user.developer_user.name

  policy = jsonencode({
    Version = "2012-10-17"
    Statement = [
      {
        Action   = ["ec2:Describe*"]
        Effect   = "Allow"
        Resource = "*"
      },
      {
        Action   = ["s3:ListBucket", "s3:GetObject"]
        Effect   = "Allow"
        Resource = ["arn:aws:s3:::example-bucket/*"]
      }
    ]
  })
}

output "access_key_id" {
  value = aws_iam_access_key.developer_access_key.id
}

output "secret_access_key" {
  value = aws_iam_access_key.developer_access_key.secret
  sensitive = true
}
