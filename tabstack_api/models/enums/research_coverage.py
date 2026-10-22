from enum import Enum
from typing import Annotated, TypeAlias

from ...core import open_enum_validator


class ResearchCoverage(str, Enum):
    """Research coverage level - assesses quality across all questions.

    Hierarchy: Light < Moderate < Solid < Comprehensive

    - **Light**: Basic info on some questions, most need more depth → Continue
    - **Moderate**: Multiple questions answered, some remain partial → Continue
    - **Solid**: Most questions well-answered with validated sources → Sufficient to stop
    - **Comprehensive**: All questions thoroughly answered, exceptional depth → Definitely stop"""

    LIGHT = "Light"
    MODERATE = "Moderate"
    SOLID = "Solid"
    COMPREHENSIVE = "Comprehensive"

    __str__ = str.__str__


ResearchCoverageOrStr: TypeAlias = Annotated[ResearchCoverage | str, open_enum_validator(ResearchCoverage)]
