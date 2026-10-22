from __future__ import annotations

from typing_extensions import TypedDict

from ..core import SdkBaseModel
from .v1_action_result_event_data import V1ActionResultEventData, V1ActionResultEventDataDict


class V1AutomateEventBrowserActionCompleted(SdkBaseModel):
    """Envelope for the "browser:action_completed" event from /v1/automate."""

    event: str
    data: V1ActionResultEventData
    """Event data for action results"""


class V1AutomateEventBrowserActionCompletedDict(TypedDict):
    event: str
    data: V1ActionResultEventDataDict
