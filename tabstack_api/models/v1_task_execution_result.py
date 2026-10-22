from __future__ import annotations

from pydantic import Field
from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .stats import Stats, StatsDict
from .v1_task_error import V1TaskError, V1TaskErrorDict


class V1TaskExecutionResult(SdkBaseModel):
    error: Optional[V1TaskError] = UNSET
    """Error details when success is false"""

    final_answer: str | None = Field(alias="finalAnswer")
    """Final answer or result from the agent"""

    stats: Stats
    """Execution statistics"""

    success: bool
    """Whether the task completed successfully"""


class V1TaskExecutionResultDict(TypedDict):
    error: NotRequired[V1TaskErrorDict]
    final_answer: str | None
    stats: StatsDict
    success: bool
