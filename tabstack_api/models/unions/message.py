from __future__ import annotations

from typing import TypeAlias

from ..assistant import Assistant, AssistantDict
from ..system import System, SystemDict
from ..tool import Tool, ToolDict
from ..user import User, UserDict

Message: TypeAlias = System | User | Assistant | Tool
"""A message that can be used in the ``messages`` field of a prompt. It can be a user message, an assistant message, or
a tool message."""

MessageDict: TypeAlias = SystemDict | UserDict | AssistantDict | ToolDict
