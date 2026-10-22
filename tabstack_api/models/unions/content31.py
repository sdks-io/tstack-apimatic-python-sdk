from __future__ import annotations

from typing import TypeAlias

from ..file import File, FileDict
from ..reasoning import Reasoning, ReasoningDict
from ..text import Text, TextDict
from ..tool_approval_request import ToolApprovalRequest, ToolApprovalRequestDict
from ..tool_call import ToolCall, ToolCallDict
from ..tool_result import ToolResult, ToolResultDict

Content31: TypeAlias = Text | File | Reasoning | ToolCall | ToolResult | ToolApprovalRequest

Content31Dict: TypeAlias = TextDict | FileDict | ReasoningDict | ToolCallDict | ToolResultDict | ToolApprovalRequestDict
