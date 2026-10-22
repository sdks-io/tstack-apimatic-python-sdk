from __future__ import annotations

from pydantic import Field
from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel


class ToolApprovalResponse(SdkBaseModel):
    """Tool approval response prompt part."""

    approval_id: str = Field(alias="approvalId")
    """ID of the tool approval."""

    approved: bool
    """Flag indicating whether the approval was granted or denied."""

    provider_executed: Optional[bool] = Field(default=UNSET, alias="providerExecuted")
    """Flag indicating whether the tool call is provider-executed. Only provider-executed tool approval responses should
    be sent to the model."""

    reason: Optional[str] = UNSET
    """Optional reason for the approval or denial."""

    type_: str = Field(alias="type")


class ToolApprovalResponseDict(TypedDict):
    approval_id: str
    approved: bool
    provider_executed: NotRequired[bool]
    reason: NotRequired[str]
    type_: str
