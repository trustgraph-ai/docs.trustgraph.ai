---
title: Current Security Features
nav_order: 1
parent: Security
grand_parent: How-to Guides
review_date: 2025-11-21
---

# Current Security Features

**What's available in TrustGraph today**

This page honestly describes the security features currently implemented in TrustGraph. We don't oversell—if a feature is in development, we say so clearly.

## Multi-Tenant Data Separation

### Pulsar-Based Architecture

**Status**: ✅ **Production-ready foundation**

TrustGraph's use of Apache Pulsar for dataflows provides natural data separation:

**How it works**:
```
User A data → Topic A → Processing A → Storage partition A
User B data → Topic B → Processing B → Storage partition B
```

**Security benefits**:
- Data streams are separated at the message queue level
- Different users'/tenants' data never mix in processing pipelines
- Each dataflow can have independent access controls
- Foundation for true multi-tenant security

**Current capabilities**:
- ✅ Separate Pulsar topics per collection
- ✅ Independent processing flows
- ✅ Isolated message routing
- ✅ Natural audit trail (message history)

**Configuration**:
```yaml
pulsar:
  tenant: production
  namespace: user-{user-id}
  topics:
    - persistent://production/user-{user-id}/documents
```

**Why it matters**: Most platforms add multi-tenancy as an afterthought. TrustGraph's architecture makes it fundamental—data separation happens at the dataflow level, not just storage.

### Collection-Based Isolation

**Status**: ✅ **Available now**

Collections provide logical data separation:

```bash
# User A's collection
tg-set-collection user-a-docs
tg-load-pdf --collection user-a-docs document.pdf

# User B's collection
tg-set-collection user-b-docs
tg-load-pdf --collection user-b-docs document.pdf
```

**Security properties**:
- Collections map to separate Pulsar topics
- Queries scoped to specific collections
- No cross-collection data leakage in queries
- Foundation for tenant isolation

## Service Authentication

### Inter-Service Communication

**Status**: ✅ **Available (optional), 🔄 Being extended to all services**

Some TrustGraph services support authenticated communication:

**Current support**:
- ✅ Optional credentials for service-to-service auth
- ✅ Token-based authentication between components
- 🔄 Being extended to all components (in progress)

**Configuration example**:
```yaml
services:
  graph-rag:
    auth:
      enabled: true
      token: ${SERVICE_TOKEN}

  embeddings:
    auth:
      enabled: true
      token: ${SERVICE_TOKEN}
```

**How to enable**:
1. Generate service tokens during deployment
2. Configure services with `auth.enabled: true`
3. Provide tokens via environment variables
4. Services validate tokens on each request

**Limitations**:
- ⚠️ Not all services support authentication yet
- ⚠️ Manual token management required
- ⚠️ No automatic token rotation currently

**Roadmap**: Universal service authentication with automatic rotation (see [Enterprise Roadmap](enterprise-roadmap)).

## Infrastructure Security

### Kubernetes Deployment Security

**Status**: ✅ **Production-ready**

TrustGraph's Kubernetes deployments include security best practices:

#### Secret Management with Pulumi

**How it works**:
- Secrets generated during deployment (not in git repos)
- Pulumi manages secret lifecycle
- Secrets injected into K8s as needed
- Never committed to version control

**Example** (from deployment code):
```python
# Secrets generated at deployment time
db_password = random.RandomPassword("db-password",
    length=32,
    special=True
)

# Injected into K8s secret
k8s_secret = k8s.core.v1.Secret("trustgraph-secrets",
    metadata={"name": "trustgraph-secrets"},
    string_data={
        "db-password": db_password.result
    }
)
```

**Security benefits**:
- ✅ Secrets never in source code
- ✅ Secrets never in git repos
- ✅ Each deployment has unique secrets
- ✅ Secrets managed by IaC tooling

#### CI/CD Security Testing

**Status**: ✅ **Active in deployment repos**

Deployment repositories include automated security tests:

**Example repos with security testing**:
- `pulumi-trustgraph-ovhcloud`
- Other Pulumi deployment repos

**What's tested**:
- Infrastructure security configuration
- Secret management correctness
- Network policy configuration
- Service exposure rules

**How it works**:
```yaml
# In CI pipeline
- name: Test security configuration
  run: |
    # Verify secrets not in plain text
    # Verify network policies exist
    # Verify TLS configuration
    # etc.
```

**Impact**: If someone breaks security logic in infrastructure code, CI fails the build.

### Network Security

**Status**: ✅ **Configurable via K8s**

TrustGraph supports standard Kubernetes network security:

**Network Policies**:
```yaml
apiVersion: networking.k8s.io/v1
kind: NetworkPolicy
metadata:
  name: trustgraph-isolation
spec:
  podSelector:
    matchLabels:
      app: trustgraph
  policyTypes:
  - Ingress
  ingress:
  - from:
    - podSelector:
        matchLabels:
          app: trustgraph
```

**Available configurations**:
- ✅ Pod-to-pod communication restrictions
- ✅ Ingress/egress rules
- ✅ Service-level isolation
- ✅ External access control

**Best practices**:
- Use network policies to restrict pod communication
- Limit external access to API gateway only
- Isolate database/storage access
- Segment production/staging environments

## Data Security

### Data at Rest

**Status**: ⚠️ **Depends on storage layer configuration**

TrustGraph stores data in external systems:

| Component | Storage | Encryption |
|-----------|---------|------------|
| Graph data | Cassandra | Configure at Cassandra level |
| Vectors | Qdrant | Configure at Qdrant level |
| Messages | Pulsar | Configure at Pulsar level |
| Documents | Object storage | Configure at storage level |

**Current state**:
- TrustGraph doesn't manage storage encryption directly
- Encryption configured at storage layer
- Use cloud provider encryption (AWS KMS, Azure Key Vault, etc.)
- Or configure encryption in Cassandra/Qdrant/Pulsar

**Recommendations**:
```yaml
# Cassandra with encryption
cassandra:
  encryption:
    enabled: true
    keystore: /path/to/keystore

# Qdrant with TLS
qdrant:
  tls:
    enabled: true
    cert: /path/to/cert
```

### Data in Transit

**Status**: ✅ **TLS configurable**

TrustGraph supports TLS for network communication:

**External connections**:
- ✅ TLS for API gateway connections
- ✅ TLS for client-to-service communication
- ⚠️ Configure at reverse proxy/gateway level

**Internal connections**:
- ✅ TLS for service-to-storage (configure on storage)
- ⚠️ Service-to-service TLS (configure per service)
- 🔄 Default TLS for all internal comms (roadmap)

**Configuration**:
```yaml
# API Gateway with TLS
gateway:
  tls:
    enabled: true
    cert: ${TLS_CERT}
    key: ${TLS_KEY}
```

## Access Control

### Current State

**Status**: ⚠️ **Application layer responsibility**

TrustGraph currently does not provide built-in user authentication or authorization:

**What TrustGraph provides**:
- ✅ Collection-based data isolation
- ✅ Service authentication (optional)
- ✅ Foundation for access control

**What you need to implement**:
- ⚠️ User authentication (at API gateway)
- ⚠️ Authorization/RBAC (at application layer)
- ⚠️ User-to-collection mapping
- ⚠️ API access control

**Typical architecture**:
```
User → Auth Gateway → TrustGraph API
         ↓
      Identity Provider
      (OAuth, SAML, etc.)
```

**Recommendations**:
1. Deploy reverse proxy with authentication
2. Map authenticated users to collections
3. Enforce access controls at gateway
4. Use collection isolation for data separation

**Example with nginx**:
```nginx
location /api/ {
    auth_request /auth;
    proxy_pass http://trustgraph:8000/;

    # Pass user ID to TrustGraph
    proxy_set_header X-User-ID $auth_user_id;
}
```

## Monitoring & Audit

### Available Now

**Status**: ✅ **Foundation in place**

**Grafana dashboards**:
- ✅ System metrics
- ✅ Processing statistics
- ✅ Performance monitoring
- ⚠️ Security events (basic)

**Pulsar audit trail**:
- ✅ Message history preserved
- ✅ Can replay dataflows for audit
- ✅ Topic-level activity tracking
- ⚠️ Not formatted as audit logs

**What's missing**:
- ⚠️ Comprehensive security event logging
- ⚠️ User activity audit trails
- ⚠️ Access logs
- ⚠️ Tamper-proof logging (in development)

**Current recommendations**:
- Use infrastructure monitoring (K8s audit logs)
- Collect application logs
- Monitor Pulsar topics for activity
- Export to SIEM if required

## Government Security Programme

### Validation

**Status**: ✅ **Completed**

TrustGraph completed a three-phase government AI security programme:

**What was validated**:
- Security architecture for agentic systems
- MCP framework security
- Suitability for government/defense environments

**What we can't disclose**:
- Specific programme details (confidential)
- Exact security features evaluated
- Government partner information

**What it means**:
- ✅ TrustGraph security reviewed by government experts
- ✅ Architecture validated for high-assurance environments
- ✅ Security approach proven in demanding scenarios
- ✅ Foundation for government/defense deployments

## Security Configuration Examples

### Minimal Security (Development)

```yaml
# Docker Compose - development only
services:
  trustgraph:
    network_mode: bridge
    # No authentication
    # No encryption
    # Suitable for local development only
```

### Basic Security (Staging)

```yaml
# Kubernetes with basic hardening
security:
  networkPolicies: true
  serviceAuth:
    enabled: true
  secrets:
    management: pulumi
  tls:
    external: true
    internal: false
```

### Enhanced Security (Production)

```yaml
# Production with available security features
security:
  networkPolicies: true
  serviceAuth:
    enabled: true
    allServices: true
  secrets:
    management: pulumi
    rotation: manual
  tls:
    external: true
    internal: true
    storage: true
  monitoring:
    enabled: true
    alerts: true
```

## What's Next

See [Enterprise Roadmap](enterprise-roadmap) for upcoming security features including:

- Multi-layer MCP credential encryption
- Tamper-proof logging
- Universal service authentication
- Enhanced multi-tenant security
- Zero-trust architecture

## Questions About Current Features?

- **[Security Index](index)** - Security overview and philosophy
- **[Enterprise Roadmap](enterprise-roadmap)** - Planned features
- **[Production Guide](../../deployment/production-considerations)** - Production security setup
- **[Contact Us](../../contributing/getting-help)** - Security questions

---

**Remember**: We tell it like it is. If a feature isn't ready, we say so. If you need something that's not here yet, let us know—your requirements drive the roadmap.
