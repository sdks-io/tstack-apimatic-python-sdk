from enum import Enum
from typing import Annotated, TypeAlias

from ...core import open_enum_validator


class FinishReason(str, Enum):
    STOP = "stop"
    LENGTH = "length"
    CONTENT_FILTER = "content-filter"
    TOOL_CALLS = "tool-calls"
    ERROR = "error"
    OTHER = "other"

    __str__ = str.__str__


FinishReasonOrStr: TypeAlias = Annotated[FinishReason | str, open_enum_validator(FinishReason)]
