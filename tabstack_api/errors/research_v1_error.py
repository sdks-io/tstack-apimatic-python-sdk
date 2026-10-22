from __future__ import annotations

from dataclasses import dataclass
from typing import Final, TypeAlias

from ..core import ErrorMapper, RawError

ResearchV1ErrorBody: TypeAlias = RawError


@dataclass(frozen=True, slots=True)
class _ResearchV1Error:
    def map(self, status_code: int, content: bytes) -> ResearchV1ErrorBody:
        match status_code:
            case 400 | 401 | 402 | 429 | 500 | 503:
                return RawError(status_code, content)
            case _:
                return RawError(status_code, content)


research_v1_error_mapper: Final[ErrorMapper[ResearchV1ErrorBody]] = _ResearchV1Error()
