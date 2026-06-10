# sqlfluff-dq-rules

> Data Development Quality Rules plugin for SQLFluff

## Rules

| Rule | Code | Description |
|------|------|-------------|
| No SELECT * | DQ01 | Detects wildcard in SELECT clauses |
| WHERE required | DQ02 | Flags DELETE/UPDATE without WHERE |
| Explicit JOIN | DQ03 | Detects implicit comma joins |

## Quick Start

\\ash
pip install sqlfluff
pip install sqlfluff-dq-rules
sqlfluff lint --rules DQ01,DQ02,DQ03 query.sql
\
## Architecture

SQLFluff parses SQL into AST. Rules extend BaseRule and use SegmentSeekerCrawler to find target nodes.
