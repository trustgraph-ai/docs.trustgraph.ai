---
title: Security
nav_order: 50
parent: How-to Guides
grand_parent: TrustGraph Documentation
has_children: true
review_date: 2026-03-26
---

# Security Guide

**Security foundations and enterprise roadmap for TrustGraph**

## Security Philosophy

TrustGraph is developed by a team with deep cybersecurity expertise—20+ years of enterprise security experience, including protecting Lyft's infrastructure and building cybersecurity detection businesses. **Because of that background, we tell it like it is.**

### Current Status

✅ **Strong foundations are in place**
⚠️ **Enterprise features are in active development**
🎯 **Planning for best-in-class enterprise security**

We're building TrustGraph's security infrastructure methodically, with enterprise-grade security as a core design principle from the start—not bolted on later.

## What We Have Today

### Multi-Tenant Data Separation

**Foundation**: Pulsar-based dataflow architecture provides natural data separation

- ✅ Separate dataflows per tenant/user
- ✅ Data isolation at the message queue level
- ✅ Architectural foundation for multi-tenant environments

**Why it matters**: Security isn't just about data at rest—TrustGraph separates data flows to prevent cross-contamination during processing.

### Service Authentication (Optional)

**Current**: Inter-service authentication available

- ✅ Optional credentials for service-to-service communication
- ✅ Authentication between TrustGraph components
- 🔄 Being extended to all components

### Infrastructure Security

**Kubernetes deployments** include security-by-default:

- ✅ **Secret generation with Pulumi**: Secrets generated in deployment, never committed to repos
- ✅ **Security testing in CI/CD**: Automated tests catch infrastructure security regressions
- ✅ **Deployment-time secrets**: Credentials exist only in deployment environments

**Example**: The `pulumi-trustgraph-ovhcloud` repo includes security infrastructure testing—if someone breaks security logic, tests fail.

### Government-Validated Security

✅ **Completed government AI security programme**

- Three-phase security infrastructure programme for agentic and MCP frameworks
- Focus on challenging government environments
- Details are confidential due to programme requirements
- Validates TrustGraph's security approach for high-assurance environments

## Enterprise Security Roadmap

### In Development

The following enterprise-grade features are actively being developed:

#### 🔄 Multi-Layer MCP Credential Encryption

**Problem**: MCP-enabled environments need per-user credentials protected at every layer

**Solution in development**:
- Per-user MCP credential management
- Multi-layer encryption
- Credentials exposed only at point of invocation
- Minimizes credential exposure surface

#### 🔄 Tamper-Proof Logging Architecture

**Problem**: Enterprise environments require audit trails that prove they haven't been modified

**Solution in development**:
- Tamper-proof logging system
- Immutable audit trails
- Compliance-ready logging infrastructure

#### 🔄 Enhanced Multi-Tenant Security

**Building on current Pulsar architecture**:
- Full data separation guarantees
- Protection against injection attacks in multi-tenant scenarios
- Secure tool calling in agentic flows
- Additional security layers for MCP environments

#### 🔄 Universal Service Authentication

**Extending current optional authentication**:
- Mandatory authentication for all inter-service communication
- Zero-trust service mesh integration
- Credential rotation automation

### Enterprise Vision

**When complete, TrustGraph will provide**:

- 🎯 Best-in-class multi-tenant security
- 🎯 Government/defense-grade security options
- 🎯 Full audit trail and compliance support
- 🎯 Defense-in-depth architecture
- 🎯 Zero-trust security model

## Current Security Recommendations

### For Development/Testing

**Docker Compose and local deployments**:
- ✅ Suitable for development and testing
- ⚠️ Not hardened for production
- ⚠️ No authentication required by default
- ⚠️ Assumes trusted network environment

**Best practices**:
- Run on isolated networks
- Don't expose to public internet
- Use for trusted, single-user environments
- Treat as development/POC infrastructure

### For Production (Current State)

**What you can deploy today**:
- ✅ Kubernetes with infrastructure security
- ✅ Network isolation via K8s policies
- ✅ Secret management via Pulumi
- ✅ Optional inter-service authentication

**What requires additional hardening**:
- ⚠️ API authentication (implement at reverse proxy/gateway)
- ⚠️ User access control (implement at application layer)
- ⚠️ Audit logging (implement via infrastructure monitoring)
- ⚠️ Data encryption at rest (configure at storage layer)

**Recommendation**: For production deployments requiring strict security:
1. Deploy behind authenticated reverse proxy
2. Implement network segmentation
3. Use K8s network policies
4. Enable all available service authentication
5. Contact us about enterprise security features

### For Enterprise

**If you need enterprise-grade security now**:

- 📧 **Contact us**: We're actively developing enterprise features
- 🤝 **Partner with us**: Security roadmap is informed by real requirements
- 💼 **Early access**: Enterprise customers can participate in security programme

**Tell us what you need**: Your security requirements help prioritize development.

## Security by Deployment Type

### Docker Compose

**Security level**: Development/Testing

- Network: Isolated to Docker network
- Authentication: None by default
- Encryption: None by default
- Suitable for: Local development, POCs, trusted environments

### Kubernetes (Minikube, Cloud)

**Security level**: Configurable

- Network: K8s network policies available
- Authentication: Service authentication available (optional)
- Secrets: Pulumi-managed, not in repos
- Infrastructure: Security-tested in CI/CD
- Suitable for: Testing, staging, production (with additional hardening)

### Cloud Managed (AWS, Azure, GCP)

**Security level**: Infrastructure-dependent

- Inherits cloud provider security (IAM, VPC, encryption)
- Add TrustGraph service authentication
- Implement gateway authentication
- Use cloud-native secrets management
- Suitable for: Production with proper configuration

## Security Checklist for Production

Use this checklist to evaluate your security posture:

### Network Security
- [ ] TrustGraph not exposed directly to internet
- [ ] Reverse proxy/API gateway in place
- [ ] Network segmentation configured
- [ ] TLS/SSL for all external connections
- [ ] Kubernetes network policies enabled (if using K8s)

### Authentication & Access
- [ ] API gateway authentication configured
- [ ] User access control implemented at application layer
- [ ] Service-to-service authentication enabled
- [ ] Admin access restricted and audited

### Data Protection
- [ ] Secrets managed via Pulumi/vault (not in repos)
- [ ] Sensitive data encrypted at rest (storage layer)
- [ ] Data in transit encrypted (TLS)
- [ ] Data isolation strategy for multi-user scenarios

### Monitoring & Audit
- [ ] Infrastructure monitoring in place
- [ ] Access logs collected
- [ ] Security events monitored
- [ ] Incident response plan exists

### Infrastructure
- [ ] Running latest TrustGraph version
- [ ] Security patches applied
- [ ] Infrastructure-as-code security tested
- [ ] Deployment automation secured

## What TrustGraph Does Differently

### Security-First Architecture

**Design choices driven by security requirements**:

1. **Pulsar for data flows**: Natural data separation, audit trails, replay protection
2. **Microservices architecture**: Service isolation, blast radius containment
3. **Infrastructure-as-code**: Security testing, no manual configuration drift
4. **MCP security focus**: Addressing novel threats in agentic systems

### Real Cybersecurity Experience

**The team has**:
- 20+ years enterprise security experience
- Protected major tech company infrastructure (Lyft)
- Built cybersecurity detection businesses
- Government security programme validation

**This means**:
- We know what enterprise security actually requires
- We don't oversell incomplete features
- We're building for real threat models
- We understand compliance requirements

## Getting Help with Security

### For Security Questions

📧 **Contact us directly** - Security is a priority conversation

- Security architecture questions
- Enterprise requirements discussion
- Security roadmap inquiries
- Partnership opportunities

### Reporting Security Issues

🔒 **Responsible disclosure**:
- Email: security@trustgraph.ai (if available)
- GitHub: Private security advisories
- Do not post publicly until coordinated disclosure

### Community

- **[GitHub Discussions](https://github.com/trustgraph-ai/trustgraph/discussions)** - General security questions (non-sensitive)
- **[Contributing](../../contributing/)** - Contributing security improvements

## Related Documentation

- **[Current Security Features](current-features)** - Detailed current security capabilities
- **[Enterprise Roadmap](enterprise-roadmap)** - Planned enterprise security features
- **[Production Deployment](../../deployment/production-considerations)** - Security for production
- **[Infrastructure Security](infrastructure-security)** - K8s and cloud security patterns

## The Bottom Line

**Today**: Strong security foundations suitable for development, testing, and internal deployments with additional hardening.

**Tomorrow**: Best-in-class enterprise security for government, defense, and multi-tenant SaaS environments.

**Our commitment**: We're building this right, telling you honestly where we are, and prioritizing security throughout.

**Your role**: Tell us what you need. Enterprise security requirements drive our roadmap.
