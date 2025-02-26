# terraform/aws/compute/variables.tf
variable "vpc_id" {
  description = "The ID of the VPC"
  type        = string
}

variable "subnet_id" {
  description = "The ID of the subnet"
  type        = string
}

variable "key_name" {
  description = "The name of the SSH key pair"
  type        = string
}