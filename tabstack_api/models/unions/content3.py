from __future__ import annotations

from typing import TypeAlias

from .content1 import Content1, Content1Dict

Content3: TypeAlias = str | list[Content1]
"""Content of a user message. It can be a string or an array of text and image parts."""

Content3Dict: TypeAlias = str | list[Content1Dict]
