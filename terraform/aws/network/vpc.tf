# terraform/aws/network/vpc.tf
  data "aws_vpc" "default" {
    default = true
  }

  resource "aws_vpc" "main" {
    count      = length(data.aws_vpc.default.id) == 0 ? 1 : 0
    cidr_block = "10.0.0.0/16"
  }

  resource "aws_subnet" "main" {
    vpc_id            = length(data.aws_vpc.default.id) == 0 ? aws_vpc.main[0].id : data.aws_vpc.default.id
    cidr_block        = "10.0.1.0/24"
    availability_zone = "us-west-2a"
  }

  output "vpc_id" {
    value = length(data.aws_vpc.default.id) == 0 ? aws_vpc.main[0].id : data.aws_vpc.default.id
  }

  output "subnet_id" {
    value = aws_subnet.main.id
  }