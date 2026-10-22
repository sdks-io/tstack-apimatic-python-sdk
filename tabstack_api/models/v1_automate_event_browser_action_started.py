from __future__ import annotations

from typing_extensions import TypedDict

from ..core import SdkBaseModel
from .v1_action_execution_event_data import V1ActionExecutionEventData, V1ActionExecutionEventDataDict


class V1AutomateEventBrowserActionStarted(SdkBaseModel):
    """Envelope for the "browser:action_started" event from /v1/automate."""

    event: str
    data: V1ActionExecutionEventData
    """Event data for action execution"""


class V1AutomateEventBrowserActionStartedDict(TypedDict):
    event: str
    data: V1ActionExecutionEventDataDict
