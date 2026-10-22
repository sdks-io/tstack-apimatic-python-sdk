from enum import Enum
from typing import Annotated, TypeAlias

from ...core import open_enum_validator


class V1TaskErrorCode(str, Enum):
    """Error codes for task failures"""

    TASK_ABORTED = "TASK_ABORTED"
    MAX_ITERATIONS = "MAX_ITERATIONS"
    MAX_ERRORS = "MAX_ERRORS"
    TASK_FAILED = "TASK_FAILED"

    __str__ = str.__str__


V1TaskErrorCodeOrStr: TypeAlias = Annotated[V1TaskErrorCode | str, open_enum_validator(V1TaskErrorCode)]
