from __future__ import annotations

from pydantic import Field
from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .cited_page import CitedPage, CitedPageDict
from .enums.query_complexity import QueryComplexityOrStr
from .enums.v1_mode import V1ModeOrStr
from .url_sources import UrlSources, UrlSourcesDict
from .v1_gap_evaluation import V1GapEvaluation, V1GapEvaluationDict
from .v1_judgment_result import V1JudgmentResult, V1JudgmentResultDict
from .v1_research_metrics import V1ResearchMetrics, V1ResearchMetricsDict
from .v1_research_outline import V1ResearchOutline, V1ResearchOutlineDict


class V1ResearchMetadata(SdkBaseModel):
    """Research metadata

    Note: citedPages, gapEvaluations, outline, and judgments are optional to support fast mode, which skips these phases
    for maximum speed."""

    cited_pages: Optional[list[CitedPage]] = Field(default=UNSET, alias="citedPages")
    """Pages cited in the report, ordered by first citation appearance"""

    executed_queries: list[list[str]] = Field(alias="executedQueries")
    gap_evaluations: Optional[list[V1GapEvaluation]] = Field(default=UNSET, alias="gapEvaluations")
    judgments: Optional[list[V1JudgmentResult]] = UNSET
    metrics: Optional[V1ResearchMetrics] = UNSET
    """Complete research metrics"""

    mode: V1ModeOrStr
    """Research mode determines depth, thinking budget, and quality controls

    Modes (in order of cost/thoroughness):
    - **fast**: Quick answers with minimal validation (~$2, 1 iteration, no judge)
    - **balanced**: Standard research with moderate depth (~$8, 3 iterations, Flash models, no judge)
    - **deep**: Thorough research with judge review (~$15, 5 iterations, Flash models, with judge)
    - **max**: Maximum quality with Pro models (~$40, 5 iterations, Pro models, with judge)
    - **ultra**: Ultimate tier - all Pro models, 10 iterations (expensive, for when accuracy is paramount)"""

    outline: Optional[V1ResearchOutline] = UNSET
    """Report outline from research writer"""

    prompt: str
    query_complexity: QueryComplexityOrStr = Field(alias="queryComplexity")
    research_objective: str = Field(alias="researchObjective")
    research_plan: str = Field(alias="researchPlan")
    research_questions: list[str] = Field(alias="researchQuestions")
    total_pages_analyzed: float = Field(alias="totalPagesAnalyzed")
    """Total pages analyzed across all iterations"""

    url_sources: Optional[UrlSources] = Field(default=UNSET, alias="urlSources")


class V1ResearchMetadataDict(TypedDict):
    cited_pages: NotRequired[list[CitedPageDict]]
    executed_queries: list[list[str]]
    gap_evaluations: NotRequired[list[V1GapEvaluationDict]]
    judgments: NotRequired[list[V1JudgmentResultDict]]
    metrics: NotRequired[V1ResearchMetricsDict]
    mode: V1ModeOrStr
    outline: NotRequired[V1ResearchOutlineDict]
    prompt: str
    query_complexity: QueryComplexityOrStr
    research_objective: str
    research_plan: str
    research_questions: list[str]
    total_pages_analyzed: float
    url_sources: NotRequired[UrlSourcesDict]
