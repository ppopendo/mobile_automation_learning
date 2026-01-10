# Automation TODO List

This document tracks remaining tasks, improvements, and technical debt for the mobile automation project.

## 🚨 Critical Items
- [ ] **Login Analysis**: Resolve the "Page Object exists, no dedicated tests" status for Login. Implement a robust `test_login.py` suite covering:
  - Successful login
  - Invalid credentials
  - Empty fields validation
- [ ] **Data Management**: Verify if `data/users.json` is effectively used in all tests or if hardcoded values exist.

## 🔄 Improvements & Refactoring (from Test Plan)

### Slider Feature
- [ ] **Drag Gesture**: Add strict drag gesture tests (currently mostly tapping).
- [ ] **Value Assertion**: Add assertion for actual slider value text changes (currently validating position/response).
- [ ] **Locator Verification**: Verify `SLIDER_ELEMENT` and `SLIDER_VALUE_TEXT` locators during a debug session.

### Photo View Feature
- [ ] **Pan Gestures**: Implement and test pan gestures in multiple directions (Up/Down/Left/Right).

### Carousel Feature
- [ ] **Edge Cases**: Add tests for boundary conditions (swiping past first/last item).

### General
- [ ] **Wait Strategy Audit**: Review all `time.sleep()` usages (if any remain) and replace with explicit waits.
- [ ] **Locator Strategy**: Ensure all new locators use `AppiumBy` and are strictly typed in `Locator` dataclasses.
- [ ] **CI/CD**: Set up a basic CI pipeline file (e.g., GitHub Actions workflow) to run tests on pull requests.

## 📝 Documentation
- [ ] **Docstrings**: Ensure all new Page Objects (`WebViewPage`, `NativeViewDemoPage`, etc.) have full Google-style docstrings.
- [ ] **README**: Update the main project README with instructions on running the new test suites (`pytest tests/vodqa/test_web_view.py`, etc.).

