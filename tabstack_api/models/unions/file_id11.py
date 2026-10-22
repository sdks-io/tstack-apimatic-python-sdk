from __future__ import annotations

from typing import TypeAlias

FileId11: TypeAlias = str | dict[str, str]
"""Image that is referenced using a provider file id.

If you use multiple providers, you need to specify the provider specific ids using the Record option. The key is the
provider name, e.g. 'openai' or 'anthropic'."""

FileId11Dict: TypeAlias = str | dict[str, str]
