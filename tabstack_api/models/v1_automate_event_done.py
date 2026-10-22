from __future__ import annotations

from typing import Any

from typing_extensions import TypedDict

from ..core import SdkBaseModel


class V1AutomateEventDone(SdkBaseModel):
    """Envelope for the "done" event from /v1/automate."""

    event: str
    data: dict[str, Any]
    """Payload for the ``done`` stream terminator event. Empty today; reserved for future metadata."""


class V1AutomateEventDoneDict(TypedDict):
    event: str
    data: dict[str, Any]
