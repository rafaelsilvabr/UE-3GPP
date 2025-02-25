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
git clone https://github.com/LABORA-INF-UFG/UE-3GPP
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

## 📦 Installing UERANSIM via Ansible Playbook

```bash
ansible-playbook dev/ueransim/ueransim-install.yaml -i dev/hosts
```

---

## 🌐 Configuring Network for Free5GC and UERANSIM
After installing Free5GC and UERANSIM, it is necessary to configure the network to ensure that packets are forwarded correctly.

### 1️⃣ Enable IPv4 Packet Forwarding
Run the command below to ensure that Linux continues to forward packets between network interfaces:

```bash
echo "net.ipv4.ip_forward=1" | sudo tee -a /etc/sysctl.conf
sudo sysctl -p
```

### 2️⃣ Identify the Network Interface
Before configuring NAT, find out which network interface is being used for external connection (dn_interface):
```bash
ip a
```
On `Ubuntu Server 20.04 and 22.04`, the interfaces are usually `enp0s3` or `enp0s4`.

### 3️⃣ Configure NAT and Allow Forwarding
Once you have identified the correct interface, replace `<dn_interface>` in the commands below:

```bash
sudo iptables -t nat -A POSTROUTING -o <dn_interface> -j MASQUERADE
sudo iptables -I FORWARD 1 -j ACCEPT
```
These commands allow packets from `Free5GC` and `UERANSIM` to pass correctly to the network.

### 4️⃣ Make IPTables Rules Persistent
To ensure that iptables rules are automatically applied after reboots, install the iptables-persistent package:
```bash
sudo apt install -y iptables-persistent
```
Save the rules so they are automatically loaded at boot:

```bash
sudo netfilter-persistent save
sudo netfilter-persistent reload
```

### 5️⃣ 🔥 [Optional] Adjust or Disable UFW Firewall
The UFW firewall may block connections from Free5GC if not configured correctly.

If you have connection problems, add rules to release important ports:

```bash
sudo ufw allow 2152/udp
sudo ufw allow 50051/tcp
sudo ufw allow 8080/tcp
sudo ufw allow 9876/udp
```

If you need to disable it temporarily for testing:

```bash
sudo systemctl stop ufw
```
To disable it permanently:
```bash
sudo systemctl disable ufw
```
**Note: Disable the firewall only if necessary! If everything works correctly, keep UFW active with the appropriate permissions.**

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

#### 📌 Actions to be performed in the Free5GC WebConsole

1️⃣ Access the WebConsole via a browser:

🔗 `http://<FREE5GC_IP>:5000`
(Replace `<FREE5GC_IP>` with the correct Free5GC server IP)

2️⃣ Log in:

Username: `admin`, Password: `free5gc`

3️⃣ Navigate to the Subscribers section:

In the left sidebar menu, click on `Subscribers`.

4️⃣ Create a new UE:

Click the `New Subscriber` button.

5️⃣ Adjust the Operator Code Type:

Scroll down to `Operator Code Type`.
Change "OPc" to "OP".

6️⃣ Finalize the registration:

Leave all other fields unchanged.
Scroll to the bottom of the page and click `Submit`.

Now the UE is successfully registered in Free5GC! 

---

## 🚀 Running UERANSIM

### ▶️ Running gNB

On the `labora-UE-3GPP` host, run the following command to start the gNB:

```bash
cd ~/ueransim
./build/nr-gnb -c config/free5gc-gnb.yaml
```
- This starts the gNB and establishes the N2 (NGAP) and N3 (GTP-U) connections with Free5GC.
- Ensure the AMF is running on Free5GC before starting gNB.

### ▶️ Running UE

On the `labora-UE-3GPP` host, run the following command to start the UE simulation:

```bash
cd ~/ueransim
./build/nr-ue -c config/free5gc-ue.yaml
```
- This starts the UE and attempts to register with the Free5GC core.
- The UE should establish PDU sessions and get an IP address from the Free5GC network.

---

## ✅ Testing Data Connectivity

### 1️⃣ Check UE's assigned IP
```bash
ifconfig
```
- Look for the `uesimtun0` interface. If it exists, the UE is connected.
### 2️⃣ Ping Free5GC from UE
```bash
ping -I uesimtun0 60.60.0.1
```
- This tests if the UE can communicate with the Free5GC UPF.
### 3️⃣ Ping the Internet from UE
```bash
ping -I uesimtun0 google.com
```
- If the Free5GC core is properly forwarding traffic, you should get replies.

### 4️⃣ Traceroute to Google from UE
```bash
traceroute -i uesimtun0 google.com
```

### ❌ Test Deregistering UE
To manually deregister the UE from Free5GC:

```bash
sudo ./build/nr-cli imsi-208930000000001 --exec "deregister normal"
```
- This forces the UE to disconnect from the 5G network.

---
