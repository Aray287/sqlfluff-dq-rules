# sqlfluff-dq-rules

> Data Development Quality Rules plugin for SQLFluff

Custom rules plugin for [SQLFluff](https://github.com/sqlfluff/sqlfluff) that adds SQL quality checks for data development scenarios. Can be used as a SQL quality gate in CI pipelines.

## Rules

| Code | Name | Detects | Pain Point |
|------|------|---------|------------|
| DQRules_DQ01 | \dq.no_select_star\ | \*\ wildcard in SELECT clauses | Poor query performance, fragile schema |
| DQRules_DQ02 | \dq.require_where_for_modify\ | DELETE/UPDATE without WHERE | Accidental data loss/corruption |
| DQRules_DQ03 | \dq.explicit_join\ | Comma-separated tables in FROM | Poor readability, accidental cross joins |

## Quick Start

### Install

\\ash
pip install sqlfluff
pip install sqlfluff-dq-rules
\
### Usage

\\ash
sqlfluff lint --rules DQRules_DQ01,DQRules_DQ02,DQRules_DQ03 --dialect ansi query.sql
\
Or create a \.sqlfluff\ config file in your project root:

\\ini
[sqlfluff]
dialect = ansi
rules = DQRules_DQ01, DQRules_DQ02, DQRules_DQ03
\
### Verify

\\sql
-- test.sql
SELECT * FROM orders;
DELETE FROM orders;
\
\\ash
sqlfluff lint test.sql
# L:1 | DQRules_DQ01 | SELECT statements should not use '*' wildcard.
# L:2 | DQRules_DQ02 | DELETE and UPDATE statements must have a WHERE clause.
\
## Architecture

\SQLFluff CLI -> Plugin Manager (pluggy) -> sqlfluff-dq-rules -> SQL AST Parser
\
SQLFluff discovers plugins via \importlib.metadata.entry_points\. Rules extend \BaseRule\ and use \SegmentSeekerCrawler\ to find AST nodes, then \_eval()\ checks for violations.

## Requirements

- Python >= 3.9
- SQLFluff >= 4.0.0
- Any OS (Windows / Linux / macOS)

## Development

\\ash
pip install -e .
\