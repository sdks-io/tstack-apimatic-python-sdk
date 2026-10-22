from __future__ import annotations

from typing import TypeAlias

from .v1_alias9221552061564119221552060129727133205725 import (
    V1Alias9221552061564119221552060129727133205725,
    V1Alias9221552061564119221552060129727133205725Dict,
)

V1Alias9221552064114769221552060129727: TypeAlias = (
    str | float | bool | list[V1Alias9221552061564119221552060129727133205725]
)
"""A JSON value can be a string, number, boolean, object, array, or null. JSON values can be serialized and deserialized
by the JSON.stringify and JSON.parse methods."""

V1Alias9221552064114769221552060129727Dict: TypeAlias = (
    str | float | bool | list[V1Alias9221552061564119221552060129727133205725Dict]
)
