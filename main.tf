provider "aws" {
  region     = "ap-south-1"
  access_key = "AKIARIZDJCZWBCVTPL6N"
  secret_key = "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"
}

resource "aws_s3_bucket" "s3_create" {
  bucket = "msdscenario-prod-bucket"
 versioning {
    enabled = true
  }
}

resource "aws_s3_bucket_object" "s3_push" {
  bucket = aws_s3_bucket.s3_create.bucket
  key    = "python.py"
  source = "/data/git_checkout_location/python.py"
}
