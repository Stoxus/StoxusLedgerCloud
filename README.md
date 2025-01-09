# **Stoxus LedgerCloud**

A scalable platform for hosting JupyterHub environments in the cloud, optimized for blockchain and crypto analytics, with automated resource scaling.

---

## **Overview**

**Stoxus LedgerCloud** enables seamless access to Jupyter Notebook environments for crypto professionals, analysts, and developers. Users can log in instantly and launch isolated cloud-based instances. Each user is allocated a dedicated server instance at login, which is paused when inactive to minimize resource costs.

This system is designed to handle the heavy computational demands of blockchain data analysis while maintaining efficiency and scalability.

---

## **System Deployment**

### **Setup**

1. Clone the project repository.
2. Create and configure the `secure.py` file based on the provided `secure.py.example` template.

---

### **Network Configuration**

#### **Virtual Private Network (VPN)**
- Deploy on a custom private network optimized for security and high throughput.
- Example configuration:
  ```plaintext
  VPN_ID = "vpn-xxxxxxxx"
  ```

#### **Access Keys**
Generate and securely store access keys for your private cloud instance:
```plaintext
KEY_NAME = "stoxus-key"
KEY_PATH = "/ABSOLUTE/PATH/TO/KEY/stoxus-key.pem"
```

#### **Subnets**
- **Private Subnet**: Used for individual user environments (worker nodes).
- **Public Subnet**: Hosts the main JupyterHub instance (manager node) to route user traffic.

---

### **Network Gateway**

To ensure private instances can access external crypto networks:

1. Set up a **Network Gateway** in the public subnet.
2. Route traffic from private instances through the gateway for secure blockchain data access.

---

### **Base Image**

- Use a lightweight and secure base operating system image, pre-configured for crypto and data analysis workflows.
- Ensure compatibility with distributed ledger libraries and analytics tools.

---

### **Deployment Script**

Install dependencies and configure the system as follows:

```bash
# Install dependencies
pip install -r launch_cluster/requirements.txt

# Create and configure secure.py
cp launch_cluster/secure.py.example launch_cluster/secure.py
nano launch_cluster/secure.py

# Launch the cluster
./launch_cluster/launch.py [CLUSTER_NAME] [BASE_IMAGE_ID] [PRIVATE_SUBNET_ID] [PUBLIC_SUBNET_ID]
```

---

## **How LedgerCloud Works**

Upon launch, the system creates:

- **Security Policies**: Enforcing access control between manager and worker nodes.
- **Cloud Instances**:
  - **Manager Node**: Hosts the JupyterHub service for user access.
  - **Worker Nodes**: Dedicated environments for user computations and blockchain analysis.

These resources are managed dynamically to scale up or down based on active users.

---

### **Default Assumptions**

1. Manager instances can deploy, terminate, and manage worker nodes.
2. Network routes are preconfigured for optimal traffic flow and blockchain data integration.
3. Resource limits (e.g., server counts) are sufficient for projected user activity.

---

## **Running Secure Clusters**

To run your LedgerCloud environment securely:

- Enable SSL/TLS encryption for all communications.
- Place SSL certificates in `/etc/jupyterhub/ssl/` on the manager node.
- Update your `jupyterhub_config.py` with the required certificate paths.

---

## **Authentication**

Stoxus LedgerCloud supports multiple authentication methods tailored for crypto professionals:

- **Custom Blockchain Wallet Authentication**: Log in using wallet credentials or cryptographic keys.
- **OAuth Integration**: Connect via popular decentralized identity providers.

Admins can bulk add users and assign permissions through the manager interface.

---

## **Configuring LedgerCloud**

### **Key Configuration Files**

1. **`jupyterhub_config.py`**
   - Central configuration for user access and authentication.

2. **`server_config.json`**
   - Manage session timeouts and resource allocations.
   - Adjust the inactivity timeout (`NOTEBOOK_TIMEOUT`, default: 1 hour).

3. **`instance_config.json`**
   - Configure server types for worker and manager nodes.
   - Specify custom base images tailored for blockchain data analysis.

---

## **Terminating a Cluster**

To shut down your LedgerCloud environment:

1. Run the cleanup script to terminate all active worker nodes:
   ```bash
   ./terminate_all_workers.py
   ```
2. Delete the manager instance, security policies, and any associated snapshots.

---

## **Optimized for Blockchain Analytics**

**Stoxus LedgerCloud** has been fine-tuned for crypto professionals. Features include:

- Pre-installed libraries for interacting with blockchain APIs and analyzing transaction data.
- Scalable environments for running smart contract simulations and on-chain analytics.
- Secure integration with decentralized networks.

---

## **Development Notes**

Earlier versions of LedgerCloud relied on containerized environments, but the transition to isolated server instances has provided:

- **Enhanced Security**: Individual environments minimize risks of privilege escalation and resource leaks.
- **Improved Performance**: Reduced latency and optimized server utilization during high-demand periods.
- **Simplified Maintenance**: Eliminates compatibility issues with container orchestration tools.

---

**Stoxus LedgerCloud** offers a powerful, secure, and scalable solution for blockchain-focused analytics and computations. For more details, visit [Stoxus](https://ai.stoxus.com).
