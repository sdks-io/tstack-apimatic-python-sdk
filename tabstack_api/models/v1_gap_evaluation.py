from __future__ import annotations

from pydantic import Field
from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .enums.research_coverage import ResearchCoverageOrStr
from .v1_research_question_assessment import V1ResearchQuestionAssessment, V1ResearchQuestionAssessmentDict


class V1GapEvaluation(SdkBaseModel):
    """Gap evaluation results from research strategist"""

    gap_description: str = Field(alias="gapDescription")
    """Based on unanswered/partial questions, what specific information is still needed?"""

    new_research_questions: Optional[list[str]] = Field(default=UNSET, alias="newResearchQuestions")
    """New research questions to add (optional, use sparingly)
    - Only if original decomposition missed something critical
    - Maximum 2-3 new questions total across all iterations
    - Most iterations should return empty array or omit this field"""

    question_assessments: list[V1ResearchQuestionAssessment] = Field(alias="questionAssessments")
    """Assessment of each research question's status and findings"""

    research_coverage: ResearchCoverageOrStr = Field(alias="researchCoverage")
    """Research coverage level - assesses quality across all questions.

    Hierarchy: Light < Moderate < Solid < Comprehensive

    - **Light**: Basic info on some questions, most need more depth → Continue
    - **Moderate**: Multiple questions answered, some remain partial → Continue
    - **Solid**: Most questions well-answered with validated sources → Sufficient to stop
    - **Comprehensive**: All questions thoroughly answered, exceptional depth → Definitely stop"""

    search_queries: Optional[list[str]] = Field(default=UNSET, alias="searchQueries")
    """Search queries to address identified gaps (only when shouldContinueResearch is true)
    - Target unanswered questions first, then partial questions
    - 3-10 targeted queries if shouldContinueResearch is true
    - Omit or provide empty array if shouldContinueResearch is false"""

    should_continue_research: bool = Field(alias="shouldContinueResearch")
    """Explicit decision: should research continue with another iteration?
    - Considers: how many questions unanswered/partial, coverage for mode, remaining iterations
    - Drives query generation: true → generate queries, false → stop researching"""


class V1GapEvaluationDict(TypedDict):
    gap_description: str
    new_research_questions: NotRequired[list[str]]
    question_assessments: list[V1ResearchQuestionAssessmentDict]
    research_coverage: ResearchCoverageOrStr
    search_queries: NotRequired[list[str]]
    should_continue_research: bool
