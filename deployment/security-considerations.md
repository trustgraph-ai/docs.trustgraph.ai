---
title: Security Considerations
nav_order: 10
parent: Deployment
review_date: 2026-02-19
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
               when using such a deployment to a box which is directly
               addressable from the internet.  It is possible that
               services will be directly accessible from the internet
               without authentication.</li>
               <li>Scaleway: The Kubernetes deployment does not have any external access enabled.  Access is only possible through `kubectl` port-forwarding using your Kubernetes credentials.</li>
               <li>OVHcloud: The Kubernetes deployment does not have any external access enabled.  Access is only possible through `kubectl` port-forwarding using your Kubernetes credentials.</li>
               <li>AWS EC2: The provided configuration has a security group configuration which does not permit external access.</li>
               <li>AWS RKE: The provided configuration has a security group configuration which does not permit external access.</li>
            </ul>
        </td>
        <td style="vertical-align: top;">Ensure you understand whether TrustGraph services are exposed to the network outside of your host, and always verify you understand the network security controls applied by your cloud environment.</td>
    </tr>
    <tr>
        <td style="vertical-align: top;">Service credentials</td>
        <td style="vertical-align: top;">Services such as Cassandra and Pulsar are deployed without security credentials, relying on network isolation to prevent unauthorised access</td>
        <td style="vertical-align: top;">For complex multi-tenant environments consider understanding the extra security features which are available in services</td>
    </tr>
    <tr>
        <td style="vertical-align: top;">Gateway authentication</td>
        <td style="vertical-align: top;">Out-of-the-box, there is no authentication on the API gateway</td>
        <td style="vertical-align: top;">Consider setting `GATEWAY_TOKEN`, and using a token in API calls.  Alternatively protect the gateway with a custom authentication gateway for external access.</td>
    </tr>
</table>

## Enterprise Support

Enhanced security support for TrustGraph is available from KnowNext at
[https://knownext.io](https://knownext.io).
