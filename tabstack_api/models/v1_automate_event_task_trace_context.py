from __future__ import annotations

from typing_extensions import TypedDict

from ..core import SdkBaseModel
from .v1_trace_context_event_data import V1TraceContextEventData, V1TraceContextEventDataDict


class V1AutomateEventTaskTraceContext(SdkBaseModel):
    """Envelope for the "task:trace_context" event from /v1/automate."""

    event: str
    data: V1TraceContextEventData
    """Payload for the task:trace_context event. Carries the OpenTelemetry trace ID for this /v1/automate request so
    consumers can deep-link to distributed-tracing UIs (e.g. Cloud Trace, Cloud Logging) for the run."""


class V1AutomateEventTaskTraceContextDict(TypedDict):
    event: str
    data: V1TraceContextEventDataDict
