"""
UserLoginForm suite - local conftest.py

Suite-specific configuration for login functionality tests.

Note: Login page setup is handled by the shared `login_page` fixture
from tests/fixtures/fixtures_navigation.py which:
1. Opens the side menu
2. Logs out the user if logged in
3. Navigates to the login form
4. Returns a ready LoginPage instance

Tests in this suite should use the `login_page` fixture directly.
"""
