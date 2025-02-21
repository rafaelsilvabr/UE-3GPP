# 📡 UE 3GPP - Environment Configuration
🚧 **WARNING: This repository is under development!** 🚧

This project is still in progress and may undergo changes.

**User Equipment 3GPP access via free5gc V3.4.4**

----  

This repository is a **fork** of [UE-non3GPP](https://github.com/LABORA-INF-UFG/UE-non3GPP).  

## 🏗️ Test Environment Overview

This repository provides a **test environment** using:
- **[Free5GC](https://github.com/free5gc/free5gc)** for the **5G Core Network (5GC)**
- **[UERANSIM](https://github.com/aligungr/UERANSIM)** for **User Equipment (UE) and gNB simulation**

This guide describes the setup and configuration required to deploy a **3GPP-compatible UE environment** with **Free5GC v3.4.4** and **UERANSIM**.


## 📌 Prerequisites

Before getting started, ensure that you have the following installed on your machine:
- [Git](https://git-scm.com/)
- [Ansible](https://www.ansible.com/)

## ⚙️ Setting Up the Development Environment

Install the required dependencies for the development environment:

```bash
sudo apt update && sudo apt -y install python git ansible net-tools
```

Clone the project using the following command:

```bash
git clone https://github.com/rafaelsilvabr/UE-3GPP.git
```

After cloning the project, you need to **edit the `hosts` file**, located at:  
_UE-3GPP/dev_.

The **hosts** file maps two hosts:
- `fee5gc-core` (for the 5GC core)
- `labora-UE-3GPP` (used for deploying a UE version and simulating a gNB on a second machine)

Let's start by configuring the host responsible for running **fee5gc-core**.

---

## 🔧 Host Configuration

Edit the `hosts` file and replace `<ip-host-5GCore>` and `<ip-ue-3gpp>` with the **IP addresses** of the machines where **fee5gc-core** and **UE-3GPP** will be configured, respectively.

```yaml
[fee5gc-5GCORE]
<ip-host-5GCore> internet_network_interface=eth0  nwdaf_install=false ansible_user=ansible

[ueransim-UE-3GPP]
<ip-ue-3gpp> free5gc_ip_address=<ip-host-5GCore> ansible_user=ansible
```

**Note:** Create a user named `ansible` on the machines and add it to the `sudo` group.

---

## 🔑 SSH Key Exchange

To configure **fee5gc-core** and **UE-3GPP**, the machine needs **root access**, which is done via an SSH key exchange, as described below:

1️⃣ **Generate an SSH key:**  
```bash
ssh-keygen -t ecdsa -b 521
```  
**Note:** After running the command, press **ENTER** three times.

2️⃣ **Copy the generated key to each VM:**  
```bash
ssh-copy-id -i ~/.ssh/id_ecdsa.pub ansible@<ip-host-5GCore>
ssh-copy-id -i ~/.ssh/id_ecdsa.pub ansible@<ip-ue-3gpp>
```

---

## 🔄 Testing Ansible Connection

To test the connection with the hosts, run the following command:  
```bash
ansible -i ./dev/free5gc-v3.4.4/hosts -m ping all -u ansible
```

---

## 🚀 Installing GO via Ansible Playbook

The following command installs **GO v1.21** on each of the VMs.  
Run this from the **root directory** of the project (`UE-3GPP`).

```bash
ansible-playbook dev/free5gc-v3.4.4/go-install-1.21.yaml -i dev/hosts
```

---

## 📦 Installing Free5GC via Ansible Playbook

The command below installs **Free5GC v3.4.4**.  
Run this from the **root directory** of the project (`UE-3GPP`).

```bash
ansible-playbook dev/free5gc-v3.4.4/free5gc-install.yaml -i dev/hosts
```

---

## 🔜 #TODO: Installing UERANSIM via Ansible Playbook

```bash
# ansible-playbook dev/free5gc-v3.4.4/ueransim-install.yaml -i dev/free5gc-v3.4.4/hosts
```

---

## 🏁 Running Free5GC

### ▶️ Running Free5GC Core

To run the **Free5GC Core**, access the `fee5gc-core` host and execute:  
```bash
cd ~/go/src/free5gc
sudo ./run.sh
```

### ▶️ Running Free5GC WebConsole

To run the **WebConsole**, access the `fee5gc-core` host with a new terminal and execute:  
```bash
cd ~/free5gc/webconsole
sudo go run server.go
```

---

## 🔜 #TODO: Running UERANSIM

### ▶️ TODO: Running gNB

// Run the **gNB**

### ▶️ TODO: Running UE

// Run the **UE**

---

## 🔜 TODO: Testing the Connection

// Commands to test routing and deregistration commands  