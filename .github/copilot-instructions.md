# GitHub Copilot Instructions

## Project Overview

This is a mobile automation testing project using Python with Appium for Android app testing. The project follows the Page Object Model (POM) design pattern.

## Tech Stack

- **Language**: Python 3.12+
- **Testing Framework**: pytest
- **Mobile Automation**: Appium Python Client
- **Reporting**: Allure
- **Code Quality**: Black, Pylint, isort, mypy, pre-commit

## Code Style & Conventions

### General

- Line length: 120 characters (configured in Black and Pylint)
- Use double quotes for strings (Black default)
- Follow PEP 8 style guide
- Use type hints for all function parameters and return types
- All public methods should have docstrings

### Page Object Pattern

- All page classes inherit from `BasePage`
- Locators are defined as frozen dataclasses with `@dataclass(frozen=True)` decorator
- Locator class names follow pattern: `{PageName}Locators` (e.g., `ProductDetailsPageLocators`)
- Locators use `Tuple[str, str]` type with `field(default=(...), init=False)` pattern
- Use `AppiumBy` for locator strategies (XPATH, ID, ACCESSIBILITY_ID, etc.)
- UPPER_CASE naming for locator constants

### Page Class Methods

- Use `@allure.step()` decorator for all public methods with descriptive step names
- Step descriptions should be in format: "the user {action}" (e.g., "the user clicks the login button")
- Use `@property` decorator for getter methods that retrieve element text/attributes
- Property step descriptions should be in format: "retrieving {what}" (e.g., "retrieving product price")
- Return type hints are mandatory

### Waits & Timeouts

- Import timeouts from `config.config_vars`: `TIMEOUT`, `SHORT_TIMEOUT`, `PAGE_LOAD_TIMEOUT`
- Use `wait_for_element()` method from BasePage for element waits
- Use `wait_for_all_elements()` for waiting on multiple elements
- Avoid hardcoded sleep times; use explicit waits instead

### Testing

- Test files go in `tests/` directory
- Use pytest fixtures defined in `conftest.py`
- Test function names should be descriptive: `test_{feature}_{scenario}`
- Use Allure decorators for test metadata: `@allure.feature()`, `@allure.story()`, `@allure.severity()`

## File Structure

```
pages/           # Page Object classes
tests/           # Test files
config/          # Configuration and environment variables
data/            # Test data files
libs/            # Utility libraries and helpers
resources/       # External resources
allure-results/  # Allure report data (gitignored)
```

## Example Patterns

### Locator Definition

```python
from dataclasses import dataclass, field
from typing import Tuple
from appium.webdriver.common.appiumby import AppiumBy

@dataclass(frozen=True)
class ExamplePageLocators:
    BUTTON_LOGIN: Tuple[str, str] = field(
        default=(AppiumBy.ID, "com.example.app:id/loginButton"), init=False
    )
```

### Page Method

```python
@allure.step("the user clicks the login button")
def click_login_button(self) -> None:
    self.tap_element(ExamplePageLocators.BUTTON_LOGIN)

@property
@allure.step("retrieving error message text")
def error_message(self) -> str:
    return self.wait_for_element(ExamplePageLocators.ERROR_MESSAGE).text
```

## Dependencies

When adding new dependencies, add them to `requirements.txt` and ensure compatibility with existing packages.

## Pre-commit Hooks

The project uses pre-commit hooks for code quality. Run `pre-commit run --all-files` before committing.

## Build, Test, and Lint Commands

### Installing Dependencies

```bash
# Create and activate virtual environment
python -m venv .venv
source .venv/bin/activate  # On Windows: .venv\Scripts\Activate.ps1

# Install dependencies
pip install -r requirements.txt

# Install pre-commit hooks
pre-commit install
```

### Running Tests

```bash
# Run all tests
pytest tests/

# Run specific test file
pytest tests/UserLoginForm/test_login.py

# Run specific test case
pytest tests/UserLoginForm/test_login.py::TestLogin::test_successful_login

# Run tests with specific marker
pytest -m regression tests/

# Run tests with Allure report
pytest --alluredir=allure-results tests/

# Generate and open Allure report
allure generate allure-results --clean -o reports
allure open ./reports/
```

### Code Quality Checks

```bash
# Run all pre-commit hooks
pre-commit run --all-files

# Format code with Black
black .

# Run Pylint
pylint pages/ tests/ config/ libs/

# Type checking with mypy
mypy pages/ tests/ config/ libs/

# Sort imports with isort
isort .
```

## Common Patterns and Troubleshooting

### Element Interaction Patterns

**Problem**: Element not found or stale element exceptions
**Solution**: Always use wait methods from `BasePage`:
- Use `wait_for_element()` for single elements
- Use `wait_for_all_elements()` for multiple elements
- Use `safe_send_keys()` for input fields with retry logic
- Use `tap_element()` instead of direct `.click()` for mobile elements

**Problem**: Slow test execution
**Solution**: 
- Use `wait_for_all_elements()` to wait for multiple critical elements in parallel
- Avoid `time.sleep()` - use explicit waits instead
- Import specific timeout constants from `config.config_vars`

### Test Data Management

- Use pytest fixtures for test data (see `conftest.py`)
- Store reusable test data in `data/` directory
- Use `faker` library for generating random test data when needed

### Page Object Best Practices

**Always:**
- Inherit from `BasePage`
- Define locators as frozen dataclasses at the top of the file
- Use `@allure.step()` decorators on all public methods
- Use descriptive step names in natural language
- Return type hints are mandatory

**Never:**
- Don't use hardcoded `time.sleep()` - use explicit waits
- Don't access `self._driver` directly in tests - use page methods
- Don't mix test logic with page logic - keep them separate

## Security Considerations

- Never hardcode credentials in test files
- Use environment variables for sensitive data (stored in `.env` file, not committed)
- Use the `.env_template` file as a reference for required environment variables
- Test data should not contain real user information

## Test Organization

Tests are organized by feature in subdirectories under `tests/`:
- `tests/UserLoginForm/` - Login functionality tests
- `tests/CheckoutFlow/` - Checkout process tests
- `tests/CheckoutShippingAddress/` - Shipping address tests
- `tests/General/` - General utility tests

Each test class should:
- Use `@allure.epic()`, `@allure.feature()`, `@allure.story()` decorators
- Use `@pytest.mark.tcid()` for test case IDs
- Use `@pytest.mark.regression` or other markers for test categorization
- Use descriptive class names: `Test{Feature}` (e.g., `TestLogin`)

## Debugging Tips

- Use `allure.attach()` to add screenshots or data to test reports
- Check `allure-results/` directory for test execution details
- Use `pytest -v` for verbose test output
- Use `pytest --log-cli-level=INFO` to see logging output during test runs
- Use `--capture=no` or `-s` flag to see print statements during test execution

