from __future__ import annotations

from dataclasses import dataclass
from typing import Final, TypeAlias

from ..core import ErrorMapper, RawError, decode_json
from ..models.v1_error_response import V1ErrorResponse

AutomateInputV1ErrorBody: TypeAlias = V1ErrorResponse | RawError


@dataclass(frozen=True, slots=True)
class _AutomateInputV1Error:
    def map(self, status_code: int, content: bytes) -> AutomateInputV1ErrorBody:
        match status_code:
            case 400 | 401 | 402 | 410 | 429 | 500 | 503:
                return decode_json[V1ErrorResponse](content)
            case _:
                return RawError(status_code, content)


automate_input_v1_error_mapper: Final[ErrorMapper[AutomateInputV1ErrorBody]] = _AutomateInputV1Error()
