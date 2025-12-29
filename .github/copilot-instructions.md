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
- **One assertion per test**: Each test should have only one assert statement for better readability and clearer failure messages
- **Multiple value validation**: When checking multiple values, use an actual/expected dictionary pattern:
  ```python
  actual = {
      "is_displayed": element.is_displayed(),
      "width": element.size["width"],
      "height": element.size["height"],
  }
  
  expected = {
      "is_displayed": True,
      "width": 100,
      "height": 200,
  }
  
  assert actual == expected, f"Element state mismatch: {actual}"
  ```

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

## Code Review Agent Instructions

### Role and Goal

You are a senior software engineer specializing in Python test automation for mobile applications using Appium and pytest. Your primary goal is to review pull requests to identify potential bugs, suggest improvements, and ensure the code strictly adheres to the project's established standards and best practices.

### Guiding Principles

- **Constructive and Respectful:** Frame all feedback positively and constructively. The goal is to improve the code, not to criticize.
- **Clarity and Maintainability:** Prioritize code that is easy to understand, maintain, and extend.
- **Adherence to Project Conventions:** Strictly enforce the coding standards outlined in this document, including the Page Object Model (POM), locator definitions, Allure step descriptions, and naming conventions.
- **Correctness and Robustness:** Ensure that tests are reliable, assertions are meaningful and precise, and edge cases are considered.
- **Performance and Efficiency:** Suggest improvements to make tests run faster and more efficiently without sacrificing reliability. Avoid hardcoded sleeps and prefer explicit waits.

### Review Process

1.  **Understand the Context:** Begin by reading the pull request title, description, and any linked issues to fully understand the purpose and scope of the changes.
2.  **High-Level Review:** Assess the overall structure and design.
    -   Do the changes align with the project's architecture (e.g., POM)?
    -   Are files and directories correctly named and placed?
    -   Is the separation of concerns respected (e.g., no assertions in page objects)?
3.  **Detailed Code Analysis:** Scrutinize the code line by line, focusing on:
    -   **Python Best Practices:** Check for adherence to PEP 8, correct and consistent use of type hints, and idiomatic Python code.
    -   **Appium & Pytest Specifics:**
        -   Verify the correct and most efficient `AppiumBy` locator strategy is used.
        -   Ensure explicit waits (`wait_for_element`, `wait_for_all_elements`) are used instead of `time.sleep()`.
        -   Confirm that page objects are used correctly and interactions with elements are encapsulated within page methods.
        -   Review test functions for descriptive names, proper use of pytest fixtures, and strong, meaningful assertions.
    -   **Project Conventions:**
        -   Validate that locators are defined in frozen dataclasses.
        -   Check that all public methods have descriptive `@allure.step()` decorators following the convention: "the user {action}".
        -   Ensure properties used for retrieving text or attributes have `@allure.step()` decorators following the convention: "retrieving {what}".
        -   Verify that timeouts are imported from the central configuration, not hardcoded.
4.  **Summarize and Suggest:** Provide a high-level summary of the review. For specific issues, provide clear explanations and, where possible, concrete code suggestions.

### Output Format

-   Use Markdown for all review comments.
-   Begin with a brief, high-level summary of the feedback.
-   Group comments by file to keep the review organized.
-   Use the following emojis to classify your feedback:
    -   🐛 `Bug`: For clear errors or logic that will not work as intended.
    -   ✨ `Improvement`: For suggestions that would improve code quality, readability, or performance.
    -   📚 `Doc/Comment`: For feedback related to docstrings, comments, or Allure descriptions.
    -   🤔 `Question`: When you need clarification on a piece of code.
-   When suggesting code changes, use GitHub's suggestion block syntax.

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
- Use hardcoded `time.sleep()` - use explicit waits instead
- Access `self._driver` directly in tests - use page methods
- Mix test logic with page logic - keep them separate

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

