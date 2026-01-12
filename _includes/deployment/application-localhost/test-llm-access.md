Test that Scaleway Gen AI integration is working by invoking the LLM through the gateway:

```bash
tg-invoke-llm 'Be helpful' 'What is 2 + 2?'
```

You should see output like:

```
2 + 2 = 4
```

This confirms that TrustGraph can successfully communicate with Scaleway's Generative AI service.
