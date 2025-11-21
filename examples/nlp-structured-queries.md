---
title: NLP and Structured Query Examples
parent: Examples
nav_order: 5
permalink: /examples/nlp-structured-queries
---

# NLP and Structured Query Examples

This page provides practical examples of using TrustGraph's NLP Query and Structured Query services for various data analysis tasks.

## Basic Query Generation and Execution

### Example 1: Product Catalog Analysis

```bash
# Generate GraphQL from natural language
tg-invoke-nlp-query -q "Show all products with price over $100" --format graphql

# Output: query { products(where: {price: {_gt: 100}}) { id name price category } }

# Execute the query to get actual data
tg-invoke-structured-query -q "query { products(where: {price: {_gt: 100}}) { id name price category } }"
```

**Expected Output:**
```
+----+----------------+--------+-------------+
| id | name           | price  | category    |
+----+----------------+--------+-------------+
| 1  | Gaming Laptop  | 1299.99| Electronics |
| 2  | Professional Monitor | 599.99 | Electronics |
| 3  | Wireless Headphones | 149.99 | Audio |
+----+----------------+--------+-------------+
```

### Example 2: Customer Analysis

```python
from trustgraph.api import Api

api = Api("http://localhost:8088/").flow().id("default")

# Natural language to GraphQL
nlp_response = api.nlp_query(
    question="Find customers who placed orders in the last 30 days"
)

print("Generated Query:", nlp_response["graphql_query"])
print("Confidence:", nlp_response["confidence"])

# Execute the query
results = api.structured_query(
    question=nlp_response["graphql_query"]
)

print(f"Found {len(results['data']['customers'])} active customers")
```

## Extract-Query-Analyze Workflows

### Example 3: Financial Document Analysis

```python
# Step 1: Extract structured financial data
financial_text = """
Q4 2024 Earnings Report - TechCorp Inc.

Financial Highlights:
- Revenue: $245.7 million (up 34% YoY)
- Gross Profit: $156.2 million (64% margin)
- Net Income: $89.4 million
- Cash: $523.1 million

Business Segments:
- Cloud Services: $156M revenue (up 45%)
- Enterprise Software: $67M revenue (up 18%)
- Consulting: $22.7M revenue (up 12%)

Key Metrics:
- Customer Count: 12,847 (up 28%)
- Annual Recurring Revenue: $892M
- Churn Rate: 3.2% (improved from 4.1%)
"""

# Extract structured data
extraction = api.invoke_agent(
    prompt="""Extract structured financial data including:
    1. Company financial metrics
    2. Business segment performance
    3. Key performance indicators
    Store as Company and FinancialReport objects.""",
    text=financial_text
)

# Step 2: Query the extracted data
revenue_analysis = api.structured_query(
    question="What business segments have the highest growth rates?"
)

# Step 3: Generate insights
insights = api.invoke_agent(
    prompt=f"""Analyze this financial performance data:
    {revenue_analysis['data']}
    
    Provide insights on:
    1. Growth drivers
    2. Market positioning
    3. Investment opportunities
    4. Risk factors""",
    extraction_mode="analysis"
)

print("Business Insights:", insights["analysis"])
```

### Example 4: Competitive Intelligence Pipeline

```python
# Process multiple competitor documents
competitors = [
    {"name": "Company A", "document": "company_a_earnings.pdf"},
    {"name": "Company B", "document": "company_b_10k.pdf"},
    {"name": "Company C", "document": "company_c_investor_deck.pdf"}
]

competitive_data = []

for competitor in competitors:
    # Extract competitive intelligence
    extraction = api.invoke_agent(
        prompt=f"""Extract competitive intelligence for {competitor['name']}:
        1. Revenue and financial metrics
        2. Product portfolio
        3. Market share data
        4. Strategic initiatives
        5. Competitive advantages""",
        text=load_document(competitor["document"])
    )
    competitive_data.append(extraction)

# Comparative analysis
comparison = api.structured_query(
    question="Compare revenue growth and market share across all companies"
)

# Strategic recommendations
strategy = api.invoke_agent(
    prompt=f"""Based on this competitive analysis: {comparison['data']}
    
    Recommend:
    1. Market positioning strategy
    2. Product development priorities
    3. Competitive responses
    4. Market entry opportunities""",
    extraction_mode="strategic"
)
```

## Command Line Workflows

### Example 5: Interactive Data Exploration

```bash
#!/bin/bash
# explore_data.sh - Interactive data exploration script

echo "=== TrustGraph Data Explorer ==="

while true; do
    echo ""
    read -p "Ask a question about your data: " QUESTION
    
    if [ "$QUESTION" = "exit" ]; then
        break
    fi
    
    echo "Generating query..."
    GRAPHQL=$(tg-invoke-nlp-query -q "$QUESTION" --format graphql)
    
    if [ $? -eq 0 ]; then
        echo "Generated GraphQL: $GRAPHQL"
        echo ""
        echo "Executing query..."
        tg-invoke-structured-query -q "$GRAPHQL" --format table
    else
        echo "Could not generate query. Trying direct agent analysis..."
        tg-invoke-agent -p "$QUESTION"
    fi
done
```

### Example 6: Automated Report Generation

```bash
#!/bin/bash
# generate_reports.sh - Generate structured reports from data

# Extract today's metrics
echo "=== Daily Business Report ===" > daily_report.txt
date >> daily_report.txt
echo "" >> daily_report.txt

# Revenue analysis
echo "## Revenue Analysis" >> daily_report.txt
tg-invoke-structured-query -q "Show today's revenue by product category" --format csv > revenue.csv
cat revenue.csv >> daily_report.txt
echo "" >> daily_report.txt

# Customer metrics
echo "## Customer Metrics" >> daily_report.txt
tg-invoke-structured-query -q "Count new customers today" --format json | \
  jq -r '.customers_aggregate.aggregate.count' | \
  xargs -I {} echo "New customers: {}" >> daily_report.txt

# Top products
echo "## Top Products" >> daily_report.txt
tg-invoke-structured-query -q "Top 5 products by sales today" --format table >> daily_report.txt

echo "Report generated: daily_report.txt"
```

## Advanced Integration Examples

### Example 7: Real-Time Query Enhancement

```python
class SmartQueryEngine:
    def __init__(self):
        self.api = Api("http://localhost:8088/").flow().id("default")
        self.query_cache = {}
    
    def smart_query(self, user_question):
        """
        Smart query that tries multiple approaches
        """
        # Try direct structured query first
        try:
            result = self.api.structured_query(question=user_question)
            if result["data"]:
                return result["data"]
        except:
            pass
        
        # Generate GraphQL query
        try:
            nlp_result = self.api.nlp_query(question=user_question)
            if nlp_result["confidence"] > 0.7:
                structured_result = self.api.structured_query(
                    question=nlp_result["graphql_query"]
                )
                return structured_result["data"]
        except:
            pass
        
        # Fallback to agent analysis
        agent_result = self.api.invoke_agent(
            prompt=user_question,
            extraction_mode="comprehensive"
        )
        return agent_result["analysis"]
    
    def explain_query(self, user_question):
        """
        Explain how a query would be processed
        """
        nlp_result = self.api.nlp_query(question=user_question)
        
        explanation = {
            "original_question": user_question,
            "generated_graphql": nlp_result["graphql_query"],
            "detected_schemas": nlp_result["detected_schemas"],
            "confidence": nlp_result["confidence"],
            "query_complexity": self._analyze_complexity(nlp_result["graphql_query"])
        }
        
        return explanation

# Usage
engine = SmartQueryEngine()

# Smart query processing
result = engine.smart_query("What were our best selling products last quarter?")
explanation = engine.explain_query("What were our best selling products last quarter?")

print("Query Explanation:", explanation)
print("Results:", result)
```

### Example 8: Multi-Document Knowledge Building

```python
def build_knowledge_from_documents(document_paths):
    """
    Build queryable knowledge base from multiple documents
    """
    api = Api("http://localhost:8088/").flow().id("default")
    
    # Phase 1: Extract all structured data
    all_extractions = []
    for doc_path in document_paths:
        with open(doc_path, 'r') as f:
            content = f.read()
        
        extraction = api.invoke_agent(
            prompt="""Extract all structured entities:
            - Companies and organizations
            - People and roles
            - Products and services  
            - Financial data and metrics
            - Dates and events
            Create clear relationships between entities.""",
            text=content,
            metadata={"source": doc_path}
        )
        all_extractions.append(extraction)
    
    # Phase 2: Query for insights across all data
    cross_doc_queries = [
        "Which companies appear in multiple documents?",
        "What are the common themes across documents?",
        "Which people are mentioned most frequently?",
        "What products are discussed across documents?"
    ]
    
    insights = {}
    for query in cross_doc_queries:
        try:
            result = api.structured_query(question=query)
            insights[query] = result["data"]
        except:
            # Fallback to NLP query
            nlp_result = api.nlp_query(question=query)
            if nlp_result["confidence"] > 0.5:
                result = api.structured_query(question=nlp_result["graphql_query"])
                insights[query] = result["data"]
    
    # Phase 3: Generate summary analysis
    summary = api.invoke_agent(
        prompt=f"""Analyze this cross-document intelligence:
        {insights}
        
        Provide:
        1. Key entities and their importance
        2. Relationship patterns
        3. Emerging themes
        4. Notable connections
        5. Data quality assessment""",
        extraction_mode="synthesis"
    )
    
    return {
        "extractions": all_extractions,
        "cross_document_insights": insights,
        "summary_analysis": summary
    }

# Process a set of business documents
documents = [
    "annual_report_2024.pdf",
    "competitor_analysis.pdf", 
    "market_research.pdf",
    "customer_feedback.txt"
]

knowledge_base = build_knowledge_from_documents(documents)
print("Knowledge Base Summary:", knowledge_base["summary_analysis"])
```

## Error Handling and Troubleshooting

### Example 9: Robust Query Processing

```python
def robust_query_with_fallback(question, max_retries=3):
    """
    Robust query processing with multiple fallback strategies
    """
    api = Api("http://localhost:8088/").flow().id("default")
    
    for attempt in range(max_retries):
        try:
            # Strategy 1: Direct structured query
            result = api.structured_query(question=question)
            if result["data"]:
                return {"method": "direct", "data": result["data"]}
                
        except Exception as e:
            print(f"Direct query failed (attempt {attempt + 1}): {e}")
        
        try:
            # Strategy 2: NLP query generation + execution
            nlp_result = api.nlp_query(question=question)
            if nlp_result["confidence"] > 0.6:
                structured_result = api.structured_query(
                    question=nlp_result["graphql_query"]
                )
                return {
                    "method": "nlp_generated", 
                    "data": structured_result["data"],
                    "generated_query": nlp_result["graphql_query"],
                    "confidence": nlp_result["confidence"]
                }
                
        except Exception as e:
            print(f"NLP query failed (attempt {attempt + 1}): {e}")
        
        try:
            # Strategy 3: Agent-based analysis
            agent_result = api.invoke_agent(
                prompt=f"Analyze and answer: {question}",
                extraction_mode="comprehensive"
            )
            return {"method": "agent_analysis", "data": agent_result}
            
        except Exception as e:
            print(f"Agent analysis failed (attempt {attempt + 1}): {e}")
    
    return {"method": "failed", "data": None, "error": "All strategies failed"}

# Usage with error handling
question = "What are our top revenue drivers?"
result = robust_query_with_fallback(question)

if result["method"] != "failed":
    print(f"Successfully answered using: {result['method']}")
    print("Data:", result["data"])
else:
    print("Could not process query:", result["error"])
```

## Performance Optimization Examples

### Example 10: Caching and Batch Processing

```python
import time
from functools import lru_cache
from concurrent.futures import ThreadPoolExecutor

class OptimizedQueryProcessor:
    def __init__(self):
        self.api = Api("http://localhost:8088/").flow().id("default")
    
    @lru_cache(maxsize=256)
    def cached_nlp_query(self, question):
        """Cache NLP query results"""
        return self.api.nlp_query(question=question)
    
    def batch_structured_queries(self, questions):
        """Process multiple queries concurrently"""
        def process_query(question):
            try:
                return self.api.structured_query(question=question)
            except:
                return None
        
        with ThreadPoolExecutor(max_workers=5) as executor:
            results = list(executor.map(process_query, questions))
        
        return [r for r in results if r is not None]
    
    def optimize_query_pattern(self, questions):
        """Optimize common query patterns"""
        # Group similar queries
        grouped = self._group_similar_queries(questions)
        
        optimized_results = {}
        for group_type, group_questions in grouped.items():
            if group_type == "aggregation":
                # Use single aggregation query
                combined_query = self._combine_aggregation_queries(group_questions)
                result = self.api.structured_query(question=combined_query)
                optimized_results[group_type] = result
            else:
                # Process individually
                results = self.batch_structured_queries(group_questions)
                optimized_results[group_type] = results
        
        return optimized_results

# Performance testing
processor = OptimizedQueryProcessor()

# Test queries
test_questions = [
    "Count total orders",
    "Sum total revenue", 
    "Average order value",
    "Show top customers",
    "List recent products"
]

# Benchmark different approaches
start_time = time.time()
sequential_results = [processor.api.structured_query(question=q) for q in test_questions]
sequential_time = time.time() - start_time

start_time = time.time()
batch_results = processor.batch_structured_queries(test_questions)
batch_time = time.time() - start_time

print(f"Sequential processing: {sequential_time:.2f}s")
print(f"Batch processing: {batch_time:.2f}s")
print(f"Performance improvement: {sequential_time/batch_time:.1f}x")
```

These examples demonstrate the power and flexibility of TrustGraph's NLP and Structured Query capabilities. Start with the basic examples and gradually work up to the more advanced integration patterns based on your specific use case.

## See Also

- [NLP Query API](../reference/apis/api-nlp-query)
- [Structured Query API](../reference/apis/api-structured-query)
- [Agent Extraction Guide](../guides/agent-extraction)
- [Object Extraction Guide](../guides/object-extraction)
- [tg-invoke-nlp-query CLI](../reference/cli/tg-invoke-nlp-query)
- [tg-invoke-structured-query CLI](../reference/cli/tg-invoke-structured-query)