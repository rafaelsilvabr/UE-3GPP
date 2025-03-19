output "droplet_ids" {
  value = digitalocean_droplet.app[*].id
}

output "droplet_private_ips" {
  value = digitalocean_droplet.app[*].ipv4_address_private
}

output "droplet_public_ips" {
  value = digitalocean_droplet.app[*].ipv4_address
}

output "droplet_public_dns" {
  value = digitalocean_droplet.app[*].name
}