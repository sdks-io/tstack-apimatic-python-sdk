from __future__ import annotations

from typing_extensions import TypedDict

from ..core import SdkBaseModel
from .v1_stream_error_event_data import V1StreamErrorEventData, V1StreamErrorEventDataDict


class V1AutomateEventError(SdkBaseModel):
    """Envelope for the "error" event from /v1/automate."""

    event: str
    data: V1StreamErrorEventData
    """Payload for the top-level ``error`` stream event. Emitted when an uncaught error escapes the task runner. Mirrors
    ``ErrorResponse`` from the server package's ``taskRunner.ts`` — kept structurally aligned so schema and runtime stay
    consistent. Distinct from agent-level error events like ``ai:generation:error`` and ``task:validation_error``, which
    are emitted through the normal event emitter during the agent loop."""


class V1AutomateEventErrorDict(TypedDict):
    event: str
    data: V1StreamErrorEventDataDict
