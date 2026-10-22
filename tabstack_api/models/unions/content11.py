from __future__ import annotations

from typing import TypeAlias

from ..tool_approval_response import ToolApprovalResponse, ToolApprovalResponseDict
from ..tool_result import ToolResult, ToolResultDict

Content11: TypeAlias = ToolResult | ToolApprovalResponse

Content11Dict: TypeAlias = ToolResultDict | ToolApprovalResponseDict
