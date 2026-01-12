Back in the workbench, select the *Assistant* tab.

In the top line next to the *Assistant* word, change the mode to *Basic LLM*.

Enter a question in the prompt box at the bottom of the tab and press *Send*. If everything works, after a short period you should see a response to your query.

![Simple LLM usage](llm-interaction.png)

If LLM interactions are not working, check the Grafana logs dashboard for errors in the `text-completion` service.
