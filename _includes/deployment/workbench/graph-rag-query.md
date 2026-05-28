From the Workflows page, select **Graph RAG Query**. This console is more than your average chatbot — it has full Explainable AI enabled. This helps to understand and diagnose retrieval, but is not intended as an end-user experience.

Enter a query such as "What was the cause of the Bronze Age Collapse?" and after a short while you should see a response.

![Graph RAG query result](graph-rag-query.png)

There is a lot to see here if you are interested. The bottom right part of the screen shows the various explainability events, starting from the question:

- **Grounding** — where retrieval selects key concepts for discovery
- **Exploration** — where graph nodes are selected for analytics
- **Focus** — where the system decides on a core set of graph edges to resolve the question
- **Synthesis** — where this is processed to provide an answer

On the left-hand side you see the actual answer to the query. The **Focus** event may be of particular interest as you can trace graph edges all the way back to the source documents. For example, the graph edge *(Systems Collapse Model → proposed by → Joseph Tainter)* has a link to source below which, when followed, shows the original source text.

![Source tracing from graph edge](graph-rag-source.png)
