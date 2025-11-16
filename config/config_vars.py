"""Simple configuration variables.
Keep only simple constants here (timeouts, retries) — environment values should be in `config/.env`.
"""

from typing import Final


TIMEOUT: Final[int] = 30
APPIUM_CONNECT_RETRIES: Final[int] = 5
APPIUM_CONNECT_DELAY: Final[float] = 2.0
