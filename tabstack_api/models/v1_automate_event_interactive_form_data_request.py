from __future__ import annotations

from typing_extensions import TypedDict

from ..core import SdkBaseModel
from .v1_interactive_form_data_request_event_data import (
    V1InteractiveFormDataRequestEventData,
    V1InteractiveFormDataRequestEventDataDict,
)


class V1AutomateEventInteractiveFormDataRequest(SdkBaseModel):
    """Envelope for the "interactive:form_data:request" event from /v1/automate."""

    event: str
    data: V1InteractiveFormDataRequestEventData
    """Event data when the agent requests user data for form fields"""


class V1AutomateEventInteractiveFormDataRequestDict(TypedDict):
    event: str
    data: V1InteractiveFormDataRequestEventDataDict
