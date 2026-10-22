from __future__ import annotations

from typing_extensions import TypedDict

from ..core import SdkBaseModel
from .enums.status import StatusOrStr


class V1ResearchQuestionAssessment(SdkBaseModel):
    """Assessment of a single research question"""

    findings: str
    """What we learned (if answered/partial) or what's missing (if unanswered)"""

    question: str
    """The research question being assessed"""

    status: StatusOrStr
    """Status: answered (clear info), partial (some info, gaps remain), unanswered (no relevant info)"""


class V1ResearchQuestionAssessmentDict(TypedDict):
    findings: str
    question: str
    status: StatusOrStr
