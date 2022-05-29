# SPDX-License-Identifier: MIT
# Copyright (c) 2022, Mathias Laurin

from __future__ import annotations

from typing import Optional, Sequence

algorithms_guaranteed: Sequence[str]
algorithms_available: Sequence[str]

class Hash:
    def __init__(
        self,
        name: str,
        buffer: Optional[bytes] = None,
        *,
        block_size: int = ...,
    ) -> None: ...
    @property
    def digest_size(self) -> int: ...
    @property
    def block_size(self) -> int: ...
    @property
    def name(self) -> str: ...
    def update(self, buffer: bytes) -> None: ...
    def digest(self) -> bytes: ...
    def hexdigest(self) -> str: ...
    def copy(self) -> Hash: ...

class Hmac:
    def __init__(
        self,
        key: bytes,
        name: str,
        buffer: Optional[bytes] = None,
        *,
        block_size: int,
    ) -> None: ...
    @property
    def digest_size(self) -> int: ...
    @property
    def block_size(self) -> int: ...
    @property
    def name(self) -> str: ...
    def update(self, buffer: bytes) -> None: ...
    def digest(self) -> bytes: ...
    def hexdigest(self) -> str: ...
    def copy(self) -> Hmac: ...
