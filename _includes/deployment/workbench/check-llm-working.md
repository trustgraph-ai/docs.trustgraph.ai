If the `tg-invoke-llm` command worked earlier, you can skip this section. Otherwise, this is a quick way to verify LLM access through the workbench while introducing the prompt management workflow.

From the Workflows page, select **Prompt Management**. This screen is where all the prompt templates live. You can edit existing templates and construct your own.

To run a simple test, find the **question** prompt in the list on the left and select it. The template is straightforward — just `{% raw %}{{question}}{% endraw %}` — which means the `question` variable is fed directly to the LLM.

On the right-hand side, change the **TEST** box from `{}` to:

```json
{"question": "What is 2 + 2?"}
```

Click **Run**. You should see the answer to your question appear below.

![Prompt test with question template](prompt-test.png)

If you want to experiment with prompts, try adding "Please provide a detailed explanation" to the prompt template, click **Save**, and run the test again to see a different response.

If LLM interactions are not working, check the Grafana logs dashboard for errors in the `text-completion` service.
