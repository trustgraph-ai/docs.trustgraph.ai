Access Grafana monitoring at [http://localhost:3000](http://localhost:3000) (requires port-forwarding to be running).

**Default credentials:**
- Username: `admin`
- Password: `admin`

All TrustGraph components collect metrics using Prometheus and make these available using this Grafana workbench. The Grafana deployment is configured with 2 dashboards:
- **Overview metrics dashboard**: Shows processing metrics
- **Logs dashboard**: Shows collated TrustGraph container logs

For a newly launched system, the metrics won't be particularly interesting yet.
