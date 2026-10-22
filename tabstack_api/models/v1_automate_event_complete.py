from __future__ import annotations

from typing_extensions import TypedDict

from ..core import SdkBaseModel
from .v1_task_execution_result import V1TaskExecutionResult, V1TaskExecutionResultDict


class V1AutomateEventComplete(SdkBaseModel):
    """Envelope for the "complete" event from /v1/automate."""

    event: str
    data: V1TaskExecutionResult
    """Payload for the ``complete`` stream event. Structurally identical to TaskExecutionResult from webAgent.ts — the
    ``complete`` event's data is the agent's final TaskExecutionResult, stringified onto the SSE stream."""


class V1AutomateEventCompleteDict(TypedDict):
    event: str
    data: V1TaskExecutionResultDict
