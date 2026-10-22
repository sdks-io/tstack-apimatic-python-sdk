from __future__ import annotations

from pydantic import Field
from typing_extensions import TypedDict

from ..core import SdkBaseModel


class ToolApprovalRequest(SdkBaseModel):
    """Tool approval request prompt part."""

    approval_id: str = Field(alias="approvalId")
    """ID of the tool approval."""

    tool_call_id: str = Field(alias="toolCallId")
    """ID of the tool call that the approval request is for."""

    type_: str = Field(alias="type")


class ToolApprovalRequestDict(TypedDict):
    approval_id: str
    tool_call_id: str
    type_: str
