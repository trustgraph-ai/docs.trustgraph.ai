<details>
<summary>Specific guidance for Azure</summary>
<div markdown="1">
There are 2 hosted model options for Azure:

- Machine Learning Services (MLS)
- Cognitive Services (CS)

TrustGraph's *Azure* is for integration with MLS. *Azure OpenAI* is for
integration with CS. If you are using the *Azure* / MLS integration, you
should make sure you know your model endpoint, and the token granted for the
endpoint, and configure these values thus:
```
export AZURE_ENDPOINT=https://ENDPOINT.API.HOST.GOES.HERE/
export AZURE_TOKEN=TOKEN-GOES-HERE
```
If you are using the *Azure OpenAI* / CS integration, you should make sure
you know your model endpoint, the token and configure them thus:
```
export AZURE_ENDPOINT=https://ENDPOINT.API.HOST.GOES.HERE/
export AZURE_TOKEN=TOKEN-GOES-HERE
```
</div>
</details>

<details>
<summary>Specific guidance for AWS Bedrock</summary>
<div markdown="1">
To use Bedrock, you need to have AWS credentials provisioned.
The easiest way is to create an IAM user, and create credentials for this
user. When you provision the user, you will be asked to give the user
permissions. To allow Bedrock access, the `AmazonBedrockFullAccess`
role should be added.

You would then provision credentials which would give you an *access key ID*
and a *secret access key*. You should pick the identifier of an
AWS region to connect to e.g. `eu-west-2`. In order to prepare to deploy,
you should set three environment variables using the information.

```
export AWS_ACCESS_KEY_ID=ID-KEY-HERE
export AWS_SECRET_ACCESS_KEY=TOKEN-GOES-HERE
export AWS_DEFAULT_REGION=AWS-REGION-HERE
```

Note: You should be very careful with AWS cloud credentials provisioned
this way: if lost or leaked this provides a malicious person access to the
AWS resources you gave this user.
</div>
</details>

<details>
<summary>Specific guidance for Anthropic Claude</summary>
<div markdown="1">
To use Anthropic's Claude models directly, sign up for API access at
[console.anthropic.com](https://console.anthropic.com/). Create an API key
from the dashboard. Set the key as an environment variable:

```
export CLAUDE_KEY=sk-ant-api03-xxxxx
```
</div>
</details>

<details>
<summary>Specific guidance for Cohere</summary>
<div markdown="1">
To use Cohere's models, sign up at [cohere.com](https://cohere.com/) and
create an API key from your dashboard. Set the key as an environment variable:

```
export COHERE_KEY=your-cohere-api-key-here
```
</div>
</details>

<details>
<summary>Specific guidance for Google AI Studio</summary>
<div markdown="1">
To use Google's Gemini models via AI Studio, visit
[aistudio.google.com](https://aistudio.google.com/) and generate an API key.
Set the key as an environment variable:

```
export GOOGLE_AI_STUDIO_KEY=your-api-key-here
```
</div>
</details>

<details>
<summary>Specific guidance for Llamafile / llama.cpp server</summary>
<div markdown="1">
If running a llamafile or llama.cpp server locally, configure the URL to point
to your server. The URL must include the `/v1` path:

```
export LLAMAFILE_URL=http://your-server-host:port/v1
```

If running on the same host as your containers, use `host.containers.internal`
as the hostname (e.g., `http://host.containers.internal:7000/v1`).

See also: [Container networking and self-hosted models](container-networking)
</div>
</details>

<details>
<summary>Specific guidance for LMStudio</summary>
<div markdown="1">
If running LMStudio locally, configure the URL to point to your LMStudio server.
LMStudio typically runs on port 1234:

```
export LMSTUDIO_URL=http://your-server-host:1234
```

If running on the same host as your containers, use `host.containers.internal`
as the hostname (e.g., `http://host.containers.internal:1234`).

See also: [Container networking and self-hosted models](container-networking)
</div>
</details>

<details>
<summary>Specific guidance for Mistral AI</summary>
<div markdown="1">
To use Mistral's API, sign up at [console.mistral.ai](https://console.mistral.ai/)
and create an API key. Set the key as an environment variable:

```
export MISTRAL_TOKEN=your-mistral-api-key-here
```
</div>
</details>

<details>
<summary>Specific guidance for Ollama</summary>
<div markdown="1">
If running Ollama locally, configure the URL to point to your Ollama server.
Ollama typically runs on port 11434:

```
export OLLAMA_HOST=http://your-server-host:11434
```

If running on the same host as your containers, use `host.containers.internal`
as the hostname (e.g., `http://host.containers.internal:11434`).

See also: [Container networking and self-hosted models](container-networking)
</div>
</details>

<details>
<summary>Specific guidance for OpenAI</summary>
<div markdown="1">
To use OpenAI's API, sign up at [platform.openai.com](https://platform.openai.com/)
and create an API key. Set the key as an environment variable:

```
export OPENAI_TOKEN=your-openai-api-key-here
```

Many other services provide OpenAI-compatible APIs. You can use these by setting
the `OPENAI_BASE_URL` environment variable to point to the alternative service:

```
export OPENAI_BASE_URL=http://your-server-host:8000/v1
```
</div>
</details>

<details>
<summary>Specific guidance for Google Cloud VertexAI</summary>
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

After placing the file, you may need to adjust file permissions as described
earlier in the configuration unpacking section:

```sh
chmod 644 vertexai/private.json
```

On SELinux systems, also run:

```sh
sudo chcon -Rt svirt_sandbox_file_t vertexai/
```
</div>
</details>

<details>
<summary>Specific guidance for vLLM</summary>
<div markdown="1">
If running vLLM locally, configure the URL to point to your vLLM server.
The URL should include the `/v1` path:

```
export VLLM_URL=http://your-server-host:port/v1
```

If running on the same host as your containers, use `host.containers.internal`
as the hostname (e.g., `http://host.containers.internal:8000/v1`).

See also: [Container networking and self-hosted models](container-networking)
</div>
</details>
