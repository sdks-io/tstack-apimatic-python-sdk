from __future__ import annotations

from typing import TypeAlias

from ..content import Content, ContentDict
from ..error_json import ErrorJson, ErrorJsonDict
from ..error_text import ErrorText, ErrorTextDict
from ..execution_denied import ExecutionDenied, ExecutionDeniedDict
from ..json import Json, JsonDict
from ..text2 import Text2, Text2Dict

Output: TypeAlias = Text2 | Json | ExecutionDenied | ErrorText | ErrorJson | Content
"""Result of the tool call. This is a JSON-serializable object."""

OutputDict: TypeAlias = Text2Dict | JsonDict | ExecutionDeniedDict | ErrorTextDict | ErrorJsonDict | ContentDict
