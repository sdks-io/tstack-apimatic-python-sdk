from __future__ import annotations

from typing_extensions import TypedDict

from ..core import SdkBaseModel
from .enums.complexity import ComplexityOrStr


class V1PlanningEndEvent(SdkBaseModel):
    complexity: ComplexityOrStr
    message: str
    objective: str
    plan: str
    queries: list[str]
    questions: list[str]
    timestamp: float


class V1PlanningEndEventDict(TypedDict):
    complexity: ComplexityOrStr
    message: str
    objective: str
    plan: str
    queries: list[str]
    questions: list[str]
    timestamp: float
