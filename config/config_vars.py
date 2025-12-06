"""Simple configuration variables.
Keep only simple constants here (timeouts, retries) — environment values should be in `config/.env`.
"""

from typing import Final


# Default timeout for element waits (reduced for faster feedback)
TIMEOUT: Final[int] = 15
# Short timeout for quick element checks
SHORT_TIMEOUT: Final[int] = 5
# Page load timeout - used when waiting for pages to load
PAGE_LOAD_TIMEOUT: Final[int] = 10
APPIUM_CONNECT_RETRIES: Final[int] = 5
APPIUM_CONNECT_DELAY: Final[float] = 2.0
