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
| **1. Native View** | ✅ **Automated** | **2** | ✅ `NativeViewDemoPage` | TC-21-01, TC-21-02 complete |
| **2. Slider** | ✅ **Automated** | **5** | ✅ `SliderPage` | TC-02-01, TC-02-02, TC-02-03 complete |
| **3. Vertical Swiping** | ✅ **Automated** | **5** | ✅ `VerticalSwipingPage` | TC-03-01 to TC-03-04 complete |
| **4. Drag and Drop** | ✅ **Automated** | **6** | ✅ `DragAndDropPage` | TC-04-01 to TC-04-04 complete |
| **5. Double Tap** | ✅ **Automated** | **2** | ✅ `DoubleTapPage` | TC-05-01, TC-05-02 complete |
| **6. Long Press** | ✅ **Automated** | **2** | ✅ `LongPressPage` | TC-06-01, TC-06-02 complete |
| **7. Photo View** | ✅ **Automated** | **9** | ✅ `PhotoViewPage` | TC-09-01 to TC-09-09 complete (Pinch gestures with validation) |
| **8. Web View** | ✅ **Automated** | **5** | ✅ `WebViewPage` | TC-22-01 to TC-22-05 complete |
| **9. Carousel** | ✅ **Automated** | **4** | ✅ `CarouselPage` | TC-10-01 to TC-10-04 complete (Horizontal fling with ID validation) |
| **10. Wheel Picker** | ✅ **Automated** | **5** | ✅ `WheelPickerDemoPage` | TC-20-01, TC-20-02 (parametrized) complete |
| **11. Swipe Gestures** | ✅ **Automated** | **6** | ✅ `SliderPage` | TC-07-01, TC-07-02, TC-07-04, TC-07-05 complete |
| **12. Fling & Scroll Gestures** | ✅ **Automated** | **9** | ✅ `VerticalSwipingPage` | TC-08-01 to TC-08-09 complete (W3C gestures, vertical) |

**Total Automated Tests:** 53  
**Last Updated:** 2026-01-18

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

**Automation Status:** ✅ **AUTOMATED**

| Test Case | Status | Test File | Notes |
|-----------|--------|-----------|-------|
| TC-21-01: Page has required elements | ✅ Automated | `tests/vodqa/test_native_view_demo.py` | Verifies container texts |
| TC-21-02: Containers display expected text | ✅ Automated | `tests/vodqa/test_native_view_demo.py` | Verifies specific text content |

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

**Page Object:** `NativeViewDemoPage` - `pages/vodqa/native_view_demo_page.py`

**Implemented Methods:**
- `container_text_1` (property)
- `container_text_2` (property)
- `container_text_3` (property)

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

**Automation Status:** ✅ **AUTOMATED**

| Test Case | Status | Test File | Notes |
|-----------|--------|-----------|-------|
| TC-03-01: Swipe up gesture | ✅ Automated | `tests/vodqa/test_vertical_swiping.py` | Verifies swipe up |
| TC-03-02: Swipe down gesture | ✅ Automated | `tests/vodqa/test_vertical_swiping.py` | Verifies swipe down |
| TC-03-03: Scroll element into view | ✅ Automated | `tests/vodqa/test_vertical_swiping.py` | Verifies scrolling to element |
| TC-03-04: Scroll with percentage | ✅ Automated | `tests/vodqa/test_vertical_swiping.py` | Parametrized (2 tests) |

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

**Page Object:** `VerticalSwipingPage` - `pages/vodqa/vertical_swiping_page.py`

**Implemented Methods:**
- `scroll_to_item(item_text, direction, max_scrolls)`
- `is_item_displayed(item_text)`

---

### 4. Feature: Drag and Drop

**Content Descriptor:** `dragAndDrop`

**Automation Status:** ✅ **AUTOMATED**

| Test Case | Status | Test File | Notes |
|-----------|--------|-----------|-------|
| TC-04-01: Page has drag button | ✅ Automated | `tests/vodqa/test_drag_and_drop.py` | Verifies drag button visibility |
| TC-04-02: Page has drop zone | ✅ Automated | `tests/vodqa/test_drag_and_drop.py` | Verifies drop zone visibility |
| TC-04-03: Drag and drop element | ✅ Automated | `tests/vodqa/test_drag_and_drop.py` | Verifies drag and drop action |
| TC-04-04: Drag with speed | ✅ Automated | `tests/vodqa/test_drag_and_drop.py` | Parametrized (3 tests) |

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

**Page Object:** `DragAndDropPage` - `pages/vodqa/drag_and_drop_page.py`

**Implemented Methods:**
- `drag_and_drop_element(speed)`
- `is_drag_me_button_displayed`
- `is_drop_here_zone_displayed`
- `message_dropped_text`

---

### 5. Feature: Double Tap

**Content Descriptor:** `doubleTap`

**Automation Status:** ✅ **AUTOMATED**

| Test Case | Status | Test File | Notes |
|-----------|--------|-----------|-------|
| TC-05-01: Page has elements | ✅ Automated | `tests/vodqa/test_double_tap.py` | Verifies button visibility |
| TC-05-02: Double tap on element | ✅ Automated | `tests/vodqa/test_double_tap.py` | Verifies double tap action |

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

**Page Object:** `DoubleTapPage` - `pages/vodqa/double_tap_page.py`

**Implemented Methods:**
- `double_tap_on_double_tap_me_button()`
- `is_double_tap_me_button_displayed`
- `is_double_tap_modal_displayed`

---

### 6. Feature: Long Press

**Content Descriptor:** `longPress`

**Automation Status:** ✅ **AUTOMATED**

| Test Case | Status | Test File | Notes |
|-----------|--------|-----------|-------|
| TC-06-01: Page has elements | ✅ Automated | `tests/vodqa/test_long_press.py` | Verifies header visibility |
| TC-06-02: Long press on element | ✅ Automated | `tests/vodqa/test_long_press.py` | Verifies long press action |

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

**Page Object:** `LongPressPage` - `pages/vodqa/long_press_page.py`

**Implemented Methods:**
- `long_press_on_long_press_button()`
- `is_long_press_header_displayed`
- `is_long_press_modal_displayed`

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

**Automation Status:** ✅ **AUTOMATED**

| Test Case | Status | Test File | Notes |
|-----------|--------|-----------|-------|
| TC-22-01: Page displays correct header | ✅ Automated | `tests/vodqa/test_web_view.py` | Verifies 'Hacker News' header |
| TC-22-02: 'More' button functionality | ✅ Automated | `tests/vodqa/test_web_view.py` | Verifies header after 'More' click |
| TC-22-03: Search functionality | ✅ Automated | `tests/vodqa/test_web_view.py` | Verifies search results for 'Bluescreen' |
| TC-22-04: Dropdown stories display | ✅ Automated | `tests/vodqa/test_web_view.py` | Verifies dropdown after entering search value |
| TC-22-05: WebView context diagnostic | ✅ Automated | `tests/vodqa/test_web_view.py` | Diagnostic test for WebView context troubleshooting |

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

**Page Object:** `WebViewPage` - `pages/vodqa/web_view_page.py`

**Implemented Methods:**
- `wait_until_page_is_loaded()`
- `is_header_displayed` (property)
- `is_news_title_displayed(title)`
- `tap_more_link_button()`
- `enter_search_value(search_value)`
- `submit_search()`
- `get_search_results_count(search_value)`


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

**Automation Status:** ✅ **AUTOMATED**

| Test Case | Status | Test File | Notes |
|-----------|--------|-----------|-------|
| TC-20-01: Page has required elements | ✅ Automated | `tests/vodqa/test_wheel_picker_demo.py` | Verifies color text and box |
| TC-20-02: Select color from dropdown | ✅ Automated | `tests/vodqa/test_wheel_picker_demo.py` | Parametrized (4 colors) |

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

**Page Object:** `WheelPickerDemoPage` - `pages/vodqa/wheel_picker_demo_page.py`

**Implemented Methods:**
- `select_color(color)`
- `capture_color_box_screenshot()`
- `current_color_text` (property)
- `color_dropdown_value` (property)

### 11. Feature: Swipe Gestures

**Automation Status:** ✅ **AUTOMATED**

| Test Case | Status | Test File | Notes |
|-----------|--------|-----------|-------|
| TC-07-01: Swipe left gesture | ✅ Automated | `tests/vodqa/test_swipe_gestures.py` | Verifies swipe left |
| TC-07-02: Swipe right gesture | ✅ Automated | `tests/vodqa/test_swipe_gestures.py` | Verifies swipe right |
| TC-07-04: Swipe with percentage | ✅ Automated | `tests/vodqa/test_swipe_gestures.py` | Parametrized (2 tests) |
| TC-07-05: Swipe with speed | ✅ Automated | `tests/vodqa/test_swipe_gestures.py` | Parametrized (2 tests) |

**Description:** Test horizontal swipe gestures using the Slider page.

**Steps to Reproduce:**
1. Navigate to Samples List
2. Locate 'Slider' option
3. Tap on 'Slider'
4. Perform horizontal swipe gestures (left and right)
5. Verify swipe behavior

**Expected Outcome:**
- Swipe gestures are recognized
- Elements respond to swipe gestures

**Page Object:** `SliderPage` - `pages/vodqa/slider_page.py`

**Implemented Methods:**
- `swipe_left_slider_1()`
- `swipe_right_slider_2()`
- `swipe_left_slider_2(percentage)`
- `swipe_right_slider_1(speed)`

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
6. **W3C Gesture Commands:** Fling, scroll, and pinch gestures use the appium-gestures-plugin which must be installed and enabled on the Appium server

---

## Recent Updates

### 2025-12-28: Enhanced Carousel Tests with ID Validation
- Simplified CarouselPage locators to use content-desc and text-based XPaths
  - `CAROUSEL_ITEM`: `//*[@content-desc]` for carousel items
  - `CAROUSEL_ID`: `//*[contains(@text," / ")]` for carousel ID indicator
- Renamed method to `fling_on_carousel_item()` for clarity
- Added `carousel_id` property to retrieve current carousel position
- Enhanced tests to validate carousel ID changes after fling gestures
- Added TC-10-01 test that specifically validates carousel ID is one of "1 / 3", "2 / 3", "3 / 3"
- Updated TC-10-02, TC-10-03 to verify carousel ID after fling operations
- Total test count: 45 → 46 tests

### 2025-12-28: Refinement of Page Objects and Test Consolidation
- Updated CarouselPage locators to use dynamic XPath for carousel indicators and views
- Consolidated carousel fling methods into single `fling_on_carousel(direction, speed)` method
- Updated PhotoViewPage title to "Photos - Pinch & Zoom" and simplified image locator
- Added `photo_image_size` property to PhotoViewPage for validation
- Added TC-09-08 test to verify image enlargement after pinch gesture
- Consolidated horizontal fling tests from 6 to 3 using pytest parametrize
- Total test count adjusted: 50 → 45 tests (through consolidation)

### 2025-12-27: W3C Gesture Methods and New Page Objects
- Added comprehensive parameter validation for all gesture methods (percentage 0.0-1.0, speed > 0)
- Implemented new W3C gesture commands: `fling_element`, `scroll_element`, `pinch_open`, `pinch_close`
- Created PhotoViewPage for pinch gesture testing (zoom in/out functionality)
- Created CarouselPage for horizontal fling gesture testing
- Added 21 new test cases:
  - 9 for vertical fling/scroll gestures (consolidated validation tests)
  - 8 for pinch gestures on Photo View
  - 4 for horizontal fling gestures on Carousel
- Refactored duplicate code using `_validate_gesture_result()` helper method
- Updated documentation to clarify behavior changes and method distinctions
- Consolidated parameter validation tests using pytest parametrize

### 2026-01-04: Native View and Wheel Picker Automation
- Implemented `NativeViewDemoPage` and `WheelPickerDemoPage`
- Added tests for Native View (TC-21-01, TC-21-02)
- Added tests for Wheel Picker (TC-20-01, TC-20-02)
- Updated automation coverage summary
- Total automated tests increased to 48

### 2026-01-10: Web View Automation
- Implemented `WebViewPage` with interactions for Web View elements
- Added tests for Web View (TC-22-01, TC-22-02, TC-22-03, TC-22-04, TC-22-05)
- Validated header display, 'More' button, search functionality, dropdown stories, and diagnostic test
- Total automated tests increased to 53

---

**Document Version:** 1.4
**Last Updated:** 2026-01-10  
**Status:** In Progress

