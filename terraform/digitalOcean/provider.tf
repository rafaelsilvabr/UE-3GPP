terraform {
  required_providers {
    digitalocean = {
      source = "digitalocean/digitalocean"
      version = "~> 2.0" # Verifique a versão mais recente no registry
    }
  }
}

provider "digitalocean" {
  token = var.do_token
}