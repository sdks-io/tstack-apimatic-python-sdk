from __future__ import annotations

from typing_extensions import TypedDict

from ..core import SdkBaseModel
from .v1_task_metrics_event_data import V1TaskMetricsEventData, V1TaskMetricsEventDataDict


class V1AutomateEventTaskMetrics(SdkBaseModel):
    """Envelope for the "task:metrics" event from /v1/automate."""

    event: str
    data: V1TaskMetricsEventData


class V1AutomateEventTaskMetricsDict(TypedDict):
    event: str
    data: V1TaskMetricsEventDataDict
