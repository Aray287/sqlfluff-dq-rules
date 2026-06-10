# sqlfluff-dq-rules

> Data Development SQL Quality Rules Plugin for SQLFluff

Custom rules plugin that adds SQL quality checks for data development. Can be used as a SQL quality gate in CI pipelines.

---

## Rules

| Code | Name | What It Detects | Why It Matters |
|------|------|-----------------|----------------|
| `DQRules_DQ01` | No SELECT * | `SELECT *` and `SELECT t.*` in queries | Prevents fragile schema dependencies, reduces unnecessary I/O |
| `DQRules_DQ02` | WHERE required | `DELETE` / `UPDATE` without a `WHERE` clause | Prevents accidental full-table data loss |
| `DQRules_DQ03` | Explicit JOIN only | Comma-separated tables in `FROM` clause | Improves readability, prevents accidental cross joins |

---

## Quick Start

```bash
# Install SQLFluff and this plugin
pip install sqlfluff
pip install sqlfluff-dq-rules

# Lint a SQL file with DQ rules enabled
sqlfluff lint --rules DQRules_DQ01,DQRules_DQ02,DQRules_DQ03 --dialect ansi your_query.sql
```

Or create a `.sqlfluff` config in your project root:

```ini
[sqlfluff]
dialect = ansi
rules = DQRules_DQ01, DQRules_DQ02, DQRules_DQ03
```

Then simply run:

```bash
sqlfluff lint your_query.sql
```

### Example

```sql
-- bad.sql
SELECT * FROM orders;
DELETE FROM orders;
SELECT o.*, c.name FROM orders o, customers c WHERE o.id = c.id;
```

```bash
$ sqlfluff lint bad.sql
L:1 | DQRules_DQ01 | SELECT statements should not use wildcard.
L:2 | DQRules_DQ02 | DELETE and UPDATE statements must have a WHERE clause.
L:3 | DQRules_DQ01 | SELECT statements should not use wildcard.
L:3 | DQRules_DQ03 | Use explicit JOIN instead of comma-separated tables.
```

---

## Architecture

```
SQLFluff CLI -> Plugin Manager (pluggy) -> sqlfluff-dq-rules -> SQL AST Engine
```

SQLFluff discovers plugins via `importlib.metadata.entry_points`. Each rule extends `BaseRule`, uses `SegmentSeekerCrawler` to locate AST nodes, and `_eval()` checks for pattern violations.

### Plugin Loading

pyproject.toml defines the entry point:

```toml
[project.entry-points.sqlfluff]
dq_rules = "sqlfluff_plugin_dq"
```

---

## Requirements

- Python >= 3.9
- SQLFluff >= 4.0.0
- Any OS (no GPU required)

## Development

```bash
git clone https://github.com/<YOUR_USERNAME>/sqlfluff-dq-rules.git
cd sqlfluff-dq-rules
pip install -e .
```
