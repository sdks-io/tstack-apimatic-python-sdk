from __future__ import annotations

from typing import Any, TypeAlias

from .v1_alias9221552061564119221552060129727133205725 import (
    V1Alias9221552061564119221552060129727133205725,
    V1Alias9221552061564119221552060129727133205725Dict,
)

ProviderOptions: TypeAlias = str | float | bool | dict[str, Any] | list[V1Alias9221552061564119221552060129727133205725]
"""A JSON value can be a string, number, boolean, object, array, or null. JSON values can be serialized and deserialized
by the JSON.stringify and JSON.parse methods."""

ProviderOptionsDict: TypeAlias = (
    str | float | bool | dict[str, Any] | list[V1Alias9221552061564119221552060129727133205725Dict]
)
