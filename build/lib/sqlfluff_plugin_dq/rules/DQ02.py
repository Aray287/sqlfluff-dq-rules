"""DQ02: DELETE/UPDATE must have WHERE clause.

Data safety rule: DELETE and UPDATE statements without a WHERE
clause are dangerous in production as they modify all rows.
This is a critical data engineering best practice.

Note: This rule only applies to DELETE FROM and UPDATE statements,
not TRUNCATE (which is intentionally destructive).
"""
from typing import Optional

from sqlfluff.core.rules import BaseRule, LintResult, RuleContext
from sqlfluff.core.rules.crawlers import SegmentSeekerCrawler


class Rule_DQ02(BaseRule):
    """DELETE and UPDATE statements must have a ``WHERE`` clause.

    Unconditional DELETE/UPDATE can cause data loss or corruption
    in production databases. Always specify a WHERE clause to
    limit the affected rows.

    **Anti-pattern**

    .. code-block:: sql

        DELETE FROM orders;
        UPDATE orders SET status = 'archived';

    **Best practice**

    .. code-block:: sql

        DELETE FROM orders WHERE status = 'cancelled';
        UPDATE orders SET status = 'archived' WHERE created_at < '2024-01-01';
    """

    name = "dq.require_where_for_modify"
    aliases = ("L0D2",)
    groups: tuple[str, ...] = ("all", "dq")
    crawl_behaviour = SegmentSeekerCrawler({"delete_statement", "update_statement"})
    is_fix_compatible = False

    def _eval(self, context: RuleContext) -> Optional[LintResult]:
        """Check that DELETE/UPDATE has a WHERE clause."""
        has_where = any(
            child.is_type("where_clause")
            for child in context.segment.segments
        )
        if not has_where:
            return LintResult(anchor=context.segment)
        return None
