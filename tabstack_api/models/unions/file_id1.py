from __future__ import annotations

from typing import TypeAlias

FileId1: TypeAlias = str | dict[str, str]
"""ID of the file.

If you use multiple providers, you need to specify the provider specific ids using the Record option. The key is the
provider name, e.g. 'openai' or 'anthropic'."""

FileId1Dict: TypeAlias = str | dict[str, str]
