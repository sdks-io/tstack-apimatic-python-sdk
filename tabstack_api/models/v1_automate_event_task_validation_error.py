from __future__ import annotations

from typing_extensions import TypedDict

from ..core import SdkBaseModel
from .v1_validation_error_event_data import V1ValidationErrorEventData, V1ValidationErrorEventDataDict


class V1AutomateEventTaskValidationError(SdkBaseModel):
    """Envelope for the "task:validation_error" event from /v1/automate."""

    event: str
    data: V1ValidationErrorEventData
    """Event data for validation errors during action response processing"""


class V1AutomateEventTaskValidationErrorDict(TypedDict):
    event: str
    data: V1ValidationErrorEventDataDict
