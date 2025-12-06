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

