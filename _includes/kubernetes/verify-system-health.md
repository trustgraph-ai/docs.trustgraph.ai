Use the TrustGraph verification tool to check system health. First, set up port-forwarding to access the API gateway (see next section), then run:

```bash
# After setting up port-forwarding (see below)
tg-verify-system-status \
  --api-url http://localhost:8088 \
  --pulsar-url http://localhost:8080 \
  --ui-url http://localhost:8888
```

A healthy system will show:

```
============================================================
TrustGraph System Status Verification
============================================================

Phase 1: Infrastructure
------------------------------------------------------------
[00:00] ✓ Pulsar: Pulsar healthy
[00:00] ✓ API Gateway: API Gateway is responding

Phase 2: Core Services
------------------------------------------------------------
[00:00] ✓ Processors: Found 34 processors
[00:00] ✓ Flow Classes: Found 9 flow class(es)
[00:00] ✓ Flows: Flow manager responding (1 flow(s))
[00:00] ✓ Prompts: Found 16 prompt(s)

Phase 3: Data Services
------------------------------------------------------------
[00:00] ✓ Library: Library responding (0 document(s))

Phase 4: User Interface
------------------------------------------------------------
[00:00] ✓ Workbench UI: Workbench UI is responding

============================================================
Summary
============================================================
Checks passed: 8/8
Checks failed: 0/8

✓ System is healthy!
```
