# Mobile App Testing Plan: VodQA - Comprehensive Test Plan

**Objective:** Comprehensive test plan for the VodQA mobile application to guide test automation implementation using the Page Object Model pattern with Appium and pytest.

## Application Details

| Property | Value |
|----------|-------|
| **App** | `VodQA.apk` |
| **Package** | `com.vodqareactnative` |
| **Activity** | `com.vodqareactnative.MainActivity` |
| **Location** | `apk/` directory |

## Test Environment

| Property | Value                            |
|----------|----------------------------------|
| **Appium Server** | `APPIUM_SERVER_URL` in .env file |
| **Device** | `DEVICE_NAME` in .env file       |
| **Platform** | `PLATFORM_VERSION` in .env file  |
| **Automation** | UiAutomator2                     |

## Credentials

- **File:** `data/users.json`
- **Path:** `valid_users[2]`
- **Username:** `admin`
- **Password:** `admin`

---

## Automation Coverage Summary

| Feature | Status | Test Count | Page Object | Notes |
|---------|--------|------------|-------------|-------|
| 0. Login | ⏳ Partial | 0 | ✅ `LoginPage` | Page Object exists, no dedicated tests |
| 1. Native View | 🔲 Not Started | 0 | 🔲 - | - |
| **2. Slider** | ✅ **Automated** | **5** | ✅ `SliderPage` | TC-02-01, TC-02-02, TC-02-03 complete |
| 3. Vertical Swiping | 🔲 Not Started | 0 | 🔲 - | - |
| 4. Drag and Drop | 🔲 Not Started | 0 | 🔲 - | - |
| 5. Double Tap | 🔲 Not Started | 0 | 🔲 - | - |
| 6. Long Press | 🔲 Not Started | 0 | 🔲 - | - |
| 7. Photo View | 🔲 Not Started | 0 | 🔲 - | - |
| 8. Web View | 🔲 Not Started | 0 | 🔲 - | - |
| 9. Carousel | 🔲 Not Started | 0 | 🔲 - | - |
| 10. Wheel Picker | 🔲 Not Started | 0 | 🔲 - | - |

**Total Automated Tests:** 5 (tests/vodqa/test_slider.py)  
**Last Updated:** 2025-12-13  
**Last Test Run:** ✅ 5 passed in 120.28s

---

## Test Scenarios

### 0. Initial Setup and Login

**Description:** User authentication flow to access the VodQA application features.

**Prerequisites:**
- VodQA app is installed on the device
- Device is connected and accessible via ADB

**Steps:**
1. Launch the VodQA application
2. Wait for the login page to load
3. Enter username in the username field: `admin`
4. Enter password in the password field: `admin`
5. Tap the 'LOG IN' button
6. Wait for navigation to Samples List page

**Expected Outcome:**
- User is successfully authenticated
- Samples List page is displayed with header text 'Samples List'
- All sample options are visible or accessible via scrolling

**Key Locators:**
```python
USERNAME_INPUT = (AppiumBy.ACCESSIBILITY_ID, "username")
PASSWORD_INPUT = (AppiumBy.ACCESSIBILITY_ID, "password")
LOGIN_BUTTON = (AppiumBy.XPATH, "//android.widget.TextView[@text='LOG IN']")
SAMPLES_LIST_HEADER = (AppiumBy.XPATH, "//android.widget.TextView[@text='Samples List']")
```

**Page Object:** `LoginPage` (already exists in `pages/vodqa/login_page.py`)

---

## Samples List Features

### 1. Feature: Native View (Chained View)

**Content Descriptor:** `chainedView`

**Description:** Test navigation through chained/native views within the application.

**Steps to Reproduce:**
1. Navigate to Samples List (after login)
2. Locate 'Native View' option with content-desc='chainedView'
3. Tap on 'Native View'
4. Observe the Native View screen
5. Interact with available elements
6. Tap 'Back' button to return to Samples List

**Expected Outcome:**
- Native View screen opens successfully
- Screen displays expected UI elements
- User can navigate back to Samples List
- No crashes or errors occur

**Locators:**
```python
NATIVE_VIEW_BUTTON = (AppiumBy.XPATH, "//android.widget.TextView[@content-desc='chainedView']")
```

**Automation Recommendations:**
- Create `NativeViewPage` class in `pages/vodqa/`
- Define `NativeViewPageLocators` dataclass
- Implement test: `test_chainedView_navigation`

---

### 2. Feature: Slider

**Content Descriptor:** `slider1`

**Automation Status:** ✅ **AUTOMATED**

| Test Case | Status | Test File | Notes |
|-----------|--------|-----------|-------|
| TC-02-01: Slider page has two sliders | ✅ Automated | `tests/vodqa/test_slider.py::TestSlider::test_slider_page_has_two_sliders` | Verifies both sliders are visible |
| TC-02-02: Slider 1 interaction updates value | ✅ Automated | `tests/vodqa/test_slider.py::TestSlider::test_slider_1_interaction_updates_value` | Tests tap at 50% |
| TC-02-03: Multiple positions (0%, 50%, 100%) | ✅ Automated | `tests/vodqa/test_slider.py::TestSlider::test_slider_1_multiple_positions` | Parametrized test (3 runs) |

**Description:** Test slider/seekbar interaction functionality.

**Steps to Reproduce:**
1. Navigate to Samples List
2. Locate 'Slider' option with content-desc='slider1'
3. Tap on 'Slider'
4. Interact with the slider control (drag to adjust value)
5. Verify slider value changes
6. Tap 'Back' button to return

**Expected Outcome:**
- Slider screen opens with interactive seekbar
- Slider responds to touch and drag gestures
- Slider value updates correctly
- Back navigation works properly

**Locators:**
```python
SLIDER_BUTTON = (AppiumBy.XPATH, "//android.widget.TextView[@content-desc='slider1']")
SLIDER_ELEMENT = (AppiumBy.ACCESSIBILITY_ID, "slider")  # ⚠️ NEEDS VERIFICATION
SLIDER_VALUE_TEXT = (AppiumBy.XPATH, "//android.widget.TextView[contains(@text, 'Value')]")  # ⚠️ NEEDS VERIFICATION
```

**Page Object:** `SliderPage` - `pages/vodqa/slider_page.py`

**Implemented Methods:**
- `wait_until_page_is_loaded()` - waits for header with title "Slider"
- `slide_to_percentage(percentage: int)` - drag slider to specific position
- `tap_slider_at_percentage(percentage: int)` - tap on slider at specific position
- `slider_progress` (property) - retrieves current slider text value
- `slider_bounds` (property) - retrieves slider location and size
- `is_slider_displayed()` - checks if slider is visible
- `tap_back_button()` - navigates back to Samples List

**Automation Recommendations:**
- ~~Create `SliderPage` class~~ ✅ DONE
- ~~Use `BaseAppiumGestures` for drag/swipe actions~~ ✅ DONE
- ~~Test different slider positions (0%, 50%, 100%)~~ ✅ DONE
- ~~Implement test: `test_slider1_interaction`~~ ✅ DONE
- 🔲 Add test for drag gesture (not just tap)
- 🔲 Verify slider value text element locator during exploratory session
- 🔲 Add assertion for actual slider value changes

---

### 3. Feature: Vertical Swiping

**Content Descriptor:** `verticalSwiping`

**Description:** Test vertical scroll/swipe gestures.

**Steps to Reproduce:**
1. Navigate to Samples List
2. Locate 'Vertical Swiping' option
3. Tap on 'Vertical Swiping'
4. Perform vertical swipe gestures (up and down)
5. Verify scrolling behavior
6. Return to Samples List

**Expected Outcome:**
- Vertical Swiping screen displays scrollable content
- Swipe up gesture scrolls content up
- Swipe down gesture scrolls content down
- Smooth scrolling animation

**Locators:**
```python
VERTICAL_SWIPING_BUTTON = (AppiumBy.XPATH, "//android.widget.TextView[@content-desc='verticalSwiping']")
```

**Automation Recommendations:**
- Use `swipe_vertical()` method from `BaseAppiumGestures`
- Test both directions: up and down
- Verify scroll boundaries
- Implement test: `test_verticalSwiping_gestures`

**Existing Page Object:** `SamplesListPage` already has `tap_vertical_swiping()` method

---

### 4. Feature: Drag and Drop

**Content Descriptor:** `dragAndDrop`

**Description:** Test drag and drop gesture functionality.

**Steps to Reproduce:**
1. Navigate to Samples List
2. Locate 'Drag and Drop' option
3. Tap on 'Drag and Drop'
4. Identify draggable elements
5. Perform drag and drop operations
6. Verify element positions after drop
7. Return to Samples List

**Expected Outcome:**
- Drag and Drop screen displays draggable elements
- Elements can be dragged to drop zones
- Drop zones accept dragged elements
- Visual feedback during drag operation

**Locators:**
```python
DRAG_AND_DROP_BUTTON = (AppiumBy.XPATH, "//android.widget.TextView[@content-desc='dragAndDrop']")
```

**Automation Recommendations:**
- Create `DragAndDropPage` class
- Use `drag_and_drop()` method from `BaseAppiumGestures`
- Test multiple drag-drop scenarios
- Verify final element positions
- Implement test: `test_dragAndDrop_functionality`

---

### 5. Feature: Double Tap

**Content Descriptor:** `doubleTap`

**Description:** Test double tap gesture recognition.

**Steps to Reproduce:**
1. Navigate to Samples List
2. Locate 'Double Tap' option
3. Tap on 'Double Tap'
4. Perform double tap gesture on target element
5. Verify double tap action response
6. Return to Samples List

**Expected Outcome:**
- Double Tap screen displays tap-responsive element
- Double tap gesture is recognized correctly
- Expected action occurs after double tap
- Single tap does not trigger double tap action

**Locators:**
```python
DOUBLE_TAP_BUTTON = (AppiumBy.XPATH, "//android.widget.TextView[@content-desc='doubleTap']")
```

**Automation Recommendations:**
- Create `DoubleTapPage` class
- Implement double tap gesture using Actions API
- Test timing sensitivity
- Verify state changes after double tap
- Implement test: `test_doubleTap_gesture`

---

### 6. Feature: Long Press

**Content Descriptor:** `longPress`

**Description:** Test long press gesture recognition and context menu.

**Steps to Reproduce:**
1. Navigate to Samples List
2. Locate 'Long Press' option
3. Tap on 'Long Press'
4. Perform long press gesture on target element
5. Observe context menu or action result
6. Return to Samples List

**Expected Outcome:**
- Long Press screen displays press-responsive element
- Long press gesture triggers expected action
- Context menu appears (if applicable)
- Press duration is correctly detected

**Locators:**
```python
LONG_PRESS_BUTTON = (AppiumBy.XPATH, "//android.widget.TextView[@content-desc='longPress']")
```

**Automation Recommendations:**
- Create `LongPressPage` class
- Use `long_press_element()` method
- Test different press durations
- Verify action/menu appearance
- Implement test: `test_longPress_gesture`

---

### 7. Feature: Photo View

**Content Descriptor:** `photoView`

**Description:** Test image viewing and manipulation (zoom, pan).

**Steps to Reproduce:**
1. Navigate to Samples List
2. Locate 'Photo View' option
3. Tap on 'Photo View'
4. View displayed image
5. Perform zoom gestures (pinch to zoom)
6. Perform pan gestures
7. Return to Samples List

**Expected Outcome:**
- Photo View screen displays image
- Pinch-to-zoom gesture works correctly
- Pan gesture moves image within viewport
- Image quality maintains during transformations

**Locators:**
```python
PHOTO_VIEW_BUTTON = (AppiumBy.XPATH, "//android.widget.TextView[@content-desc='photoView']")
IMAGE_VIEW = (AppiumBy.CLASS_NAME, "android.widget.ImageView")
```

**Automation Recommendations:**
- Create `PhotoViewPage` class
- Test zoom in/out gestures
- Test pan in multiple directions
- Verify image bounds
- Implement test: `test_photoView_gestures`

---

### 8. Feature: Web View

**Content Descriptor:** `webView`

**Description:** Test WebView component and web content interaction.

**Steps to Reproduce:**
1. Navigate to Samples List
2. Locate 'Web View' option
3. Tap on 'Web View'
4. Wait for web content to load
5. Interact with web elements (if any)
6. Verify web content display
7. Return to Samples List

**Expected Outcome:**
- WebView screen loads successfully
- Web content is displayed correctly
- WebView is scrollable (if content exceeds viewport)
- Web elements are interactive
- No loading errors

**Locators:**
```python
WEB_VIEW_BUTTON = (AppiumBy.XPATH, "//android.widget.TextView[@content-desc='webView']")
WEB_VIEW_COMPONENT = (AppiumBy.CLASS_NAME, "android.webkit.WebView")
```

**Automation Recommendations:**
- Create `WebViewPage` class
- Switch context to WEBVIEW if needed
- Test web content loading
- Verify web element interactions
- Handle hybrid app contexts
- Implement test: `test_webView_content`

---

### 9. Feature: Carousel

**Content Descriptor:** `carousel`

**Description:** Test carousel/swipeable content navigation.

**Steps to Reproduce:**
1. Navigate to Samples List
2. Locate 'Carousel' option
3. Tap on 'Carousel'
4. Swipe through carousel items (left/right)
5. Verify carousel navigation
6. Check current item indicator
7. Return to Samples List

**Expected Outcome:**
- Carousel screen displays swipeable items
- Swipe left navigates to next item
- Swipe right navigates to previous item
- Current item indicator updates correctly
- Smooth transition animations

**Locators:**
```python
CAROUSEL_BUTTON = (AppiumBy.XPATH, "//android.widget.TextView[@content-desc='carousel']")
```

**Automation Recommendations:**
- Create `CarouselPage` class
- Test horizontal swipe gestures
- Verify item count and navigation
- Test edge cases (first/last item)
- Implement test: `test_carousel_navigation`

---

### 10. Feature: Wheel Picker

**Content Descriptor:** `wheelPicker`

**Description:** Test wheel picker/spinner selection functionality.

**Steps to Reproduce:**
1. Navigate to Samples List
2. Locate 'Wheel Picker' option
3. Tap on 'Wheel Picker'
4. Interact with wheel picker control
5. Select different values
6. Verify selected value
7. Return to Samples List

**Expected Outcome:**
- Wheel Picker screen displays picker control
- Picker responds to swipe gestures
- Selected value is highlighted
- Value can be read programmatically

**Locators:**
```python
WHEEL_PICKER_BUTTON = (AppiumBy.XPATH, "//android.widget.TextView[@content-desc='wheelPicker']")
```

**Automation Recommendations:**
- Create `WheelPickerPage` class
- Test value selection
- Verify picker scroll behavior
- Test boundary values
- Implement test: `test_wheelPicker_selection`

---

## Summary

**Total features to automate:** 10 sample features + 1 login flow = 11 test scenarios

**Test Coverage:**
- Authentication: 1 test
- Navigation: 10 tests
- Gestures: 7 tests (swipe, drag, tap, long press, zoom, pan)
- UI Components: 5 tests (slider, carousel, wheel picker, photo view, web view)

---

## Automation Implementation Plan

### Phase 1: Page Objects Creation
**Timeline:** 2-3 days

1. **Existing Pages (already implemented):**
   - ✅ `LoginPage` - `pages/vodqa/login_page.py`
   - ✅ `SamplesListPage` - `pages/vodqa/samples_list_page.py`
   - ✅ `HeaderBarComponent` - `pages/vodqa/header_bar_component.py`

2. **New Pages to Create:**
   - `NativeViewPage` - for chainedView testing
   - `SliderPage` - for slider1 testing
   - `VerticalSwipingPage` - for vertical swipe gestures
   - `DragAndDropPage` - for drag-drop functionality
   - `DoubleTapPage` - for double tap gestures
   - `LongPressPage` - for long press gestures
   - `PhotoViewPage` - for image manipulation
   - `WebViewPage` - for web content testing
   - `CarouselPage` - for carousel navigation
   - `WheelPickerPage` - for picker selection

3. **Page Object Structure:**
   - Each page should inherit from `BasePage` and `BaseAppiumGestures`
   - Use `@dataclass(frozen=True)` for locators
   - Implement `wait_until_page_is_loaded()` method
   - Add `@allure.step()` decorators for all public methods
   - Follow naming convention: `{FeatureName}Page` and `{FeatureName}PageLocators`

### Phase 2: Test Implementation
**Timeline:** 3-4 days

1. **Test Structure:**
   - Create test files in `tests/vodqa/` directory
   - Naming convention: `test_{feature_name}.py`
   - Group related tests in classes: `class TestFeatureName`
   - Use pytest fixtures from `conftest.py`

2. **Test Decorators:**
   - `@allure.feature("VodQA Samples")` - at class level
   - `@allure.story("{Feature Name}")` - at method level
   - `@allure.severity(allure.severity_level.NORMAL)` - at method level
   - `@allure.title("Test {feature} functionality")` - descriptive titles

3. **Test Data:**
   - Use existing `data/users.json` for login credentials
   - Create additional test data files if needed for parameterization

4. **Priority Testlist:**

| Priority | Feature | Test File | Complexity | Dependencies |
|----------|---------|-----------|------------|--------------|
| P0 | Login | `test_login.py` | Low | None |
| P1 | Samples List Navigation | `test_samples_list.py` | Low | Login |
| P2 | Native View | `test_native_view.py` | Low | Login |
| P3 | Slider | `test_slider.py` | Medium | Login, Gestures |
| P3 | Vertical Swiping | `test_vertical_swiping.py` | Medium | Login, Gestures |
| P4 | Drag and Drop | `test_drag_and_drop.py` | High | Login, Gestures |
| P4 | Double Tap | `test_double_tap.py` | Medium | Login, Gestures |
| P4 | Long Press | `test_long_press.py` | Medium | Login, Gestures |
| P5 | Photo View | `test_photo_view.py` | High | Login, Gestures |
| P5 | Web View | `test_web_view.py` | High | Login, Context Switch |
| P5 | Carousel | `test_carousel.py` | Medium | Login, Gestures |
| P5 | Wheel Picker | `test_wheel_picker.py` | Medium | Login |

### Phase 3: CI/CD Integration
**Timeline:** 1-2 days

1. Update pytest configuration
2. Configure Allure reporting
3. Add screenshot capture on failures
4. Setup test execution pipeline
5. Configure parallel execution (if needed)

### Phase 4: Documentation and Maintenance
**Timeline:** Ongoing

1. Document test scenarios
2. Update README with test execution instructions
3. Maintain test data
4. Review and refactor tests regularly

---

## Testing Best Practices

1. **Wait Strategies:**
   - Use explicit waits from `BasePage.wait_for_element()`
   - Import timeouts from `config.config_vars`
   - Avoid `time.sleep()`, use conditional waits

2. **Error Handling:**
   - Implement proper exception handling
   - Add meaningful assertion messages
   - Capture screenshots on test failures

3. **Test Independence:**
   - Each test should be independent
   - Use fixtures for setup/teardown
   - Reset app state between tests if needed

4. **Code Quality:**
   - Follow PEP 8 style guide
   - Use type hints
   - Keep methods focused and small
   - DRY principle - avoid code duplication

5. **Reporting:**
   - Use Allure for rich test reports
   - Add steps for better traceability
   - Attach screenshots for visual verification

---

## Known Issues and Considerations

1. **Appium Server:** Ensure Appium server is running before test execution
2. **Device Connection:** Verify device is connected and authorized for debugging
3. **App State:** Application should be installed and accessible
4. **Capabilities:** Use correct `platformVersion` and `deviceName` from `.env` file
5. **Gesture Timing:** Some gestures may require timing adjustments based on device performance

---

**Document Version:** 1.0  
**Last Updated:** 2025-12-11  
**Status:** Ready for Implementation

