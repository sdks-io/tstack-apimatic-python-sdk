from __future__ import annotations

from typing_extensions import TypedDict

from ..core import SdkBaseModel
from .v1_reasoning_event_data import V1ReasoningEventData, V1ReasoningEventDataDict


class V1AutomateEventAgentReasoned(SdkBaseModel):
    """Envelope for the "agent:reasoned" event from /v1/automate."""

    event: str
    data: V1ReasoningEventData
    """Event data for agent reasoning"""


class V1AutomateEventAgentReasonedDict(TypedDict):
    event: str
    data: V1ReasoningEventDataDict
