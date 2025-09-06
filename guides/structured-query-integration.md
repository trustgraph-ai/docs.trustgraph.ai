---
layout: default
title: Structured Query Integration
parent: Guides
nav_order: 9
permalink: /guides/structured-query-integration
---

# Structured Query Integration with Agent Functionality

This guide explains how structured query capabilities integrate with TrustGraph's agent-based extraction and processing workflows. The integration enables seamless transitions between unstructured data extraction and structured data analysis.

## Overview

The integration between structured queries and agent functionality provides:
- **Extraction-to-Query Workflows**: Extract structured data, then immediately query it
- **Query-Driven Extraction**: Use query results to guide further extraction
- **Hybrid Analysis**: Combine unstructured text analysis with structured data queries
- **Dynamic Schema Discovery**: Agents help discover queryable schemas
- **Context-Aware Processing**: Use query results to inform agent decisions

## Core Integration Patterns

### 1. Extract-Query-Analyze Pipeline

The most common pattern: extract data, query it, analyze results.

```python
from trustgraph.api import Api

api = Api("http://localhost:8088/").flow().id("default")

# Step 1: Agent extracts structured data from document
document_text = """
Q4 2024 Financial Report for TechCorp
Revenue: $125.5M (up 23% YoY)
Operating Expenses: $89.2M
Net Income: $36.3M
Employee Count: 1,847 (up 12% from Q3)
Key Products:
- CloudSync Pro: $85M revenue
- DataViz Analytics: $28M revenue  
- Security Suite: $12.5M revenue
"""

extraction_response = api.invoke_agent(
    prompt="""Extract structured financial and product data.
    Create objects for: Company, FinancialReport, Product.
    Include all numerical values and relationships.""",
    text=document_text,
    extraction_mode="comprehensive"
)

print(f"Extracted {len(extraction_response['objects'])} objects")

# Step 2: Query the extracted structured data
query_response = api.structured_query(
    question="What products generated more than $50M in revenue?"
)

high_revenue_products = query_response["data"]["products"]

# Step 3: Agent analyzes query results
analysis_response = api.invoke_agent(
    prompt=f"""Analyze these high-revenue products and identify:
    1. Market position and competitive advantages
    2. Growth opportunities
    3. Risk factors
    Products: {high_revenue_products}""",
    extraction_mode="analysis"
)

print("Analysis Results:", analysis_response["analysis"])
```

### 2. Query-Guided Extraction

Use query results to inform what to extract next:

```python
# Step 1: Initial broad query to understand available data
overview = api.structured_query(
    question="Show all companies with financial data from the last 6 months"
)

companies = overview["data"]["companies"]

# Step 2: Agent identifies gaps and extracts missing information
for company in companies:
    if not company.get("employee_count"):
        # Extract missing employee data
        hr_response = api.invoke_agent(
            prompt=f"""Find and extract employee count and workforce data 
            for {company['name']}. Look for headcount, hiring, layoffs.""",
            context={"company": company},
            extraction_mode="focused"
        )
        
    if not company.get("product_line"):
        # Extract product information
        product_response = api.invoke_agent(
            prompt=f"""Extract product line and service offerings 
            for {company['name']}. Include revenue attribution.""",
            context={"company": company},
            extraction_mode="focused"
        )
```

### 3. Dynamic Schema Discovery

Agents help discover what can be queried:

```python
# Agent analyzes documents to identify queryable entities
schema_discovery = api.invoke_agent(
    prompt="""Analyze this corpus of documents and identify:
    1. What types of structured entities are present
    2. What fields/properties each entity type has
    3. What relationships exist between entity types
    4. Suggest GraphQL schema structure""",
    text=large_document_corpus,
    extraction_mode="schema_discovery"
)

# Use discovered schemas for structured queries
discovered_schemas = schema_discovery["schemas"]
for schema in discovered_schemas:
    results = api.structured_query(
        question=f"Show all {schema['entity_type']} entities"
    )
    print(f"Found {len(results['data'][schema['entity_type']])} {schema['entity_type']} entities")
```

## Advanced Integration Workflows

### Multi-Stage Analysis Pipeline

```python
def analyze_business_documents(documents):
    """
    Multi-stage pipeline combining extraction, querying, and analysis
    """
    all_insights = []
    
    # Stage 1: Extract all structured data
    for doc in documents:
        extraction = api.invoke_agent(
            prompt="Extract all business entities: companies, products, financials, people",
            text=doc["content"],
            metadata={"source": doc["filename"]}
        )
    
    # Stage 2: Query for patterns and trends
    trend_queries = [
        "What companies showed revenue growth over 20%?",
        "Which products had declining sales?",
        "What are the top 5 companies by employee count?",
        "Show companies that acquired others in the last year"
    ]
    
    trend_data = {}
    for query in trend_queries:
        result = api.structured_query(question=query)
        trend_data[query] = result["data"]
    
    # Stage 3: Agent synthesizes insights from query results
    synthesis = api.invoke_agent(
        prompt=f"""Analyze these business trends and provide insights:
        {trend_data}
        
        Identify:
        1. Market leaders and challengers
        2. Industry consolidation patterns
        3. Growth vs stability strategies
        4. Competitive positioning""",
        extraction_mode="synthesis"
    )
    
    return synthesis["insights"]
```

### Real-Time Query-Extraction Loop

```python
def interactive_data_exploration():
    """
    Interactive loop where queries inform next extraction steps
    """
    user_question = input("What would you like to know? ")
    
    # Try to answer with existing data
    try:
        response = api.structured_query(question=user_question)
        if response["data"]:
            print("Found existing data:", response["data"])
            
            # Check if more context would help
            context_check = api.invoke_agent(
                prompt=f"""Given this user question: "{user_question}"
                And this existing data: {response["data"]}
                
                Would additional document analysis help provide a more complete answer?
                If yes, what specific information should we extract?""",
                extraction_mode="assessment"
            )
            
            if context_check["recommend_extraction"]:
                # Extract additional context
                additional_data = api.invoke_agent(
                    prompt=context_check["extraction_guidance"],
                    text=get_relevant_documents(user_question),
                    extraction_mode="targeted"
                )
                
                # Re-query with new data
                enhanced_response = api.structured_query(question=user_question)
                print("Enhanced answer:", enhanced_response["data"])
                
        else:
            print("No existing data found. Extracting from documents...")
            
            # Extract relevant data first
            extraction = api.invoke_agent(
                prompt=f"Extract data needed to answer: {user_question}",
                text=get_relevant_documents(user_question),
                extraction_mode="targeted"
            )
            
            # Then query the newly extracted data
            response = api.structured_query(question=user_question)
            print("Answer from newly extracted data:", response["data"])
            
    except Exception as e:
        print(f"Query failed: {e}")
        # Fallback to pure agent analysis
        response = api.invoke_agent(
            prompt=user_question,
            text=get_relevant_documents(user_question),
            extraction_mode="comprehensive"
        )
        print("Agent analysis:", response["analysis"])
```

### Validation and Enrichment Pipeline

```python
def validate_and_enrich_data():
    """
    Use agents to validate query results and enrich with additional context
    """
    # Query for potentially incomplete data
    incomplete_records = api.structured_query(
        question="Show all companies missing industry classification"
    )
    
    for company in incomplete_records["data"]["companies"]:
        # Agent enriches missing data
        enrichment = api.invoke_agent(
            prompt=f"""Research and determine the industry classification 
            for {company['name']}. Consider their products, services, 
            and market positioning. Provide:
            1. Primary industry (NAICS code if possible)
            2. Secondary industries
            3. Business model classification
            4. Market segment""",
            context={"company": company},
            extraction_mode="enrichment"
        )
        
        # Update the structured data
        api.update_object(
            object_type="Company",
            object_id=company["id"],
            updates={
                "industry": enrichment["primary_industry"],
                "industry_code": enrichment.get("naics_code"),
                "business_model": enrichment["business_model"],
                "market_segment": enrichment["market_segment"]
            }
        )
        
    # Validate data consistency
    validation_check = api.structured_query(
        question="Find companies with revenue > $1B but employee count < 100"
    )
    
    if validation_check["data"]["companies"]:
        # Agent investigates anomalies
        investigation = api.invoke_agent(
            prompt=f"""Investigate these companies with unusual metrics:
            {validation_check['data']['companies']}
            
            Determine if this represents:
            1. Data quality issues
            2. Legitimate business models (high automation, licensing, etc.)
            3. Measurement differences (contractors vs employees)
            
            Recommend corrections if needed.""",
            extraction_mode="validation"
        )
        
        print("Data quality findings:", investigation["findings"])
```

## Integration Patterns by Use Case

### Financial Analysis

```python
# Extract financial data from reports
financial_extraction = api.invoke_agent(
    prompt="Extract quarterly financial metrics, ratios, and KPIs",
    text=financial_reports,
    extraction_mode="financial"
)

# Query for comparative analysis
comparison = api.structured_query(
    question="Compare revenue growth rates across all companies by quarter"
)

# Agent provides investment analysis
investment_analysis = api.invoke_agent(
    prompt=f"""Based on this financial data: {comparison['data']}
    
    Provide investment analysis including:
    1. Growth trend analysis
    2. Financial health assessment  
    3. Risk factors
    4. Investment recommendations""",
    extraction_mode="analysis"
)
```

### Competitive Intelligence

```python
# Extract competitor information
competitor_data = api.invoke_agent(
    prompt="Extract competitor profiles, market share, products, strategies",
    text=market_research_docs,
    extraction_mode="competitive"
)

# Query for market positioning
market_position = api.structured_query(
    question="Show market share and product overlap between competitors"
)

# Strategic analysis
strategy_analysis = api.invoke_agent(
    prompt=f"""Analyze competitive landscape: {market_position['data']}
    
    Identify:
    1. Market leaders and followers
    2. Competitive gaps and opportunities
    3. Strategic recommendations
    4. Threat assessment""",
    extraction_mode="strategic"
)
```

### Regulatory Compliance

```python
# Extract regulatory requirements
compliance_data = api.invoke_agent(
    prompt="Extract compliance requirements, deadlines, penalties, obligations",
    text=regulatory_documents,
    extraction_mode="compliance"
)

# Query for compliance gaps
gaps_analysis = api.structured_query(
    question="Show companies with missing compliance data or upcoming deadlines"
)

# Risk assessment
risk_assessment = api.invoke_agent(
    prompt=f"""Assess compliance risks: {gaps_analysis['data']}
    
    Provide:
    1. High-risk areas requiring immediate attention
    2. Compliance gap analysis
    3. Remediation recommendations
    4. Timeline for compliance""",
    extraction_mode="risk_analysis"
)
```

## Best Practices

### 1. Design for Queryability

When extracting data, structure it for optimal querying:

```python
# Good: Structure data with queryable relationships
extraction_prompt = """
Extract structured data ensuring:
1. Consistent entity naming and IDs
2. Clear relationships between entities
3. Standardized date/time formats
4. Numerical values in consistent units
5. Categorical data using controlled vocabularies
"""
```

### 2. Progressive Enhancement

Start with basic queries, enhance with agent analysis:

```python
# Basic structured query first
basic_results = api.structured_query(question="Show all products")

# Enhance with agent insights if needed
if len(basic_results["data"]["products"]) > 50:
    # Too many results - let agent summarize
    summary = api.invoke_agent(
        prompt=f"Summarize key insights from these {len(basic_results)} products",
        context={"products": basic_results["data"]["products"]},
        extraction_mode="summarization"
    )
```

### 3. Context Preservation

Maintain context between extraction and query phases:

```python
# Preserve extraction context for queries
extraction_context = {
    "extraction_id": extraction_response["extraction_id"],
    "source_documents": document_metadata,
    "extraction_timestamp": extraction_response["timestamp"]
}

# Use context in queries
query_with_context = api.structured_query(
    question="Show recently extracted financial data",
    context=extraction_context
)
```

### 4. Error Handling and Fallbacks

```python
def robust_query_extraction(question, documents):
    try:
        # Try structured query first
        result = api.structured_query(question=question)
        if result["data"]:
            return result["data"]
    except StructuredQueryError:
        pass
    
    try:
        # Fallback to agent extraction + query
        extraction = api.invoke_agent(
            prompt=f"Extract data needed to answer: {question}",
            text=documents,
            extraction_mode="targeted"
        )
        return api.structured_query(question=question)["data"]
    except ExtractionError:
        pass
    
    # Final fallback to pure agent analysis
    return api.invoke_agent(
        prompt=question,
        text=documents,
        extraction_mode="comprehensive"
    )["analysis"]
```

## Performance Optimization

### 1. Query Optimization

```python
# Use specific queries rather than broad extractions
specific_query = api.structured_query(
    question="Show companies in tech sector with revenue > $1B"
)

# Better than extracting all data then filtering
```

### 2. Incremental Processing

```python
# Process incrementally for large datasets
def process_large_corpus(documents):
    batch_size = 10
    
    for i in range(0, len(documents), batch_size):
        batch = documents[i:i+batch_size]
        
        # Extract from batch
        extraction = api.invoke_agent(
            prompt="Extract structured business data",
            text=batch,
            extraction_mode="comprehensive"
        )
        
        # Query immediately for validation
        validation = api.structured_query(
            question="Show data extracted in the last hour"
        )
        
        # Process results before next batch
        process_batch_results(validation["data"])
```

### 3. Caching and Reuse

```python
from functools import lru_cache

@lru_cache(maxsize=128)
def cached_structured_query(question):
    return api.structured_query(question=question)

# Reuse common query patterns
common_queries = [
    "Show all companies",
    "List product categories", 
    "Display recent financial reports"
]

# Pre-populate cache
for query in common_queries:
    cached_structured_query(query)
```

## See Also

- [Agent Extraction Process](agent-extraction) - Agent-based data extraction
- [Object Extraction Process](object-extraction) - Object-focused extraction  
- [Structured Query API](../reference/apis/api-structured-query) - Query API reference
- [NLP Query API](../reference/apis/api-nlp-query) - Natural language queries
- [Agent API](../reference/apis/api-agent) - Agent API reference