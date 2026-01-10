<details>
<summary>Azure</summary>
<div markdown="1">
There are 2 hosted model options for Azure:

- Machine Learning Services (MLS)
- Cognitive Services (CS)

TrustGraph's *Azure* integration is for MLS. *Azure OpenAI* is for CS.

To use Azure, you need to know your model endpoint and the token granted for the endpoint.

Create the Kubernetes secret with your Azure credentials:
```bash
kubectl -n trustgraph create secret generic azure-credentials \
    --from-literal="azure-endpoint=https://ENDPOINT.API.HOST.GOES.HERE/" \
    --from-literal="azure-token=TOKEN-GOES-HERE"
```
</div>
</details>

<details>
<summary>AWS Bedrock</summary>
<div markdown="1">
To use Bedrock, you need to have AWS credentials provisioned.
The easiest way is to create an IAM user, and create credentials for this
user. When you provision the user, you will be asked to give the user
permissions. To allow Bedrock access, the `AmazonBedrockFullAccess`
role should be added.

You would then provision credentials which would give you an *access key ID*
and a *secret access key*. You should pick the identifier of an
AWS region to connect to e.g. `eu-west-2`.

Note: You should be very careful with AWS cloud credentials provisioned
this way: if lost or leaked this provides a malicious person access to the
AWS resources you gave this user.

Create the Kubernetes secret with your AWS credentials:
```bash
kubectl -n trustgraph create secret generic bedrock-credentials \
    --from-literal="aws-access-key-id=ID-KEY-HERE" \
    --from-literal="aws-secret-access-key=TOKEN-GOES-HERE" \
    --from-literal="aws-region=AWS-REGION-HERE"
```
</div>
</details>

<details>
<summary>Anthropic Claude</summary>
<div markdown="1">
To use Anthropic's Claude models directly, sign up for API access at
[console.anthropic.com](https://console.anthropic.com/). Create an API key
from the dashboard.

Create the Kubernetes secret with your Claude API key:
```bash
kubectl -n trustgraph create secret generic claude-credentials \
    --from-literal="claude-key=sk-ant-api03-xxxxx"
```
</div>
</details>

<details>
<summary>Cohere</summary>
<div markdown="1">
To use Cohere's models, sign up at [cohere.com](https://cohere.com/) and
create an API key from your dashboard.

Create the Kubernetes secret with your Cohere API key:
```bash
kubectl -n trustgraph create secret generic cohere-credentials \
    --from-literal="cohere-key=your-cohere-api-key-here"
```
</div>
</details>

<details>
<summary>Google AI Studio</summary>
<div markdown="1">
To use Google's Gemini models via AI Studio, visit
[aistudio.google.com](https://aistudio.google.com/) and generate an API key.

Create the Kubernetes secret with your Google AI Studio API key:
```bash
kubectl -n trustgraph create secret generic google-ai-studio-credentials \
    --from-literal="google-ai-studio-key=your-api-key-here"
```
</div>
</details>

<details>
<summary>Llamafile / llama.cpp server</summary>
<div markdown="1">
If running a llamafile or llama.cpp server locally, you need to configure the URL to point
to your server. The URL must include the `/v1` path.

If running on the same host as your Kubernetes cluster, use `host.minikube.internal`
as the hostname (e.g., `http://host.minikube.internal:7000/v1`).

Create the Kubernetes secret with your Llamafile URL:
```bash
kubectl -n trustgraph create secret generic llamafile-credentials \
    --from-literal="llamafile-url=http://host.minikube.internal:7000/v1"
```
</div>
</details>

<details>
<summary>LMStudio</summary>
<div markdown="1">
If running LMStudio locally, you need to configure the URL to point to your LMStudio server.
LMStudio typically runs on port 1234.

If running on the same host as your Kubernetes cluster, use `host.minikube.internal`
as the hostname (e.g., `http://host.minikube.internal:1234`).

Create the Kubernetes secret with your LMStudio URL:
```bash
kubectl -n trustgraph create secret generic lmstudio-credentials \
    --from-literal="lmstudio-url=http://host.minikube.internal:1234"
```
</div>
</details>

<details>
<summary>Mistral AI</summary>
<div markdown="1">
To use Mistral's API, sign up at [console.mistral.ai](https://console.mistral.ai/)
and create an API key.

Create the Kubernetes secret with your Mistral API key:
```bash
kubectl -n trustgraph create secret generic mistral-credentials \
    --from-literal="mistral-token=your-mistral-api-key-here"
```
</div>
</details>

<details>
<summary>Ollama</summary>
<div markdown="1">
If running Ollama locally, you need to configure the URL to point to your Ollama server.
Ollama typically runs on port 11434.

If running on the same host as your Kubernetes cluster, use `host.minikube.internal`
as the hostname (e.g., `http://host.minikube.internal:11434`).

Create the Kubernetes secret with your Ollama host URL:
```bash
kubectl -n trustgraph create secret generic ollama-credentials \
    --from-literal="ollama-host=http://host.minikube.internal:11434"
```
</div>
</details>

<details>
<summary>OpenAI</summary>
<div markdown="1">
To use OpenAI's API, sign up at [platform.openai.com](https://platform.openai.com/)
and create an API key.

Create the Kubernetes secret with your OpenAI API key:
```bash
kubectl -n trustgraph create secret generic openai-credentials \
    --from-literal="openai-token=your-openai-api-key-here"
```

If using an alternative OpenAI-compatible API, you can also specify a base URL:
```bash
kubectl -n trustgraph create secret generic openai-credentials \
    --from-literal="openai-token=your-openai-api-key-here" \
    --from-literal="openai-base-url=http://your-server-host:8000/v1"
```
</div>
</details>

<details>
<summary>Google Cloud VertexAI</summary>
<div markdown="1">
To use Google Cloud VertexAI, you need to create a service account with
appropriate permissions and download its credentials file.

1. In Google Cloud Console, create a service account
2. Grant the service account permissions to invoke VertexAI models (e.g.,
   `Vertex AI User` role - use minimal permissions, not admin roles)
3. Create and download a JSON key file for the service account
4. Save the key file as `vertexai/private.json` in your deployment directory

{: .warning }
**Important**: Service account credentials provide access to your Google Cloud
resources. Never commit `private.json` to version control. Use minimal
permissions - grant only what's needed for VertexAI model invocation, not
administrator roles.

Create the Kubernetes secret from the credentials file:
```bash
kubectl -n trustgraph create secret generic vertexai-credentials \
    --from-file=private.json=vertexai/private.json
```
</div>
</details>

<details>
<summary>vLLM</summary>
<div markdown="1">
If running vLLM locally, you need to configure the URL to point to your vLLM server.
The URL should include the `/v1` path.

If running on the same host as your Kubernetes cluster, use `host.minikube.internal`
as the hostname (e.g., `http://host.minikube.internal:8000/v1`).

Create the Kubernetes secret with your vLLM URL:
```bash
kubectl -n trustgraph create secret generic vllm-credentials \
    --from-literal="vllm-url=http://host.minikube.internal:8000/v1"
```
</div>
</details>
