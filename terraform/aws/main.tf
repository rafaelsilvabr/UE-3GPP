# terraform/aws/main.tf
resource "aws_vpc" "main" {
  cidr_block = "10.0.0.0/16"
}

resource "aws_subnet" "main" {
  vpc_id     = aws_vpc.main.id
  cidr_block = "10.0.1.0/24"
}

module "compute" {
  source    = "./compute"
  vpc_id    = aws_vpc.main.id
  subnet_id = aws_subnet.main.id
  key_name  = var.key_name
}