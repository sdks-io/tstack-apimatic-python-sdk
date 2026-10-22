from __future__ import annotations

from pydantic import Field
from typing_extensions import TypedDict

from ..core import SdkBaseModel


class V1TraceContextEventData(SdkBaseModel):
    """Payload for the task:trace_context event. Carries the OpenTelemetry trace ID for this /v1/automate request so
    consumers can deep-link to distributed-tracing UIs (e.g. Cloud Trace, Cloud Logging) for the run."""

    trace_id: str = Field(alias="traceId")
    """W3C trace ID — 32-character lowercase hexadecimal string."""


class V1TraceContextEventDataDict(TypedDict):
    trace_id: str
