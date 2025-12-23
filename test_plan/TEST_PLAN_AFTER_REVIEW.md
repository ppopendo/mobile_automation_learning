# VodQA Mobile App - Test Plan (After Review)

## Application Information

| Property | Value |
|----------|-------|
| Application | VodQA.apk |
| Package | com.vodqareactnative |
| Platform | Android |
| Automation | UiAutomator2 + Appium |

---

## Test Scenarios

### TC-00: Application Login

| Property | Value |
|----------|-------|
| **ID** | TC-00 |
| **Name** | User login to VodQA application |
| **Priority** | P0 - Critical |
| **Category** | Authentication |
| **Tags** | `@smoke`, `@regression`, `@login` |
| **Preconditions** | Application installed, device connected |
| **Postconditions** | User on Samples List screen |

**Locators:**

| Element | Strategy | Value |
|---------|----------|-------|
| Username field | ACCESSIBILITY_ID | `username` |
| Password field | ACCESSIBILITY_ID | `password` |
| Login button | ACCESSIBILITY_ID | `loginBtn` |
| Samples List header | XPATH | `//android.widget.TextView[@text='Samples List']` |

**Test Data:**

| Input Field | Value | Expected Result |
|-------------|-------|-----------------|
| Username | `admin` | Field accepts input |
| Password | `admin` | Field accepts input (masked) |

**Steps:**
1. Launch VodQA application
2. Wait for login page to load (verify username field visible)
3. Enter username: `admin`
4. Enter password: `admin`
5. Click 'LOG IN' button
6. Assert: "Samples List" header is displayed

**Expected Result:**
- User is successfully logged in
- "Samples List" page header text equals "Samples List"
- Login page is no longer visible

---

### TC-00a: Login with Invalid Credentials

| Property | Value |
|----------|-------|
| **ID** | TC-00a |
| **Name** | Login attempt with wrong password |
| **Priority** | P1 - High |
| **Category** | Authentication |
| **Tags** | `@regression`, `@negative`, `@login` |
| **Preconditions** | Application installed, device connected |
| **Postconditions** | User remains on login screen |

**Locators:**

| Element | Strategy | Value |
|---------|----------|-------|
| Error message | ACCESSIBILITY_ID | `errorMessage` |

**Test Data:**

| Input Field | Value | Expected Result |
|-------------|-------|-----------------|
| Username | `admin` | Field accepts input |
| Password | `wrongpassword` | Field accepts input |

**Steps:**
1. Launch VodQA application
2. Enter username: `admin`
3. Enter password: `wrongpassword`
4. Click 'LOG IN' button
5. Assert: Error message is displayed

**Expected Result:**
- Login fails
- Error message is visible
- User remains on login page

---

### TC-00b: Login with Empty Fields

| Property | Value |
|----------|-------|
| **ID** | TC-00b |
| **Name** | Login attempt with empty credentials |
| **Priority** | P2 - High |
| **Category** | Authentication |
| **Tags** | `@regression`, `@negative`, `@login` |
| **Preconditions** | Application installed, device connected |
| **Postconditions** | User remains on login screen |

**Steps:**
1. Launch VodQA application
2. Leave username field empty
3. Leave password field empty
4. Click 'LOG IN' button
5. Assert: Validation error is displayed

**Expected Result:**
- Login button is disabled OR validation error appears
- User remains on login page

---

### TC-01: Native View (Chained View)

| Property | Value |
|----------|-------|
| **ID** | TC-01 |
| **Name** | Native view navigation |
| **Priority** | P2 - High |
| **Category** | Navigation |
| **Tags** | `@regression`, `@navigation` |
| **Content Descriptor** | `chainedView` |
| **Preconditions** | User logged in, on Samples List |
| **Postconditions** | User returned to Samples List |

**Locators:**

| Element | Strategy | Value |
|---------|----------|-------|
| Native View option | ACCESSIBILITY_ID | `chainedView` |
| Back button | ACCESSIBILITY_ID | `back` |
| Screen title | XPATH | `//android.widget.TextView[@text='Native View']` |

**Steps:**
1. On Samples List find 'Native View' option (accessibility id: `chainedView`)
2. Click on 'Native View'
3. Assert: Screen title equals "Native View"
4. Verify UI elements are visible
5. Click 'Back' button
6. Assert: Samples List is displayed

**Expected Result:**
- Native View screen opens correctly
- Screen title text equals "Native View"
- Back navigation returns to Samples List

---

### TC-02: Slider

| Property | Value |
|----------|-------|
| **ID** | TC-02 |
| **Name** | Slider interaction |
| **Priority** | P3 - Medium |
| **Category** | Gesture |
| **Tags** | `@regression`, `@gesture`, `@slider` |
| **Content Descriptor** | `slider1` |
| **Preconditions** | User logged in, on Samples List |
| **Postconditions** | User returned to Samples List |

**Locators:**

| Element | Strategy | Value |
|---------|----------|-------|
| Slider option | ACCESSIBILITY_ID | `slider1` |
| Slider element | CLASS_NAME | `android.widget.SeekBar` |
| Slider value display | ACCESSIBILITY_ID | `sliderValue` |
| Back button | ACCESSIBILITY_ID | `back` |

**Test Data:**

| Slider Position | Expected Value |
|-----------------|----------------|
| 0% (left edge) | 0 |
| 50% (center) | 50 |
| 100% (right edge) | 100 |

**Steps:**
1. On Samples List click on 'Slider' option
2. Get initial slider value
3. Drag slider to 0% position
4. Assert: Slider value equals 0
5. Drag slider to 50% position
6. Assert: Slider value equals 50
7. Drag slider to 100% position
8. Assert: Slider value equals 100
9. Click 'Back' button

**Expected Result:**
- Slider responds to drag gestures
- Slider value at 0% = 0
- Slider value at 50% = 50
- Slider value at 100% = 100

---

### TC-03: Vertical Swiping

| Property | Value |
|----------|-------|
| **ID** | TC-03 |
| **Name** | Vertical scrolling |
| **Priority** | P3 - Medium |
| **Category** | Gesture |
| **Tags** | `@regression`, `@gesture`, `@swipe` |
| **Content Descriptor** | `verticalSwiping` |
| **Preconditions** | User logged in, on Samples List |
| **Postconditions** | User returned to Samples List |

**Locators:**

| Element | Strategy | Value |
|---------|----------|-------|
| Vertical Swiping option | ACCESSIBILITY_ID | `verticalSwiping` |
| Scrollable content | CLASS_NAME | `android.widget.ScrollView` |
| First item | XPATH | `(//android.widget.TextView)[1]` |
| Last item | XPATH | `(//android.widget.TextView)[last()]` |
| Back button | ACCESSIBILITY_ID | `back` |

**Steps:**
1. On Samples List click on 'Vertical Swiping' option
2. Get initial visible content position
3. Perform swipe up gesture (scroll down)
4. Assert: Content position changed (new elements visible)
5. Perform swipe down gesture (scroll up)
6. Assert: Original content visible again
7. Click 'Back' button

**Expected Result:**
- Swipe up reveals content below
- Swipe down reveals content above
- Gestures are smooth and responsive

---

### TC-04: Drag and Drop

| Property | Value |
|----------|-------|
| **ID** | TC-04 |
| **Name** | Drag and drop functionality |
| **Priority** | P4 - Low |
| **Category** | Gesture |
| **Tags** | `@regression`, `@gesture`, `@dragdrop` |
| **Content Descriptor** | `dragAndDrop` |
| **Preconditions** | User logged in, on Samples List |
| **Postconditions** | User returned to Samples List |

**Locators:**

| Element | Strategy | Value |
|---------|----------|-------|
| Drag and Drop option | ACCESSIBILITY_ID | `dragAndDrop` |
| Draggable element | ACCESSIBILITY_ID | `dragMe` |
| Drop zone | ACCESSIBILITY_ID | `dropZone` |
| Success message | ACCESSIBILITY_ID | `successMessage` |
| Back button | ACCESSIBILITY_ID | `back` |

**Steps:**
1. On Samples List click on 'Drag and Drop' option
2. Identify draggable element (accessibility id: `dragMe`)
3. Get draggable element initial coordinates (x1, y1)
4. Get drop zone coordinates (x2, y2)
5. Perform drag from (x1, y1) to (x2, y2)
6. Assert: Success message is displayed OR element position changed
7. Click 'Back' button

**Expected Result:**
- Element can be dragged
- Drop zone accepts the element
- Visual/text confirmation of successful drop

---

### TC-04a: Drag and Drop - Invalid Drop Zone

| Property | Value |
|----------|-------|
| **ID** | TC-04a |
| **Name** | Drag to invalid area |
| **Priority** | P5 - Lowest |
| **Category** | Gesture |
| **Tags** | `@regression`, `@negative`, `@dragdrop` |
| **Preconditions** | User logged in, on Drag and Drop screen |
| **Postconditions** | Element returns to original position |

**Steps:**
1. Navigate to Drag and Drop screen
2. Get draggable element initial position
3. Drag element to area outside drop zone
4. Release element
5. Assert: Element returns to original position

**Expected Result:**
- Element snaps back to original position
- No success message displayed

---

### TC-05: Double Tap

| Property | Value |
|----------|-------|
| **ID** | TC-05 |
| **Name** | Double tap gesture |
| **Priority** | P4 - Low |
| **Category** | Gesture |
| **Tags** | `@regression`, `@gesture`, `@doubletap` |
| **Content Descriptor** | `doubleTap` |
| **Preconditions** | User logged in, on Samples List |
| **Postconditions** | User returned to Samples List |

**Locators:**

| Element | Strategy | Value |
|---------|----------|-------|
| Double Tap option | ACCESSIBILITY_ID | `doubleTap` |
| Tap target | ACCESSIBILITY_ID | `doubleTapMe` |
| Result message | ACCESSIBILITY_ID | `tapResult` |
| Back button | ACCESSIBILITY_ID | `back` |

**Test Data:**

| Action | Expected Result Text |
|--------|---------------------|
| Single tap | No change / "Tap once more" |
| Double tap | "Double tap successful" |

**Steps:**
1. On Samples List click on 'Double Tap' option
2. Perform single tap on target element
3. Assert: Double tap action NOT triggered
4. Perform double tap on target element
5. Assert: Result message contains "Double tap" or success indicator
6. Click 'Back' button

**Expected Result:**
- Single tap does not trigger double tap action
- Double tap is recognized and triggers expected action
- Visual/text confirmation displayed

---

### TC-06: Long Press

| Property | Value |
|----------|-------|
| **ID** | TC-06 |
| **Name** | Long press gesture |
| **Priority** | P4 - Low |
| **Category** | Gesture |
| **Tags** | `@regression`, `@gesture`, `@longpress` |
| **Content Descriptor** | `longPress` |
| **Preconditions** | User logged in, on Samples List |
| **Postconditions** | User returned to Samples List |

**Locators:**

| Element | Strategy | Value |
|---------|----------|-------|
| Long Press option | ACCESSIBILITY_ID | `longPress` |
| Press target | ACCESSIBILITY_ID | `longPressMe` |
| Context menu / Result | ACCESSIBILITY_ID | `longPressResult` |
| Back button | ACCESSIBILITY_ID | `back` |

**Test Data:**

| Press Duration | Expected Result |
|----------------|-----------------|
| < 500ms | No action |
| >= 1000ms | Long press triggered |

**Steps:**
1. On Samples List click on 'Long Press' option
2. Perform short tap on target element
3. Assert: Long press action NOT triggered
4. Perform long press (hold for 1+ seconds) on target element
5. Assert: Context menu appears OR result message displayed
6. Click 'Back' button

**Expected Result:**
- Short tap does not trigger long press
- Long press (1+ sec) triggers action
- Visual confirmation displayed

---

### TC-07: Photo View

| Property | Value |
|----------|-------|
| **ID** | TC-07 |
| **Name** | Photo viewing and manipulation |
| **Priority** | P5 - Lowest |
| **Category** | UI Component |
| **Tags** | `@regression`, `@gesture`, `@photoview` |
| **Content Descriptor** | `photoView` |
| **Preconditions** | User logged in, on Samples List |
| **Postconditions** | User returned to Samples List |

**Locators:**

| Element | Strategy | Value |
|---------|----------|-------|
| Photo View option | ACCESSIBILITY_ID | `photoView` |
| Image element | CLASS_NAME | `android.widget.ImageView` |
| Back button | ACCESSIBILITY_ID | `back` |

**Steps:**
1. On Samples List click on 'Photo View' option
2. Assert: Image is displayed
3. Get initial image bounds
4. Perform pinch-out gesture (zoom in)
5. Assert: Image bounds increased (zoomed in)
6. Perform pinch-in gesture (zoom out)
7. Assert: Image returns to original size
8. Perform pan gesture (drag image)
9. Assert: Image position changed
10. Click 'Back' button

**Expected Result:**
- Image displays correctly
- Pinch-out zooms in
- Pinch-in zooms out
- Pan moves the image
- Image quality maintained

---

### TC-08: Web View

| Property | Value |
|----------|-------|
| **ID** | TC-08 |
| **Name** | Web content display |
| **Priority** | P5 - Lowest |
| **Category** | UI Component |
| **Tags** | `@regression`, `@webview` |
| **Content Descriptor** | `webView` |
| **Preconditions** | User logged in, on Samples List, internet connection |
| **Postconditions** | User returned to Samples List |

**Locators:**

| Element | Strategy | Value |
|---------|----------|-------|
| Web View option | ACCESSIBILITY_ID | `webView` |
| WebView container | CLASS_NAME | `android.webkit.WebView` |
| Back button | ACCESSIBILITY_ID | `back` |

**Steps:**
1. On Samples List click on 'Web View' option
2. Wait for WebView to load (max 10 seconds)
3. Assert: WebView element is present
4. Assert: No error message displayed
5. Switch to WEBVIEW context (if needed)
6. Verify web content is rendered
7. Switch back to NATIVE_APP context
8. Click 'Back' button

**Expected Result:**
- WebView loads within timeout
- Web content is visible
- No "page not found" or error messages
- Context switching works correctly

---

### TC-09: Carousel

| Property | Value |
|----------|-------|
| **ID** | TC-09 |
| **Name** | Carousel navigation |
| **Priority** | P5 - Lowest |
| **Category** | UI Component |
| **Tags** | `@regression`, `@gesture`, `@carousel` |
| **Content Descriptor** | `carousel` |
| **Preconditions** | User logged in, on Samples List |
| **Postconditions** | User returned to Samples List |

**Locators:**

| Element | Strategy | Value |
|---------|----------|-------|
| Carousel option | ACCESSIBILITY_ID | `carousel` |
| Carousel container | ACCESSIBILITY_ID | `carouselContainer` |
| Current item | ACCESSIBILITY_ID | `currentItem` |
| Page indicator | ACCESSIBILITY_ID | `pageIndicator` |
| Back button | ACCESSIBILITY_ID | `back` |

**Test Data:**

| Action | Expected Page |
|--------|---------------|
| Initial state | Page 1 |
| Swipe left | Page 2 |
| Swipe left | Page 3 |
| Swipe right | Page 2 |

**Steps:**
1. On Samples List click on 'Carousel' option
2. Assert: Initial page/item is displayed (page 1)
3. Get current item identifier
4. Swipe left
5. Assert: Next item displayed, indicator updated
6. Swipe left again
7. Assert: Third item displayed
8. Swipe right
9. Assert: Previous item displayed
10. Click 'Back' button

**Expected Result:**
- Left swipe advances to next item
- Right swipe returns to previous item
- Page indicator reflects current position
- Animations are smooth

---

### TC-10: Wheel Picker

| Property | Value |
|----------|-------|
| **ID** | TC-10 |
| **Name** | Wheel picker value selection |
| **Priority** | P5 - Lowest |
| **Category** | UI Component |
| **Tags** | `@regression`, `@gesture`, `@picker` |
| **Content Descriptor** | `wheelPicker` |
| **Preconditions** | User logged in, on Samples List |
| **Postconditions** | User returned to Samples List |

**Locators:**

| Element | Strategy | Value |
|---------|----------|-------|
| Wheel Picker option | ACCESSIBILITY_ID | `wheelPicker` |
| Picker element | CLASS_NAME | `android.widget.NumberPicker` |
| Selected value | ACCESSIBILITY_ID | `selectedValue` |
| Back button | ACCESSIBILITY_ID | `back` |

**Test Data:**

| Scroll Direction | Expected Change |
|------------------|-----------------|
| Scroll up | Next value |
| Scroll down | Previous value |

**Steps:**
1. On Samples List click on 'Wheel Picker' option
2. Get initial selected value
3. Scroll wheel picker up
4. Assert: Selected value changed to next option
5. Get new selected value
6. Scroll wheel picker down
7. Assert: Selected value returned to previous option
8. Click 'Back' button

**Expected Result:**
- Wheel picker responds to scroll gestures
- Selected value updates on scroll
- Value is highlighted/centered when selected

---

## Summary

| Category | Test Count |
|----------|------------|
| Authentication | 3 |
| Navigation | 1 |
| Gesture | 8 |
| UI Component | 4 |
| **Total** | **16** |

### Test Distribution by Priority

| Priority | Description | Count |
|----------|-------------|-------|
| P0 | Critical | 1 |
| P1 | High | 1 |
| P2 | High | 2 |
| P3 | Medium | 2 |
| P4 | Low | 4 |
| P5 | Lowest | 6 |

### Test Distribution by Type

| Type | Count |
|------|-------|
| Positive (Happy Path) | 13 |
| Negative | 3 |

### Tags Reference

| Tag | Description | Count |
|-----|-------------|-------|
| `@smoke` | Quick sanity tests | 1 |
| `@regression` | Full regression suite | 16 |
| `@login` | Login-related tests | 3 |
| `@gesture` | Gesture-based tests | 9 |
| `@navigation` | Navigation tests | 1 |
| `@negative` | Negative test cases | 3 |

---

## Appendix: Locator Strategy Guide

| Strategy | When to Use | Example |
|----------|-------------|---------|
| ACCESSIBILITY_ID | Preferred - stable, semantic | `loginBtn` |
| ID | Android resource ID | `com.vodqareactnative:id/button` |
| XPATH | Last resort - fragile | `//android.widget.TextView[@text='Login']` |
| CLASS_NAME | Generic element type | `android.widget.Button` |

---

**Document Version:** 2.0  
**Last Updated:** 2025-12-11  
**Reviewed By:** Test Architect  
**Status:** Ready for Implementation  
**Changes from v1.0:**
- Added locators for all test cases
- Added test data sections
- Added negative test scenarios (TC-00a, TC-00b, TC-04a)
- Added tags for filtering
- Added postconditions
- Fixed summary counts
- Added appendix with locator strategy guide

