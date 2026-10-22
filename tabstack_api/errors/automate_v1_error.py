from __future__ import annotations

from dataclasses import dataclass
from typing import Final, TypeAlias

from ..core import ErrorMapper, RawError, decode_json
from ..models.automate_response import AutomateResponse

AutomateV1ErrorBody: TypeAlias = AutomateResponse | RawError


@dataclass(frozen=True, slots=True)
class _AutomateV1Error:
    def map(self, status_code: int, content: bytes) -> AutomateV1ErrorBody:
        match status_code:
            case 400:
                return decode_json[AutomateResponse](content)
            case 401 | 402 | 429 | 500 | 503:
                return RawError(status_code, content)
            case _:
                return RawError(status_code, content)


automate_v1_error_mapper: Final[ErrorMapper[AutomateV1ErrorBody]] = _AutomateV1Error()
