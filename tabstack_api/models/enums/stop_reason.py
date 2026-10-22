from enum import Enum
from typing import Annotated, TypeAlias

from ...core import open_enum_validator


class StopReason(str, Enum):
    """Why research iterations stopped (only present when isLast is true)"""

    MAX_ITERATIONS = "max_iterations"
    COVERAGE_SUFFICIENT = "coverage_sufficient"

    __str__ = str.__str__


StopReasonOrStr: TypeAlias = Annotated[StopReason | str, open_enum_validator(StopReason)]
