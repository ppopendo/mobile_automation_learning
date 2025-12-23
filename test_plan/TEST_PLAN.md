# VodQA Mobile App - Test Plan

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

| ID | TC-00 |
|----|-------|
| **Name** | User login to VodQA application |
| **Priority** | P0 - Critical |
| **Preconditions** | Application installed, device connected |

**Steps:**
1. Launch VodQA application
2. Wait for login page to load
3. Enter username: `admin`
4. Enter password: `admin`
5. Click 'LOG IN' button

**Expected Result:**
- User is successfully logged in
- "Samples List" page is displayed

---

### TC-01: Native View (Chained View)

| ID | TC-01 |
|----|-------|
| **Name** | Native view navigation |
| **Priority** | P2 |
| **Content Descriptor** | `chainedView` |
| **Preconditions** | User logged in |

**Steps:**
1. On Samples List find 'Native View' option
2. Click on 'Native View'
3. Verify elements on screen
4. Click 'Back' button

**Expected Result:**
- Native View screen opens correctly
- UI elements are visible
- Back navigation to Samples List works properly

---

### TC-02: Slider

| ID | TC-02 |
|----|-------|
| **Name** | Slider interaction |
| **Priority** | P3 |
| **Content Descriptor** | `slider1` |
| **Preconditions** | User logged in |

**Steps:**
1. On Samples List find 'Slider' option
2. Click on 'Slider'
3. Drag slider to different positions (0%, 50%, 100%)
4. Verify value change
5. Click 'Back' button

**Expected Result:**
- Slider responds to drag gestures
- Slider value changes correctly
- Back navigation works properly

---

### TC-03: Vertical Swiping

| ID | TC-03 |
|----|-------|
| **Name** | Vertical scrolling |
| **Priority** | P3 |
| **Content Descriptor** | `verticalSwiping` |
| **Preconditions** | User logged in |

**Steps:**
1. On Samples List find 'Vertical Swiping' option
2. Click on 'Vertical Swiping'
3. Perform swipe up gesture
4. Perform swipe down gesture
5. Click 'Back' button

**Expected Result:**
- Content scrolls smoothly up and down
- Swipe gestures are recognized correctly

---

### TC-04: Drag and Drop

| ID | TC-04 |
|----|-------|
| **Name** | Drag and drop functionality |
| **Priority** | P4 |
| **Content Descriptor** | `dragAndDrop` |
| **Preconditions** | User logged in |

**Steps:**
1. On Samples List find 'Drag and Drop' option
2. Click on 'Drag and Drop'
3. Identify draggable elements
4. Drag element to drop zone
5. Verify new element position
6. Click 'Back' button

**Expected Result:**
- Elements can be dragged
- Drop zone accepts elements
- Visual confirmation of operation

---

### TC-05: Double Tap

| ID | TC-05 |
|----|-------|
| **Name** | Double tap gesture |
| **Priority** | P4 |
| **Content Descriptor** | `doubleTap` |
| **Preconditions** | User logged in |

**Steps:**
1. On Samples List find 'Double Tap' option
2. Click on 'Double Tap'
3. Perform double tap gesture on target element
4. Verify gesture response
5. Click 'Back' button

**Expected Result:**
- Double tap gesture is recognized
- Expected action is executed
- Single tap does not trigger double tap action

---

### TC-06: Long Press

| ID | TC-06 |
|----|-------|
| **Name** | Long press gesture |
| **Priority** | P4 |
| **Content Descriptor** | `longPress` |
| **Preconditions** | User logged in |

**Steps:**
1. On Samples List find 'Long Press' option
2. Click on 'Long Press'
3. Perform long press gesture on element
4. Verify context menu or response
5. Click 'Back' button

**Expected Result:**
- Long press gesture triggers action
- Context menu appears (if applicable)
- Press duration is correctly detected

---

### TC-07: Photo View

| ID | TC-07 |
|----|-------|
| **Name** | Photo viewing and manipulation |
| **Priority** | P5 |
| **Content Descriptor** | `photoView` |
| **Preconditions** | User logged in |

**Steps:**
1. On Samples List find 'Photo View' option
2. Click on 'Photo View'
3. Perform pinch to zoom gesture
4. Perform pan gesture
5. Click 'Back' button

**Expected Result:**
- Image displays correctly
- Zoom gesture works
- Pan gesture works
- Image quality maintained during transformation

---

### TC-08: Web View

| ID | TC-08 |
|----|-------|
| **Name** | Web content display |
| **Priority** | P5 |
| **Content Descriptor** | `webView` |
| **Preconditions** | User logged in |

**Steps:**
1. On Samples List find 'Web View' option
2. Click on 'Web View'
3. Wait for web content to load
4. Verify content display
5. Interact with web elements (if available)
6. Click 'Back' button

**Expected Result:**
- WebView loads correctly
- Web content is displayed
- No loading errors
- Web elements are interactive

---

### TC-09: Carousel

| ID | TC-09 |
|----|-------|
| **Name** | Carousel navigation |
| **Priority** | P5 |
| **Content Descriptor** | `carousel` |
| **Preconditions** | User logged in |

**Steps:**
1. On Samples List find 'Carousel' option
2. Click on 'Carousel'
3. Swipe left (next element)
4. Swipe right (previous element)
5. Verify current element indicator
6. Click 'Back' button

**Expected Result:**
- Carousel displays scrollable elements
- Left swipe shows next element
- Right swipe shows previous element
- Smooth transition animations

---

### TC-10: Wheel Picker

| ID | TC-10 |
|----|-------|
| **Name** | Wheel picker value selection |
| **Priority** | P5 |
| **Content Descriptor** | `wheelPicker` |
| **Preconditions** | User logged in |

**Steps:**
1. On Samples List find 'Wheel Picker' option
2. Click on 'Wheel Picker'
3. Scroll wheel picker to select different values
4. Verify selected value
5. Click 'Back' button

**Expected Result:**
- Wheel picker responds to scroll gestures
- Selected value is highlighted
- Value can be read programmatically

---

## Summary

| Category | Test Count |
|----------|------------|
| Authentication | 1 |
| Navigation | 10 |
| Gestures | 7 |
| UI Components | 5 |
| **Total** | **11** |

### Priorities

| Priority | Description | Count |
|----------|-------------|-------|
| P0 | Critical | 1 |
| P2 | High | 1 |
| P3 | Medium | 2 |
| P4 | Low | 3 |
| P5 | Lowest | 4 |

---

**Document Version:** 1.0  
**Last Updated:** 2025-12-11  
**Status:** Ready for Implementation

