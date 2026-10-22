from __future__ import annotations

from typing_extensions import TypedDict

from ..core import SdkBaseModel
from .enums.v1_task_error_code import V1TaskErrorCodeOrStr


class V1TaskError(SdkBaseModel):
    """Structured error information for failed tasks"""

    code: V1TaskErrorCodeOrStr
    """Error code for programmatic handling"""

    message: str
    """Human-readable error message"""


class V1TaskErrorDict(TypedDict):
    code: V1TaskErrorCodeOrStr
    message: str
