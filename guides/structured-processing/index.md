---
title: Structured data processing
parent: How-to Guides
review_date: 2026-02-01
guide_category: Advanced knowledge management
guide_category_order: 1
guide_description: Extract and process structured data from documents and files using schema-based extraction
guide_difficulty: intermediate
guide_time: 45 min
guide_emoji: 📊
guide_banner: structured-processing.jpg
guide_labels:
  - Extraction
  - Schema
  - Objects
---

# Structured Data Processing

Learn how to process documents and extract structured data using TrustGraph's
schema-based extraction capabilities.

This feature was introduced in TrustGraph 1.2 and extended to support
querying in 1.3.

## Overview

TrustGraph provides capabilities for working with 'objects'.  This
is data which could be described in e.g. table rows.

The following capabilities are available in TrustGraph 1.3 for you to
work through with this guide.

- Loading object data from documents.  In this guide tablular data from an
  example PDF document is extracted to an object store.
- Loading object data from structured data files.  Data files in
  XML, JSON and CSV format can be loaded into the object store.  This guide
  will work with an example data file.
- Querying is possible in a number of forms - this guide will look at
  querying using GraphQL and also executing a natural language query.
- Structured data queries can also be invoke from an agent, so that tabular
  data is integrated with an agent flow.

## See also

- [Schemas](schemas)
- [Load from a document](load-doc)
- [Load from a data file](load-file)
- [Querying structured data](query)
- [Agent integration](agent-integration)

