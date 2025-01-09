# Installation

Instructions for setting up the repository.

# Installation Guide for Stoxus AI JupiterHub

Follow these steps to deploy the Stoxus AI jupiterHub platform.

## Prerequisites
- Python 3.8+
- AWS CLI configured
- pip installed

## Steps
1. Clone this repository:
   ```bash
   git clone https://github.com/StoxusAI/jupiterhub.git
   cd jupiterhub
2. Install dependencies:
   pip install -r launch_cluster/requirements.txt
3. Configure your secure settings:
4. Launch the cluster

---

### **vpc-with-one-managers-and-one-workers-subnets-template.json**
```json
{
  "Description": "Stoxus AI VPC setup for JupyterHub with one manager and one worker subnet",
  "Resources": {
    "VPC": {
      "Type": "AWS::EC2::VPC",
      "Properties": {
        "CidrBlock": "10.0.0.0/16",
        "Tags": [{"Key": "Name", "Value": "StoxusAI-VPC"}]
      }
    },
    "PublicSubnet": {
      "Type": "AWS::EC2::Subnet",
      "Properties": {
        "VpcId": {"Ref": "VPC"},
        "CidrBlock": "10.0.1.0/24",
        "MapPublicIpOnLaunch": true,
        "Tags": [{"Key": "Name", "Value": "StoxusAI-Public-Subnet"}]
      }
    },
    "PrivateSubnet": {
      "Type": "AWS::EC2::Subnet",
      "Properties": {
        "VpcId": {"Ref": "VPC"},
        "CidrBlock": "10.0.2.0/24",
        "Tags": [{"Key": "Name", "Value": "StoxusAI-Private-Subnet"}]
      }
    }
  }
}
