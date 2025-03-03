output "vpc_id" {
  value = aws_vpc.main.id
}

output "subnet_id" {
  value = aws_subnet.main.id
}

output "instance_private_ips" {
  value = module.compute.instance_private_ips
}

output "instance_public_ips" {
  value = module.compute.instance_public_ips
}

output "instance_public_dns" {
  value = module.compute.instance_public_dns
}