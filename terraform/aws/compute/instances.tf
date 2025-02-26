data "aws_ami" "ubuntu" {
        most_recent = true

        filter {
          name   = "name"
          values = ["ubuntu/images/hvm-ssd/ubuntu-jammy-22.04-amd64-server-*"]
        }

        filter {
          name   = "virtualization-type"
          values = ["hvm"]
        }

        owners = ["099720109477"] # Canonical
      }

    resource "aws_security_group" "allow_ssh" {
      vpc_id = var.vpc_id

      ingress {
        from_port   = 22
        to_port     = 22
        protocol    = "tcp"
        cidr_blocks = ["0.0.0.0/0"]
      }

      ingress {
        from_port   = -1
        to_port     = -1
        protocol    = "icmp"
        cidr_blocks = ["0.0.0.0/0"]
      }

      egress {
        from_port   = 0
        to_port     = 0
        protocol    = "-1"
      }
    }

      resource "aws_instance" "app" {
        ami                    = data.aws_ami.ubuntu.id
        instance_type          = "t3.micro"
        count                  = 2
        subnet_id              = var.subnet_id
        vpc_security_group_ids = [aws_security_group.allow_ssh.id]
        associate_public_ip_address = true
        key_name               = var.key_name

        tags = {
          Name = "AppInstance"
        }
      }

      output "instance_private_ips" {
        value = aws_instance.app[*].private_ip
      }

      output "instance_public_ips" {
        value = aws_instance.app[*].public_ip
      }