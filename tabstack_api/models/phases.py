from __future__ import annotations

from typing_extensions import TypedDict

from ..core import SdkBaseModel


class Phases(SdkBaseModel):
    duration: float


class PhasesDict(TypedDict):
    duration: float
