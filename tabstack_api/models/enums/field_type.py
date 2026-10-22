from enum import Enum
from typing import Annotated, TypeAlias

from ...core import open_enum_validator


class FieldType(str, Enum):
    """Semantic field type"""

    TEXT = "text"
    EMAIL = "email"
    PHONE = "phone"
    DATE = "date"
    NUMBER = "number"
    SELECT = "select"
    CHECKBOX = "checkbox"
    RADIO = "radio"
    TEXTAREA = "textarea"
    PASSWORD = "password"
    OTHER = "other"

    __str__ = str.__str__


FieldTypeOrStr: TypeAlias = Annotated[FieldType | str, open_enum_validator(FieldType)]
