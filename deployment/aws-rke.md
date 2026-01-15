---
title: Amazon Web Services (RKE)
nav_order: 9
parent: Deployment
grand_parent: TrustGraph Documentation
review_date: 2026-05-02
guide_category:
  - Global cloud
guide_category_order: 1
guide_description: Production-ready RKE2 Kubernetes cluster on AWS with Bedrock AI integration
guide_difficulty: advanced
guide_time: 2 - 5 hr
guide_emoji: ☁️
guide_banner: rke.png
guide_labels:
  - AWS
  - Kubernetes
  - Production
---

# Amazon Web Services (RKE) Deployment

{% capture requirements %}
<ul style="margin: 0; padding-left: 20px;">
<li>AWS account with appropriate permissions (see below for setup)</li>
<li>AWS CLI installed and configured</li>
<li>Pulumi installed locally</li>
<li>kubectl command-line tool</li>
<li>Python {{site.data.software.python-min-version}}+ for CLI tools</li>
<li>SSH key pair for EC2 access</li>
<li>Basic command-line and Kubernetes familiarity</li>
</ul>
{% endcapture %}

{% include guide/guide-intro-box.html
   description=page.guide_description
   difficulty=page.guide_difficulty
   duration=page.guide_time
   you_will_need=requirements
   goal="Deploy a production-ready TrustGraph environment on AWS using RKE2 Kubernetes with AWS Bedrock integration and security hardening."
%}

## Overview

This guide walks you through deploying TrustGraph on Amazon Web Services using RKE2 (Rancher Kubernetes Engine 2) via Pulumi (Infrastructure as Code). The deployment automatically provisions a production-ready, security-hardened Kubernetes cluster integrated with AWS Bedrock for LLM capabilities.

**Pulumi** is an open-source Infrastructure as Code tool that uses general-purpose programming languages (TypeScript/JavaScript in this case) to define cloud infrastructure. Unlike manual deployments, Pulumi provides:
- Reproducible, version-controlled infrastructure
- Testable and retryable deployments
- Automatic resource dependency management
- Simple rollback capabilities

**RKE2** (Rancher Kubernetes Engine 2) is a fully conformant Kubernetes distribution that focuses on security and compliance:
- FIPS 140-2 compliance ready
- CIS Kubernetes Benchmark hardened
- Simplified operations with embedded etcd
- Government and enterprise security requirements

Once deployed, you'll have a complete TrustGraph stack running on AWS infrastructure with:
- RKE2 Kubernetes cluster (3-node setup, configurable)
- AWS Bedrock integration (Claude 3.5 Haiku default)
- EBS CSI driver for persistent storage
- Complete monitoring with Grafana and Prometheus
- Web workbench for document processing and Graph RAG
- Secure IAM roles and policies

{: .note }
> **Why AWS RKE2 for TrustGraph?**
>
> AWS with RKE2 offers unique advantages for security-focused organizations:
> - **Security Hardening**: RKE2 is CIS Benchmark hardened and FIPS 140-2 ready
> - **AWS Bedrock**: Native access to Claude, Mistral, and other frontier models
> - **Government Ready**: Meets stringent government and enterprise security requirements
> - **AWS Integration**: Seamless integration with AWS services (EBS, IAM, VPC, etc.)
> - **Global Infrastructure**: Deploy across AWS's global network of regions
>
> Ideal for organizations requiring high security standards and compliance.

## Getting ready

### AWS Account

You'll need an AWS account with appropriate permissions. If you don't have one:

1. Sign up at [https://aws.amazon.com/](https://aws.amazon.com/)
2. Complete account verification
3. Set up billing
4. AWS Free Tier includes 750 hours/month of EC2 for 12 months

### AWS Permissions Required

Your AWS user/role needs permissions for:
- EC2 (instances, VPC, security groups, key pairs)
- IAM (roles, policies, instance profiles)
- EBS (volumes, snapshots)
- Bedrock (model access)

### Install AWS CLI

Install the AWS command-line tool:

<details>
<summary>Linux</summary>
<div markdown="1">
```bash
curl "https://awscli.amazonaws.com/awscli-exe-linux-x86_64.zip" -o "awscliv2.zip"
unzip awscliv2.zip
sudo ./aws/install
```
</div>
</details>

<details>
<summary>MacOS</summary>
<div markdown="1">
```bash
curl "https://awscli.amazonaws.com/AWSCLIV2.pkg" -o "AWSCLIV2.pkg"
sudo installer -pkg AWSCLIV2.pkg -target /
```
</div>
</details>

<details>
<summary>Windows</summary>
<div markdown="1">
Download the installer from [aws.amazon.com/cli](https://aws.amazon.com/cli/)
</div>
</details>

Verify installation:

```bash
aws --version
```

### Configure AWS Credentials

Configure your AWS credentials:

```bash
aws configure
```

You'll be prompted for:
- AWS Access Key ID
- AWS Secret Access Key
- Default region (e.g., `us-west-2`)
- Default output format (recommend `json`)

Verify configuration:

```bash
aws sts get-caller-identity
```

### Enable AWS Bedrock Models

AWS Bedrock requires explicit model access enablement:

1. Navigate to the [AWS Bedrock Console](https://console.aws.amazon.com/bedrock/)
2. Select your deployment region
3. Go to **Model access** in the left navigation
4. Click **Manage model access**
5. Enable access to:
   - **Anthropic Claude 3.5 Haiku** (recommended default)
   - **Mistral Nemo Instruct** (optional alternative)
   - Any other models you want to use
6. Submit request (usually approved immediately for most models)

{: .warning }
> Model access must be enabled in the same region where you'll deploy TrustGraph.

### Create SSH Key Pair

Create an SSH key pair for EC2 instance access:

```bash
aws ec2 create-key-pair \
  --key-name trustgraph-key \
  --query 'KeyMaterial' \
  --output text > ~/.ssh/trustgraph-key.pem

chmod 400 ~/.ssh/trustgraph-key.pem
```

### Python

{% include deployment/python-requirement.md %}

### Pulumi

{% include deployment/pulumi-install.md %}

### kubectl

{% include deployment/kubectl-install.md %}

### Node.js

{% include deployment/nodejs-install.md %}

## Prepare the deployment

### Get the Pulumi code

Clone the TrustGraph AWS RKE Pulumi repository:

```bash
git clone https://github.com/trustgraph-ai/pulumi-trustgraph-aws-rke.git
cd pulumi-trustgraph-aws-rke/pulumi
```

### Install dependencies

Install the Node.js dependencies for the Pulumi project:

```bash
npm install
```

### Configure Pulumi state

{% include deployment/pulumi-configure-state.md %}

### Create a Pulumi stack

{% include deployment/pulumi-create-stack.md %}

### Configure the stack

Apply settings for AWS region, environment, and infrastructure:

```bash
pulumi config set aws:region us-west-2
pulumi config set environment prod
pulumi config set keyName trustgraph-key
pulumi config set instanceType t3a.xlarge
pulumi config set nodeCount 3
```

Available AWS regions include:
- `us-east-1` (N. Virginia)
- `us-west-2` (Oregon)
- `eu-west-1` (Ireland)
- `eu-central-1` (Frankfurt)
- `ap-southeast-1` (Singapore)
- `ap-northeast-1` (Tokyo)

Refer to [AWS Regions](https://aws.amazon.com/about-aws/global-infrastructure/regions_az/) for a complete list.

### Configure AWS Bedrock

Set the Bedrock model to use:

```bash
pulumi config set bedrockModel anthropic.claude-3-5-haiku-20241022-v1:0
```

Available Bedrock models include:
- `anthropic.claude-3-5-haiku-20241022-v1:0` (fast, cost-effective)
- `anthropic.claude-3-5-sonnet-20241022-v2:0` (balanced performance)
- `mistral.mistral-nemo-instruct-2407-v1:0` (open source)

Refer to the repository's README for more model options.

### Configure VPC Settings (Optional)

Customize network configuration if needed:

```bash
pulumi config set vpcCidr 172.38.0.0/16
pulumi config set subnetCidr 172.38.1.0/24
```

## Deploy with Pulumi

### Preview the deployment

Before deploying, preview what Pulumi will create:

```bash
pulumi preview
```

This shows all the resources that will be created:
- VPC with custom CIDR block
- Subnet and Internet Gateway
- Security groups for RKE2 cluster
- IAM roles and policies (with Bedrock permissions)
- EC2 instances for Kubernetes nodes
- EBS volumes for persistent storage
- RKE2 cluster configuration
- EBS CSI driver deployment
- TrustGraph deployments, services, and config maps

Review the output to ensure everything looks correct.

### Deploy the infrastructure

Deploy the complete TrustGraph stack:

```bash
pulumi up
```

Pulumi will ask for confirmation before proceeding. Type `yes` to continue.

The deployment typically takes 12 - 18 minutes and progresses through these stages:

1. **Creating AWS infrastructure** (3-5 minutes)
   - Creates VPC, subnet, and networking
   - Provisions security groups
   - Creates IAM roles and policies

2. **Launching EC2 instances** (2-3 minutes)
   - Launches RKE2 server node
   - Launches RKE2 agent nodes
   - Attaches EBS volumes

3. **Installing RKE2** (5-7 minutes)
   - Installs RKE2 on server node
   - Installs RKE2 on agent nodes
   - Forms Kubernetes cluster

4. **Deploying TrustGraph** (4-6 minutes)
   - Installs EBS CSI driver
   - Applies Kubernetes manifests
   - Deploys all TrustGraph services
   - Starts pods and initializes services

You'll see output showing the creation progress of all resources.

{: .note }
> **Post-deployment initialization**: After all pods show "Running" status, wait an additional 30 seconds for internal service initialization to complete before running verification commands.

### Configure and verify kubectl access

After deployment completes, a kubeconfig file is created for cluster access:

```bash
export KUBECONFIG=$(pwd)/kubeconfig.yaml
```

Verify access:

```bash
kubectl get nodes
```

You should see your RKE2 nodes listed as `Ready`.

### Check pod status

{% include kubernetes/check-pod-status.md %}

## Access services via port-forwarding

{% include kubernetes/port-forwarding.md %}

## Install CLI tools

{% include deployment/install-cli-tools.md %}

## Startup period

It can take 2-3 minutes for all services to stabilize after deployment. Services like Pulsar and Cassandra need time to initialize properly. Additionally, wait 30 seconds after pods show "Running" status for internal initialization.

### Verify system health

{% include deployment/application-localhost/verify-system-health.md %}

If everything appears to be working, the following parts of the deployment guide are a whistle-stop tour through various parts of the system.

## Test LLM access

Test that AWS Bedrock integration is working by invoking the LLM through the gateway:

```bash
tg-invoke-llm 'Be helpful' 'What is 2 + 2?'
```

You should see output like:

```
2 + 2 = 4
```

This confirms that TrustGraph can successfully communicate with AWS Bedrock.

## Load sample documents

{% include deployment/application-localhost/load-sample-documents.md %}

## Workbench

{% include deployment/application-localhost/workbench.md %}

## Monitoring dashboard

{% include deployment/application-localhost/monitoring-dashboard.md %}

## Check the LLM is working

{% include deployment/workbench/check-llm-working.md %}

## Working with a document

### Load a document

{% include deployment/workbench/load-document.md %}

### Use Vector search

{% include deployment/workbench/vector-search.md %}

### Look at knowledge graph

{% include deployment/workbench/knowledge-graph.md %}

### Query with Graph RAG

{% include deployment/workbench/graph-rag-query.md %}

## Troubleshooting

### Deployment Issues

<details>
<summary>Pulumi deployment fails</summary>
<div markdown="1">

*Diagnosis:*

Check the Pulumi error output for specific failure messages. Common issues include:

```bash
# View detailed error information
pulumi stack --show-urns
pulumi logs
```

*Resolution:*

- **Authentication errors**: Verify AWS credentials are configured correctly (`aws configure`)
- **Permission issues**: Ensure your AWS user/role has necessary permissions (EC2, IAM, VPC)
- **Key pair not found**: Verify the SSH key pair exists: `aws ec2 describe-key-pairs --key-names trustgraph-key`
- **Quota limits**: Check AWS service quotas for EC2 instances, VPCs, and EBS volumes
- **Region mismatch**: Ensure Bedrock model access is enabled in your deployment region

</div>
</details>

<details>
<summary>RKE2 cluster fails to form</summary>
<div markdown="1">

*Diagnosis:*

Check EC2 instance logs:

```bash
# Get instance IDs from Pulumi output
pulumi stack output

# SSH to server node
ssh -i ~/.ssh/trustgraph-key.pem ec2-user@SERVER_IP

# Check RKE2 server logs
sudo journalctl -u rke2-server -f
```

*Resolution:*

- Verify security group rules allow inter-node communication
- Check that all nodes can reach the RKE2 server node
- Ensure sufficient resources on EC2 instances
- Review cloud-init logs: `sudo cat /var/log/cloud-init-output.log`

</div>
</details>

<details>
<summary>Pods stuck in Pending state</summary>
<div markdown="1">

*Diagnosis:*

```bash
kubectl -n trustgraph get pods | grep Pending
kubectl -n trustgraph describe pod <pod-name>
```

Look for scheduling failures or resource constraints in the describe output.

*Resolution:*

- **Insufficient resources**: Increase instance type or node count in Pulumi configuration
- **EBS CSI driver issues**: Check CSI driver pods: `kubectl -n kube-system get pods | grep ebs-csi`
- **PersistentVolume issues**: Check PV/PVC status: `kubectl -n trustgraph get pv,pvc`
- **Node issues**: Check node status and resources: `kubectl describe nodes`

</div>
</details>

<details>
<summary>AWS Bedrock integration not working</summary>
<div markdown="1">

*Diagnosis:*

Test LLM connectivity:

```bash
tg-invoke-llm '' 'What is 2+2'
```

A timeout or error indicates Bedrock configuration issues. Check the `text-completion` pod logs:

```bash
kubectl -n trustgraph logs -l app=text-completion
```

*Resolution:*

- Verify Bedrock model access is enabled in AWS Console for your region
- Check IAM role has Bedrock permissions: `aws iam get-role-policy --role-name trustgraph-bedrock-role --policy-name BedrockAccess`
- Ensure the model ID is correct in configuration
- Verify region matches between deployment and Bedrock model access
- Check AWS service quotas for Bedrock

</div>
</details>

<details>
<summary>Port-forwarding connection issues</summary>
<div markdown="1">

*Diagnosis:*

Port-forward commands fail or connections time out.

*Resolution:*

- Verify kubeconfig is set: `echo $KUBECONFIG`
- Check that the target service exists: `kubectl -n trustgraph get svc`
- Ensure no other process is using the port (e.g., port 8088, 8888, or 3000)
- Try restarting the port-forward with verbose logging: `kubectl port-forward -v=6 ...`
- Verify RKE2 cluster is healthy: `kubectl get nodes`

</div>
</details>

### Service Failure

<details>
<summary>Pods in CrashLoopBackOff</summary>
<div markdown="1">

*Diagnosis:*

```bash
# Find crashing pods
kubectl -n trustgraph get pods | grep CrashLoopBackOff

# View logs from crashed container
kubectl -n trustgraph logs <pod-name> --previous
```

*Resolution:*

Check the logs to identify why the container is crashing. Common causes:
- Application errors (configuration issues)
- Missing dependencies (ensure all required services are running)
- Incorrect secrets or environment variables
- Resource limits too low
- AWS credentials not properly configured

</div>
</details>

<details>
<summary>EBS volume attachment failures</summary>
<div markdown="1">

*Diagnosis:*

Check EBS CSI driver logs:

```bash
kubectl -n kube-system logs -l app=ebs-csi-controller
```

*Resolution:*

- Verify EBS CSI driver is installed correctly
- Check IAM permissions for EBS operations
- Ensure availability zone matches between PVC and node
- Check AWS service limits for EBS volumes

</div>
</details>

### AWS-Specific Issues

<details>
<summary>EC2 instances fail to launch</summary>
<div markdown="1">

*Diagnosis:*

Check AWS EC2 console or CLI:

```bash
aws ec2 describe-instances --filters "Name=tag:Name,Values=trustgraph-*"
```

*Resolution:*

- Verify AWS service quotas for EC2 instances in your region
- Request quota increases if needed via AWS Console
- Try a different instance type if capacity is unavailable
- Check if AMI is available in your region
- Verify VPC and subnet configuration

</div>
</details>

<details>
<summary>Bedrock throttling errors</summary>
<div markdown="1">

*Diagnosis:*

Error messages about Bedrock rate limits or throttling in `text-completion` logs.

*Resolution:*

- Check Bedrock quotas in AWS Console under "Service Quotas"
- Request quota increases if needed
- Switch to a different Bedrock model with higher quotas
- Implement request rate limiting in your application
- Consider using provisioned throughput for production workloads

</div>
</details>

## SSH Access to Nodes

To troubleshoot or manage RKE2 nodes directly:

```bash
# Get server node IP from Pulumi output
pulumi stack output serverPublicIp

# SSH to server node
ssh -i ~/.ssh/trustgraph-key.pem ec2-user@SERVER_IP

# Common RKE2 commands
sudo systemctl status rke2-server
sudo journalctl -u rke2-server -f
sudo kubectl get nodes
```

## Shutting down

### Clean shutdown

When you're finished with your TrustGraph deployment, clean up all resources:

```bash
pulumi destroy
```

Pulumi will show you all the resources that will be deleted and ask for confirmation. Type `yes` to proceed.

The destruction process typically takes **8-12 minutes** and removes:
- All TrustGraph Kubernetes resources
- RKE2 cluster components
- All EC2 instances
- EBS volumes
- IAM roles and policies
- Security groups
- VPC and networking components (if created by Pulumi)

{: .warning }
> **Cost Warning**: AWS charges for running EC2 instances, EBS storage, data transfer, and Bedrock API calls. Make sure to destroy your deployment when you're not using it to avoid unnecessary costs.

### Verify cleanup

After `pulumi destroy` completes, verify all resources are removed:

```bash
# Check Pulumi stack status
pulumi stack

# Verify no resources remain
pulumi stack --show-urns

# Check AWS for remaining resources
aws ec2 describe-instances --filters "Name=tag:Name,Values=trustgraph-*"
aws ec2 describe-volumes --filters "Name=tag:Name,Values=trustgraph-*"
```

### Delete the Pulumi stack

If you're completely done with this deployment, you can remove the Pulumi stack:

```bash
pulumi stack rm dev
```

This removes the stack's state but doesn't affect any cloud resources (use `pulumi destroy` first).

## Cost Optimization

### Monitor Costs

Keep track of your AWS spending:

1. Navigate to **Cost Explorer** in AWS Console
2. View cost breakdown by service
3. Set up billing alerts

### Cost-Saving Tips

- **Spot Instances**: Use EC2 Spot instances for non-production workloads (up to 90% cheaper)
- **Right-size instances**: Choose instance types based on actual usage
- **Reserved Instances**: Purchase reserved instances for production (up to 72% savings)
- **Stop non-production**: Stop dev/test instances when not in use
- **EBS optimization**: Use gp3 volumes instead of gp2, delete unused snapshots
- **Bedrock optimization**: Cache responses, implement rate limiting, choose cost-effective models

Example cost estimates (us-west-2):
- **3 x t3a.xlarge instances**: ~$0.15/hour each = ~$330/month
- **EBS volumes**: ~$50-80/month (depends on size and IOPS)
- **Data transfer**: First 100GB/month free, then $0.09/GB
- **Bedrock API**: Pay per request (varies by model)
- **Total estimated**: ~$400-500/month for basic deployment (plus Bedrock usage)

## Security Hardening

RKE2 comes with security hardening by default, but additional steps can enhance security:

### Network Security

- Restrict security group ingress rules to only necessary ports
- Use AWS WAF for web application firewall protection
- Enable VPC Flow Logs for network traffic analysis
- Consider using AWS PrivateLink for service access

### Access Control

- Enable AWS CloudTrail for API activity logging
- Use IAM roles instead of access keys where possible
- Implement least privilege IAM policies
- Enable MFA for AWS console access
- Rotate SSH keys regularly

### Compliance

- Run CIS benchmark scans on RKE2 cluster
- Enable AWS Config for compliance monitoring
- Use AWS Security Hub for centralized security findings
- Consider AWS GuardDuty for threat detection

## Next Steps

Now that you have TrustGraph running on AWS with RKE2:

- **Guides**: See [Guides](../guides) for things you can do with your running TrustGraph
- **Scale the cluster**: Add more agent nodes or increase instance sizes
- **Production hardening**: Implement additional security controls and monitoring
- **High availability**: Deploy across multiple availability zones
- **Integrate AWS services**: Connect to S3, RDS, DynamoDB, or other AWS services
- **CI/CD**: Set up AWS CodePipeline or GitHub Actions for automated deployments
- **Monitoring**: Integrate with CloudWatch and AWS X-Ray
- **Bedrock models**: Explore other Bedrock models (Claude, Mistral, LLaMA, etc.)
- **Custom models**: Consider Amazon SageMaker for custom model hosting

{: .note }
> **Additional Resources**
>
> - [TrustGraph AWS RKE Pulumi Repository](https://github.com/trustgraph-ai/pulumi-trustgraph-aws-rke) - Full source code and configuration
> - [RKE2 Documentation](https://docs.rke2.io/) - Learn more about RKE2
> - [AWS Bedrock Documentation](https://docs.aws.amazon.com/bedrock/) - Explore Bedrock capabilities
> - [AWS Well-Architected Framework](https://aws.amazon.com/architecture/well-architected/) - Best practices for AWS
