variable "do_token" {
  description = "DigitalOcean API token"
  type        = string
}

variable "region" {
  description = "DigitalOcean region"
  type        = string
  default     = "nyc3"
}

variable "ssh_key_fp" {
  description = "SSH key ID for accessing droplets"
  type        = string
}