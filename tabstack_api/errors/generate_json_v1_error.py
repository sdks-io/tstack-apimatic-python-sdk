from __future__ import annotations

from dataclasses import dataclass
from typing import Final, TypeAlias

from ..core import ErrorMapper, RawError, decode_json
from ..models.v1_error_response import V1ErrorResponse

GenerateJsonV1ErrorBody: TypeAlias = V1ErrorResponse | RawError


@dataclass(frozen=True, slots=True)
class _GenerateJsonV1Error:
    def map(self, status_code: int, content: bytes) -> GenerateJsonV1ErrorBody:
        match status_code:
            case 400 | 401 | 402 | 422 | 429 | 500:
                return decode_json[V1ErrorResponse](content)
            case _:
                return RawError(status_code, content)


generate_json_v1_error_mapper: Final[ErrorMapper[GenerateJsonV1ErrorBody]] = _GenerateJsonV1Error()
