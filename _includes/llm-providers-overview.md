You need to have access to an LLM. TrustGraph can work with many different
kinds of LLM. You can use a cloud-hosted service, or have an LLM hosted
locally on your device or network. TrustGraph can work with small models
which you can run on standard home/office equipment,
but small models are still demanding on resources. A 16GB laptop is able to
run an LLM but likely not at the same time as running all the containers which
make up a TrustGraph deployment.

Here are some example ways to get an LLM to run:

| Provider | Description | Access type |
|----------|-------------|----------|
| **Google Cloud VertexAI** | This is a subscription-based service which is part of Google Cloud. The Gemini models are good and cost-effective. There are free credits for new users. | Cloud subscription |
| **AWS Bedrock** | Amazon's managed LLM service with Claude, Mistral, and other models available. Running Claude on Bedrock is a good option. | Cloud subscription |
| **Azure** | Microsoft's cloud subscription services include Machine Learning Services (MLS) and Cognitive Services (CS). The TrustGraph *Azure* integration can use the MLS service, while *Azure OpenAI* can use CS models. | Cloud subscription |
| **Anthropic Claude** | Integrates with Anthropic's APIs directly for access to the Claude models. Claude models are very capable. | API subscription |
| **Mistral AI** | Integrates with Mistral's APIs directly for access to the Mistral models. | API subscription |
| **OpenAI** | Integrates with OpenAI's API for GPT models | API subscription |
| **Ollama** | Run models locally on your machine. Supports Llama, Mistral, and many others. | Self-hosted |
| **vLLM** | The most comprehensive self-hosted model engine | Self-hosted |
| **LMStudio** | Desktop application for running local LLMs with an OpenAI-compatible API. LMStudio is a very user-friendly experience, which makes it easier to diagnose and solve hosting problems. Note: LMStudio is free, but only for non-work-related use. | Self-hosted |

Using a cloud-hosted service is a good starting point - you will need a
subscription, but no extra hardware. If you do want to run an LLM locally,
you will need a device with a good GPU, and likely some experience of
running this yourself as you may need to debug model / hosting issues.
