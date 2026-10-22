from enum import Enum
from typing import Annotated, TypeAlias

from ...core import open_enum_validator


class CompletionQuality(str, Enum):
    FAILED = "failed"
    PARTIAL = "partial"
    COMPLETE = "complete"
    EXCELLENT = "excellent"

    __str__ = str.__str__


CompletionQualityOrStr: TypeAlias = Annotated[CompletionQuality | str, open_enum_validator(CompletionQuality)]
