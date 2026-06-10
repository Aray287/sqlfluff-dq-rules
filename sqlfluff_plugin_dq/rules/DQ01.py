"""DQ01: No SELECT * in production queries."""
from typing import Optional

from sqlfluff.core.rules import BaseRule, LintResult, RuleContext
from sqlfluff.core.rules.crawlers import SegmentSeekerCrawler


class Rule_DQRules_DQ01(BaseRule):
    """SELECT statements should not use ``*`` wildcard."""

    name = "dq.no_select_star"
    aliases = ("L0D1",)
    groups: tuple[str, ...] = ("all", "dq")
    crawl_behaviour = SegmentSeekerCrawler({"select_clause_element"})
    is_fix_compatible = False

    def _eval(self, context: RuleContext) -> Optional[LintResult]:
        for child in context.segment.segments:
            if child.is_type("wildcard_expression"):
                return LintResult(anchor=context.segment)
        return None
