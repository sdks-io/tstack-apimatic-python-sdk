from __future__ import annotations

from pydantic import Field
from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel


class V1TaskStartEventData(SdkBaseModel):
    """Event data when a task is started"""

    action_items: Optional[list[str]] = Field(default=UNSET, alias="actionItems")
    iteration_id: str = Field(alias="iterationId")
    plan: str
    success_criteria: str = Field(alias="successCriteria")
    task: str
    timestamp: float
    url: str


class V1TaskStartEventDataDict(TypedDict):
    action_items: NotRequired[list[str]]
    iteration_id: str
    plan: str
    success_criteria: str
    task: str
    timestamp: float
    url: str
