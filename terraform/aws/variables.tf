# terraform/aws/variables.tf
variable "region" {
  description = "AWS region"
  type        = string
  default     = "us-west-2"
}

variable "key_name" {
  description = "The name of the SSH key pair"
  type        = string
}