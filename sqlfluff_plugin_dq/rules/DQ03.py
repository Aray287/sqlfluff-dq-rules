"""DQ03: Use explicit JOIN syntax instead of implicit joins.

Implicit joins (comma-separated tables in FROM clause) can lead to
accidental cross joins if the WHERE condition is missing. Explicit
JOIN syntax is clearer, easier to maintain, and prevents errors.
"""
from typing import Optional

from sqlfluff.core.rules import BaseRule, LintResult, RuleContext
from sqlfluff.core.rules.crawlers import SegmentSeekerCrawler


class Rule_DQRules_DQ03(BaseRule):
    """Use explicit ``JOIN`` syntax instead of comma-separated tables.

    Comma-separated tables in FROM clauses are harder to read and
    can accidentally produce cross joins. Always use explicit JOIN.

    **Anti-pattern**

    .. code-block:: sql

        SELECT * FROM orders o, customers c WHERE o.cid = c.id;

    **Best practice**

    .. code-block:: sql

        SELECT * FROM orders o JOIN customers c ON o.cid = c.id;
    """

    name = "dq.explicit_join"
    aliases = ("L0D3",)
    groups: tuple[str, ...] = ("all", "dq")
    crawl_behaviour = SegmentSeekerCrawler({"from_clause"})
    is_fix_compatible = False

    def _eval(self, context: RuleContext) -> Optional[LintResult]:
        """Check for comma-separated table references (implicit joins)."""
        has_comma = any(
            child.is_type("comma")
            for child in context.segment.segments
        )
        if has_comma:
            return LintResult(anchor=context.segment)
        return None
