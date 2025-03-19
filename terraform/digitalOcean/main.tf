resource "digitalocean_vpc" "main" {
  name     = "main-vpc"
  region   = var.region
  ip_range = "10.0.0.0/16"
}

resource "digitalocean_droplet" "app" {
  count    = 2
  image    = "ubuntu-20-04-x64"
  name     = "app-instance-${count.index}"
  region   = var.region
  size     = "s-2vcpu-4gb"
  vpc_uuid = digitalocean_vpc.main.id
  ssh_keys = [var.ssh_key_fp]

  tags = ["app"]
}

resource "digitalocean_firewall" "allow_ssh" {
  name = "allow-ssh"

  droplet_ids = digitalocean_droplet.app[*].id

  inbound_rule {
    protocol         = "tcp"
    port_range       = "22"
    source_addresses = ["0.0.0.0/0"]
  }

  inbound_rule {
    protocol         = "tcp"
    port_range       = "5000"
    source_addresses = ["0.0.0.0/0"]
  }

  inbound_rule {
    protocol         = "icmp"
    source_addresses = ["0.0.0.0/0"]
  }

  outbound_rule {
    protocol              = "tcp"
    port_range            = "1-65535"
    destination_addresses = ["0.0.0.0/0"]
  }

  outbound_rule {
    protocol              = "udp"
    port_range            = "1-65535"
    destination_addresses = ["0.0.0.0/0"]
  }

  outbound_rule {
    protocol              = "icmp"
    destination_addresses = ["0.0.0.0/0"]
  }
}