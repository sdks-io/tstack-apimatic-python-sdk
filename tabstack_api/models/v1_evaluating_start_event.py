from __future__ import annotations

from pydantic import Field
from typing_extensions import TypedDict

from ..core import SdkBaseModel


class V1EvaluatingStartEvent(SdkBaseModel):
    iteration: float
    message: str
    pages_analyzed: float = Field(alias="pagesAnalyzed")
    """Total pages analyzed so far (including this iteration)"""

    question_count: float = Field(alias="questionCount")
    """Number of research questions being assessed"""

    timestamp: float


class V1EvaluatingStartEventDict(TypedDict):
    iteration: float
    message: str
    pages_analyzed: float
    question_count: float
    timestamp: float
