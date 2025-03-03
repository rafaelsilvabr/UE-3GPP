# AWS Environment Configuration with Terraform

This guide describes the steps necessary to configure and launch an AWS environment using Terraform. It includes creating an RSA key, configuring the AWS CLI user, registering the SSH key in the AWS account, and applying Terraform.

## Prerequisites

- [Terraform](https://www.terraform.io/downloads.html) installed
- [AWS CLI](https://aws.amazon.com/cli/) installed
- AWS account with appropriate permissions

## Step 1: Configure the AWS CLI User

1. Create an IAM user in AWS with administrative permissions.
2. Generate an access key (Access Key ID and Secret Access Key) for the IAM user.
3. Configure the AWS CLI with the IAM user's credentials:

    ```sh
    aws configure
    ```

    Enter the requested information:
    - AWS Access Key ID
    - AWS Secret Access Key
    - Default region name (e.g., `us-west-2`)
    - Default output format (leave blank or choose `json`)

## Step 2: Create an RSA Key

1. Open a terminal.
2. Generate a new RSA key using the command:

    ```sh
    ssh-keygen -t rsa -b 4096 -f ~/.ssh/id_rsa
    ```

3. Save the key in a secure location. You will use the path to the private key (`id_rsa`) later.

## Step 3: Register the SSH Key in the AWS Account

### Option 1: Using the AWS Console

1. Log in to the AWS Management Console.
2. Navigate to the EC2 service.
3. In the side menu, click on "Key Pairs".
4. Click on "Import Key Pair".
5. Give the key a name (e.g., `id_rsa`).
6. Paste the contents of the `id_rsa.pub` file (the public key) into the appropriate field.
7. Click on "Import Key Pair".

### Option 2: Using the AWS CLI

1. Import the SSH key using the AWS CLI command:

    ```sh
    aws ec2 import-key-pair --key-name "id_rsa" --public-key-material fileb://~/.ssh/id_rsa.pub
    ```

## Step 4: Configure Terraform

1. Navigate to the directory containing the Terraform files and modules:

    ```sh
    cd <REPOSITORY_NAME>/terraform/aws
    ```

2. Initialize Terraform:

    ```sh
    terraform init
    ```

## Step 5: Apply Terraform

1. Edit the `terraform.tfvars` file (if necessary) to define variables, such as the SSH key name:

    ```hcl
    region   = "us-west-2"
    key_name = "id_rsa"
    ```

2. Apply Terraform to create the resources:

    ```sh
    terraform apply
    ```

    Confirm the application by typing `yes` when prompted.

## Step 6: Access the Instances

1. After applying Terraform, obtain the public IP addresses of the instances:

    ```sh
    terraform output instance_public_ips
    ```

2. Connect to the instances using SSH:

    ```sh
    ssh -i ~/.ssh/id_rsa ubuntu@<public-ip>
    ```

    Replace `<public-ip>` with the public IP address of the instance.

## Project Structure

- `main.tf`: Defines the VPC, subnet, Internet Gateway, route table, and associations.
- `compute/instances.tf`: Defines the EC2 instances and the security group.
- `provider.tf`: Configures the AWS provider.
- `variables.tf`: Defines the variables used in the project.
- `outputs.tf`: Defines the Terraform outputs.

## Clean Up Resources

To destroy the resources created by Terraform, run:

```sh
terraform destroy