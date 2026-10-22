from __future__ import annotations

from typing_extensions import TypedDict

from ..core import SdkBaseModel
from .error import Error, ErrorDict


class V1StreamErrorEventData(SdkBaseModel):
    """Payload for the top-level ``error`` stream event. Emitted when an uncaught error escapes the task runner. Mirrors
    ``ErrorResponse`` from the server package's ``taskRunner.ts`` — kept structurally aligned so schema and runtime stay
    consistent. Distinct from agent-level error events like ``ai:generation:error`` and ``task:validation_error``, which
    are emitted through the normal event emitter during the agent loop."""

    error: Error
    success: bool


class V1StreamErrorEventDataDict(TypedDict):
    error: ErrorDict
    success: bool
