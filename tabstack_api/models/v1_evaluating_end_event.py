from __future__ import annotations

from pydantic import Field
from typing_extensions import TypedDict

from ..core import SdkBaseModel
from .enums.coverage import CoverageOrStr
from .v1_research_question_assessment import V1ResearchQuestionAssessment, V1ResearchQuestionAssessmentDict


class V1EvaluatingEndEvent(SdkBaseModel):
    coverage: CoverageOrStr
    gaps: str
    iteration: float
    message: str
    next_queries: list[str] = Field(alias="nextQueries")
    question_assessments: list[V1ResearchQuestionAssessment] = Field(alias="questionAssessments")
    should_continue: bool = Field(alias="shouldContinue")
    timestamp: float


class V1EvaluatingEndEventDict(TypedDict):
    coverage: CoverageOrStr
    gaps: str
    iteration: float
    message: str
    next_queries: list[str]
    question_assessments: list[V1ResearchQuestionAssessmentDict]
    should_continue: bool
    timestamp: float
