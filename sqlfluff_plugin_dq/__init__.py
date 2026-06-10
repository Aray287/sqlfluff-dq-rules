"""SQLFluff plugin: Data Quality Rules for data development.

This plugin adds SQL best practice rules focused on data quality and
data development standards, including:
- DQ01: No SELECT * in production queries
- DQ02: DELETE/UPDATE must have WHERE clause
- DQ03: Use explicit JOIN instead of implicit joins
"""
from sqlfluff.core.plugin import hookimpl
from sqlfluff.core.rules import BaseRule


@hookimpl
def get_rules() -> list[type[BaseRule]]:
    """Register custom data quality rules."""
    from sqlfluff_plugin_dq.rules.DQ01 import Rule_DQ01
    from sqlfluff_plugin_dq.rules.DQ02 import Rule_DQ02
    from sqlfluff_plugin_dq.rules.DQ03 import Rule_DQ03
    return [Rule_DQ01, Rule_DQ02, Rule_DQ03]
