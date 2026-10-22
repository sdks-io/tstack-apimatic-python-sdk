from enum import Enum
from typing import Annotated, TypeAlias

from ...core import open_enum_validator


class Status(str, Enum):
    """Status: answered (clear info), partial (some info, gaps remain), unanswered (no relevant info)"""

    ANSWERED = "answered"
    PARTIAL = "partial"
    UNANSWERED = "unanswered"

    __str__ = str.__str__


StatusOrStr: TypeAlias = Annotated[Status | str, open_enum_validator(Status)]
