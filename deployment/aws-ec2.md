---
title: AWS EC2 Single Instance
nav_order: 7
parent: Deployment
grand_parent: TrustGraph Documentation
review_date: 2026-01-20
guide_category:
  - Standalone deployment
guide_category_order: 3
guide_description: Single AWS EC2 instance with Podman for development, testing, and small-scale deployments
guide_difficulty: advanced
guide_time: 2 - 5 hr
guide_emoji: 🖥️
guide_banner: aws-ec2.png
guide_labels:
  - AWS
  - Podman
  - Development
---

# AWS EC2 Single Instance Deployment

{% capture requirements %}
<ul style="margin: 0; padding-left: 20px;">
<li>AWS account with access to Bedrock (see below for setup)</li>
<li>AWS CLI installed and configured</li>
<li>Pulumi installed locally</li>
<li>Python {{site.data.software.python-min-version}}+ for CLI tools</li>
<li>Basic command-line familiarity</li>
</ul>
{% endcapture %}

{% include guide/guide-intro-box.html
   description=page.guide_description
   difficulty=page.guide_difficulty
   duration=page.guide_time
   you_will_need=requirements
   goal="Deploy a TrustGraph development environment on a single AWS EC2 instance with Podman containers and AWS Bedrock integration using Infrastructure as Code."
%}

## Overview

This guide walks you through deploying TrustGraph on a single AWS EC2 instance using Pulumi (Infrastructure as Code). The deployment automatically provisions an EC2 instance running Podman containers integrated with AWS Bedrock for LLM services.

**Pulumi** is an open-source Infrastructure as Code tool that uses general-purpose programming languages (TypeScript/JavaScript in this case) to define cloud infrastructure. Unlike manual deployments, Pulumi provides:
- Reproducible, version-controlled infrastructure
- Testable and retryable deployments
- Automatic resource dependency management
- Simple rollback capabilities

Once deployed, you'll have a complete TrustGraph stack running on AWS infrastructure with:
- Single EC2 instance (t3.2xlarge, configurable)
- AWS Bedrock integration (Claude 3.5 Haiku)
- Complete monitoring with Grafana and Prometheus
- Web workbench for document processing and Graph RAG
- Secure IAM role-based authentication

{: .warning }
> **Development Deployment Only**
>
> This single instance deployment is appropriate for:
> - Development and testing
> - Experimentation and learning
> - Quick prototyping
> - Analysis and evaluation
>
> **Not recommended for production use** - this deployment has no redundancy
> or resilience. It also may be complex to securely integrate a docker
> deployment with AWS VPCs for inter-service  networking.
> 
> For production deployments, consider:
> - [AWS RKE Deployment](aws-rke) - Multi-node Kubernetes cluster

{: .note }
> **Why AWS EC2 Single Instance for TrustGraph?**
>
> AWS EC2 single instance deployment offers unique advantages for development:
> - **Simple Setup**: No complex Kubernetes configuration required
> - **Direct Access**: SSH directly to the instance for debugging
> - **Cost-Effective**: Lower cost than multi-node clusters for testing
> - **AWS Bedrock Integration**: Native access to Claude and other foundation models
> - **Automatic Credentials**: IAM role handles authentication without key management
> - **Rapid Iteration**: Quick deployment and teardown cycles
>
> Ideal for developers, researchers, and teams evaluating TrustGraph capabilities before production deployment.

## Getting ready

### AWS Account

You'll need an AWS account with access to AWS Bedrock. If you don't have one:

1. Sign up at [https://aws.amazon.com/](https://aws.amazon.com/)
2. Complete account verification
3. Set up billing (new accounts receive free tier benefits)

### Enable AWS Bedrock Models

AWS Bedrock requires explicit model access enablement:

1. Navigate to the [AWS Bedrock Console](https://console.aws.amazon.com/bedrock/)
2. Select your deployment region (e.g., `us-east-1`)
3. Go to **Model access** in the left navigation
4. Click **Manage model access**
5. Enable access to:
   - **Anthropic Claude 3.5 Haiku** (recommended default)
   - **Mistral Nemo Instruct** (optional alternative)
   - Other models as desired
6. Click **Save changes**

Model availability varies by region. See [AWS Bedrock model availability](https://docs.aws.amazon.com/bedrock/latest/userguide/models-regions.html).

### Install AWS CLI

Install the AWS Command Line Interface:

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

Or via Homebrew:

```bash
brew install awscli
```
</div>
</details>

<details>
<summary>Windows</summary>
<div markdown="1">
Download the installer from [aws.amazon.com/cli/](https://aws.amazon.com/cli/)
</div>
</details>

Verify installation:

```bash
aws --version
```

### Configure AWS Authentication

Configure AWS credentials for Pulumi deployment:

```bash
aws configure
```

Provide:
- **AWS Access Key ID**: Your access key
- **AWS Secret Access Key**: Your secret key
- **Default region**: e.g., `us-east-1`
- **Default output format**: `json`

Alternatively, use AWS profiles:

```bash
export AWS_PROFILE=your-profile-name
```

### Python

{% include deployment/python-requirement.md %}

### Pulumi

{% include deployment/pulumi-install.md %}

### Node.js

{% include deployment/nodejs-install.md %}

## Prepare the deployment

### Get the Pulumi code

Clone the TrustGraph AWS EC2 Pulumi repository:

```bash
git clone https://github.com/trustgraph-ai/pulumi-trustgraph-ec2.git
cd pulumi-trustgraph-ec2/pulumi
```

### Install dependencies

Install the Node.js dependencies for the Pulumi project:

```bash
npm install
```

### Configure AWS region

Set your AWS region for Pulumi:

```bash
pulumi config set aws:region us-east-1
```

Available Bedrock regions include:
- `us-east-1` (N. Virginia)
- `us-west-2` (Oregon)
- `eu-central-1` (Frankfurt)
- `ap-southeast-1` (Singapore)
- `ap-northeast-1` (Tokyo)

Refer to [AWS Bedrock regions](https://docs.aws.amazon.com/bedrock/latest/userguide/bedrock-regions.html) for a complete list.

### Configure Pulumi state

{% include deployment/pulumi-configure-state.md %}

### Create a Pulumi stack

{% include deployment/pulumi-create-stack.md %}

### Configure the stack

Apply settings for instance type and AWS Bedrock model:

```bash
pulumi config set instanceType t3.2xlarge
pulumi config set bedrockModel anthropic.claude-3-5-haiku-20241022-v1:0
```

Available instance types:
- `t3.2xlarge` - 8 vCPUs, 32 GB RAM (recommended)
- `t3.xlarge` - 4 vCPUs, 16 GB RAM (minimum)
- `m5.2xlarge` - 8 vCPUs, 32 GB RAM (better performance)
- `m5.4xlarge` - 16 vCPUs, 64 GB RAM (high performance)

Available Bedrock models:
- `anthropic.claude-3-5-haiku-20241022-v1:0` (fast, cost-effective)
- `anthropic.claude-3-5-sonnet-20241022-v2:0` (advanced reasoning)
- `mistral.mistral-nemo-instruct-2407-v1:0` (alternative)

Refer to the repository's README for additional configuration options.

## Deploy with Pulumi

### Preview the deployment

Before deploying, preview what Pulumi will create:

```bash
pulumi preview
```

This shows all the resources that will be created:
- EC2 instance with specified type
- IAM role with Bedrock permissions
- Security group for SSH access
- EBS volumes for storage
- SSH key pair for instance access
- Elastic IP for static addressing
- User data script for automatic setup

Review the output to ensure everything looks correct.

### Deploy the infrastructure

Deploy the complete TrustGraph stack:

```bash
pulumi up
```

Pulumi will ask for confirmation before proceeding. Type `yes` to continue.

The deployment typically takes 10 - 15 minutes and progresses through these stages:

1. **Creating EC2 infrastructure** (2-3 minutes)
   - Provisions EC2 instance
   - Creates IAM role and instance profile
   - Sets up security groups
   - Assigns Elastic IP

2. **Configuring instance** (5-8 minutes)
   - Installs Podman and dependencies
   - Downloads TrustGraph containers
   - Configures Podman Compose
   - Sets up AWS Bedrock integration

3. **Starting TrustGraph** (3-5 minutes)
   - Starts all containers
   - Initializes services
   - Runs health checks

You'll see output showing the creation progress of all resources.

### Retrieve deployment outputs

After deployment completes, Pulumi will display important outputs:

```bash
pulumi stack output
```

Key outputs:
- `instanceIp` - Public IP address of the EC2 instance
- `sshCommand` - Command to SSH to the instance
- `privateKey` - SSH private key (saved to `ssh-private.key`)

The SSH private key is automatically saved to `ssh-private.key` in the current directory.

### Set SSH key permissions

Set correct permissions on the SSH private key:

```bash
chmod 600 ssh-private.key
```

## Access the instance

### SSH access with port forwarding

Access the instance with SSH port forwarding for web services:

```bash
ssh -L 3000:localhost:3000 -L 8888:localhost:8888 -L 8088:localhost:8088 \
    -i ssh-private.key ubuntu@$(pulumi stack output instanceIp)
```

This creates port forwards for:
- Port 3000 - Grafana monitoring dashboard
- Port 8888 - TrustGraph web workbench
- Port 8088 - TrustGraph API gateway

### Verify container status

Once connected via SSH, verify all containers are running:

```bash
sudo podman ps -a
```

All containers should show `Up` status. If some containers are still starting, wait 1-2 minutes and check again.

## Install CLI tools

{% include deployment/install-cli-tools.md %}

## Startup period

It can take 2-3 minutes for all services to stabilize after deployment. Services like Pulsar and Cassandra need time to initialize properly.

### Verify system health

{% include deployment/application-localhost/verify-system-health.md %}

If everything appears to be working, the following parts of the deployment guide are a whistle-stop tour through various parts of the system.

## Test LLM access

{% include deployment/application-localhost/test-llm-access.md %}

This confirms that TrustGraph can successfully communicate with AWS Bedrock service.

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

- **Authentication errors**: Verify AWS credentials are configured (`aws configure` or `AWS_PROFILE`)
- **Bedrock access denied**: Ensure Bedrock model access is enabled in your region
- **Quota limits**: Check your AWS account hasn't hit EC2 instance quotas
- **Region availability**: Verify the instance type is available in your selected region
- **Permissions**: Ensure your AWS user/role has EC2, IAM, and Bedrock permissions

</div>
</details>

<details>
<summary>Instance launches but containers don't start</summary>
<div markdown="1">

*Diagnosis:*

SSH to the instance and check container status:

```bash
ssh -i ssh-private.key ubuntu@$(pulumi stack output instanceIp)
sudo podman ps -a
sudo journalctl -u podman-compose -n 100
```

*Resolution:*

- **Container pull failures**: Check internet connectivity and container registry access
- **Resource constraints**: Verify instance type has sufficient memory (minimum t3.xlarge)
- **Podman configuration issues**: Review `/var/log/cloud-init-output.log` for setup errors
- **Port conflicts**: Ensure no other services are using required ports

</div>
</details>

<details>
<summary>AWS Bedrock integration not working</summary>
<div markdown="1">

*Diagnosis:*

Test Bedrock connectivity from the instance:

```bash
# SSH to instance
ssh -i ssh-private.key ubuntu@$(pulumi stack output instanceIp)

# Test LLM
tg-invoke-llm '' 'What is 2+2'
```

Check the `text-completion` container logs:

```bash
sudo podman logs $(sudo podman ps -q -f name=text-completion)
```

*Resolution:*

- Verify Bedrock model access is enabled in AWS Console
- Check IAM role has `bedrock:InvokeModel` permission
- Ensure the model ID is correct for your region
- Verify instance profile is attached: `aws sts get-caller-identity`
- Check Bedrock service quotas haven't been exceeded

</div>
</details>

<details>
<summary>SSH connection fails</summary>
<div markdown="1">

*Diagnosis:*

Verify instance is running and accessible:

```bash
# Check instance state
aws ec2 describe-instances --filters "Name=tag:Name,Values=trustgraph-ec2"

# Verify security group allows SSH
aws ec2 describe-security-groups --group-ids $(pulumi stack output securityGroupId)
```

*Resolution:*

- Verify SSH key permissions: `chmod 600 ssh-private.key`
- Check your IP is allowed in security group (may need to update)
- Ensure instance has public IP assigned
- Verify instance state is `running`
- Check CloudWatch Logs for instance startup issues

</div>
</details>

### Service Failure

<details>
<summary>Containers in restart loop</summary>
<div markdown="1">

*Diagnosis:*

```bash
# Find restarting containers
sudo podman ps -a | grep Restarting

# View logs from container
sudo podman logs <container-name>
```

*Resolution:*

Check the logs to identify why the container is restarting. Common causes:
- Application errors (configuration issues)
- Missing dependencies (ensure all required containers are running)
- Incorrect environment variables
- Resource limits too low (increase instance size)
- AWS credentials not properly available via IAM role

</div>
</details>

<details>
<summary>Service not responding</summary>
<div markdown="1">

*Diagnosis:*

Check service status:

```bash
sudo podman ps
sudo podman logs <container-name>
```

*Resolution:*

- Verify the container is running
- Check container logs for errors
- Ensure port-forwarding is active in your SSH session
- Use `tg-verify-system-status` to check overall system health
- Restart specific container: `sudo podman restart <container-name>`

</div>
</details>

### AWS-Specific Issues

<details>
<summary>Instance out of memory</summary>
<div markdown="1">

*Diagnosis:*

Check memory usage on the instance:

```bash
free -h
top
```

*Resolution:*

- Upgrade to larger instance type (e.g., t3.2xlarge → m5.2xlarge)
- Update Pulumi configuration: `pulumi config set instanceType m5.2xlarge`
- Redeploy: `pulumi up`

</div>
</details>

<details>
<summary>Bedrock throttling errors</summary>
<div markdown="1">

*Diagnosis:*

Error messages about Bedrock rate limits or throttling.

*Resolution:*

- Check Bedrock quotas in AWS Service Quotas console
- Request quota increases if needed
- Implement rate limiting in your application
- Switch to a different Bedrock model with higher quotas

</div>
</details>

## Shutting down

### Clean shutdown

When you're finished with your TrustGraph deployment, clean up all resources:

```bash
pulumi destroy
```

Pulumi will show you all the resources that will be deleted and ask for confirmation. Type `yes` to proceed.

The destruction process typically takes **3-5 minutes** and removes:
- EC2 instance
- IAM roles and instance profiles
- Security groups
- Elastic IP
- EBS volumes
- SSH key pair

{: .warning }
> **Cost Warning**: AWS charges for running EC2 instances and EBS storage. Make sure to destroy your deployment when you're not using it to avoid unnecessary costs. EC2 charges accrue hourly.

### Verify cleanup

After `pulumi destroy` completes, verify all resources are removed:

```bash
# Check Pulumi stack status
pulumi stack

# Verify no resources remain
pulumi stack --show-urns

# Check AWS for remaining resources
aws ec2 describe-instances --filters "Name=tag:Name,Values=trustgraph-ec2"
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

1. Navigate to **Billing** in AWS Console
2. Use **Cost Explorer** to view EC2 and Bedrock costs
3. Set up billing alerts for unexpected charges

### Cost-Saving Tips

- **Stop instance when not in use**: `aws ec2 stop-instances --instance-ids <instance-id>`
- **Use Spot Instances**: Configure Pulumi for spot instances (60-90% cheaper)
- **Right-size instance**: Start with t3.xlarge and upgrade only if needed
- **Reserved Instances**: For long-term use, purchase reserved capacity
- **Bedrock costs**: Pay only for API calls, no base charge
- **Delete snapshots**: Clean up any EBS snapshots you don't need

Example cost estimates (us-east-1):
- **t3.2xlarge instance**: ~$0.33/hour (~$240/month if running continuously)
- **EBS storage (100GB)**: ~$10/month
- **Bedrock API calls**: ~$0.25-$1.00 per 1M input tokens (varies by model)
- **Total estimated**: ~$250-300/month for continuous operation

**Cost reduction**: Stop the instance when not in use to pay only for storage (~$10/month).

## Instance Management

### Starting a stopped instance

If you stopped your instance to save costs, restart it:

```bash
# Get instance ID from Pulumi
INSTANCE_ID=$(pulumi stack output instanceId)

# Start instance
aws ec2 start-instances --instance-ids $INSTANCE_ID

# Wait for running state
aws ec2 wait instance-running --instance-ids $INSTANCE_ID

# Get new IP (if not using Elastic IP)
aws ec2 describe-instances --instance-ids $INSTANCE_ID \
  --query 'Reservations[0].Instances[0].PublicIpAddress'
```

### Stopping the instance

Stop the instance without destroying it:

```bash
INSTANCE_ID=$(pulumi stack output instanceId)
aws ec2 stop-instances --instance-ids $INSTANCE_ID
```

You'll only pay for EBS storage while stopped (~$10/month vs ~$240/month running).

## Security Considerations

### SSH Access

The deployment creates a security group allowing SSH access from your current IP address. To update allowed IPs:

```bash
# Update security group via Pulumi
pulumi config set sshAllowedCIDR "203.0.113.0/24"
pulumi up
```

### IAM Role Permissions

The EC2 instance uses an IAM role with Bedrock permissions. The role follows least-privilege principles:

```json
{
  "Effect": "Allow",
  "Action": [
    "bedrock:InvokeModel",
    "bedrock:InvokeModelWithResponseStream"
  ],
  "Resource": "*"
}
```

### Network Security

- **No inbound traffic** except SSH (port 22)
- **Outbound traffic** allowed for container registries and AWS services
- **Service access** via SSH port forwarding (no direct exposure)

## Next Steps

Now that you have TrustGraph running on AWS EC2:

- **Guides**: See [Guides](../guides) for things you can do with your running TrustGraph
- **Experiment with models**: Try different Bedrock models (Claude Sonnet, Mistral, etc.)
- **Scale up**: Upgrade instance type for better performance
- **Production migration**: When ready, migrate to [AWS RKE deployment](aws-rke) for production use
- **Customize containers**: Modify Podman Compose configuration for your needs
- **Integration**: Connect to other AWS services (S3, DynamoDB, etc.)

{: .note }
> **Additional Resources**
>
> - [TrustGraph AWS EC2 Pulumi Repository](https://github.com/trustgraph-ai/pulumi-trustgraph-ec2) - Full source code and configuration
> - [AWS Bedrock Documentation](https://docs.aws.amazon.com/bedrock/) - Learn more about AWS foundation models
> - [Podman Documentation](https://docs.podman.io/) - Container management reference
> - [AWS EC2 Best Practices](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/ec2-best-practices.html) - AWS recommendations
