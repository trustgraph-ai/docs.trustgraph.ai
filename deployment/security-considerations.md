---
title: Security Considerations
nav_order: 10
parent: Deployment
review_date: 2026-11-01
guide_category:
guide_category_order: 3
guide_description: Security characteristics and considerations for different deployment options
guide_difficulty: intermediate
guide_time: 15 min
guide_emoji: 🔐
guide_banner: security-considerations.jpg
guide_labels:
  - Security
  - Best Practices
  - Planning
---

# Security Considerations

The initial configurations of TrustGraph have the following security
characteristics:

<table>
    <tr>
        <th>Boundary</th>
        <th>Condition</th>
        <th>Consideration</th>
    </tr>
    <tr>
        <td style="vertical-align: top;">External access</td>
        <td style="vertical-align: top;">
            <p>It is necessary to consider the external access in the TrustGraph deployment:</p>
            <ul>
               <li>Docker Compose / Podman Compose: You should take care
               when using such a deployment on a host which is directly
               addressable from the internet.  It is possible that
               services will be directly accessible from the internet.</li>
               <li>Scaleway: The Kubernetes deployment does not have any external access enabled.  Access is only possible through <code>kubectl</code> port-forwarding using your Kubernetes credentials.</li>
               <li>OVHcloud: The Kubernetes deployment does not have any external access enabled.  Access is only possible through <code>kubectl</code> port-forwarding using your Kubernetes credentials.</li>
               <li>GCP: The Kubernetes deployment does not have any external access enabled.  Access is only possible through <code>kubectl</code> port-forwarding using your Kubernetes credentials.</li>
               <li>Azure AKS: The Kubernetes deployment does not have any external access enabled.  Access is only possible through <code>kubectl</code> port-forwarding using your Kubernetes credentials.</li>
               <li>AWS EC2: The provided configuration has a security group configuration which does not permit external access.</li>
               <li>AWS RKE: The provided configuration has a security group configuration which does not permit external access.</li>
            </ul>
        </td>
        <td style="vertical-align: top;">Ensure you understand whether TrustGraph services are exposed to the network outside of your host, and always verify you understand the network security controls applied by your cloud environment.</td>
    </tr>
    <tr>
        <td style="vertical-align: top;">Service credentials</td>
        <td style="vertical-align: top;">Internal services such as Cassandra and Pulsar are deployed without service-level credentials, relying on network isolation to prevent unauthorised access.  Workspace isolation provides structural data separation through per-workspace pub/sub queues and storage partitioning.</td>
        <td style="vertical-align: top;">For complex multi-tenant environments consider understanding the extra security features which are available in services.  See <a href="../architecture/workspaces">Workspaces &amp; Data Isolation</a> for details on the data separation model.</td>
    </tr>
    <tr>
        <td style="vertical-align: top;">Gateway authentication</td>
        <td style="vertical-align: top;">The API gateway enforces authentication on all requests using Authorization headers.  Two credential types are supported: API keys (long-lived tokens with a <code>tg_</code> prefix) and username/password login which issues temporary JWT tokens.</td>
        <td style="vertical-align: top;">Pay close attention to user access control management.  Ensure that API keys are handled and distributed only through secure channels.  Prefer username/password authentication for ordinary users so that only temporary tokens are in circulation.</td>
    </tr>
    <tr>
        <td style="vertical-align: top;">IAM bootstrap token</td>
        <td style="vertical-align: top;">On first cold start, TrustGraph creates an initial security account using the <code>IAM_BOOTSTRAP_TOKEN</code> environment variable.  This token is only used for initial setup — once the system is running, additional accounts can be created and tokens changed through the workbench.</td>
        <td style="vertical-align: top;">Treat the bootstrap token as a sensitive credential.  In Pulumi-based deployments it is auto-generated and retrievable via <code>pulumi stack output</code>.  For compose deployments, choose a strong token value.  Consider rotating or replacing the bootstrap credentials once the system is operational.</td>
    </tr>
</table>

## Enterprise Support

Enhanced security support for TrustGraph is available from KnowNext at
[https://knownext.io](https://knownext.io).  See also
[Security](../architecture/security) for the broader security architecture and
enterprise IAM capabilities.
