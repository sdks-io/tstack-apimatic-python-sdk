from __future__ import annotations

from typing_extensions import TypedDict

from ..core import SdkBaseModel
from .v1_interactive_form_data_error_event_data import (
    V1InteractiveFormDataErrorEventData,
    V1InteractiveFormDataErrorEventDataDict,
)


class V1AutomateEventInteractiveFormDataError(SdkBaseModel):
    """Envelope for the "interactive:form_data:error" event from /v1/automate."""

    event: str
    data: V1InteractiveFormDataErrorEventData
    """Event data when form validation fails and the agent re-requests data. Carries both the error context and the
    fields that need new values. Callers respond to this the same way as a request event."""


class V1AutomateEventInteractiveFormDataErrorDict(TypedDict):
    event: str
    data: V1InteractiveFormDataErrorEventDataDict
