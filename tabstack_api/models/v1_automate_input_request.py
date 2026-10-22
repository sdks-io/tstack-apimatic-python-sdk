from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .v1_automate_input_field_value import V1AutomateInputFieldValue, V1AutomateInputFieldValueDict


class V1AutomateInputRequest(SdkBaseModel):
    cancelled: Optional[bool] = UNSET
    """Set to true to cancel/decline the request"""

    fields: Optional[list[V1AutomateInputFieldValue]] = UNSET
    """Field values as array of {ref, value} pairs (required when not cancelled)"""


class V1AutomateInputRequestDict(TypedDict):
    cancelled: NotRequired[bool]
    fields: NotRequired[list[V1AutomateInputFieldValueDict]]
