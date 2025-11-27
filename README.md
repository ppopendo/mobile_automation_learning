# Mobile Automation Testing - Learning Repository
##
Draft version.

This repository is dedicated to learning and experimenting with mobile automation testing.

It contains various scripts, configurations, and resources to help understand the concepts and practices involved in automating tests for mobile applications.
## Table of Contents
- [Getting Started](#getting-started)
- [Prerequisites](#prerequisites)
- [Installation](#installation)
- [Resources](#resources)
- [Running Tests](#running-tests)
## Getting Started
To get started with mobile automation testing using this repository, follow the instructions below.
## Prerequisites
- Basic knowledge of mobile application development and testing.
- Familiarity with programming languages such as Java, Python, or JavaScript.
- Installed tools depending on your target platform: Android Studio (Android) or Xcode (iOS).
## Installation

Below are installation and verification steps to set up the test environment (instructions are primarily for Windows PowerShell; notes for macOS are provided where relevant).

1) Clone the repository

```powershell
git clone https://github.com/your-org/mobile_automation_learning.git
cd mobile_automation_learning
```

2) Python - create a virtual environment and install requirements

It is recommended to use a virtual environment to isolate project dependencies.

```powershell
python -m venv .venv
.\.venv\Scripts\Activate.ps1  # PowerShell
python -m pip install --upgrade pip
pip install -r requirements.txt
```

3) Appium (server) — install via npm

Appium requires Node.js (recommended: latest LTS). If you don't have Node.js, download it from https://nodejs.org/

```powershell
npm install -g appium
npm install -g appium-doctor
# check environment (Android/iOS)
appium-doctor --android --ios
# start Appium server (local)
appium
```

Note: iOS testing typically requires macOS with Xcode; Windows does not support iOS simulators.

4) Appium drivers (recommended)

Starting with Appium 2.x, drivers are distributed separately. Install drivers you plan to use:

```powershell
# Android (UIAutomator2)
appium driver install uiautomator2
# iOS (XCUITest) - requires macOS + Xcode
appium driver install xcuitest
```

5) adb / Android SDK installation (Android)

Option A — Android Studio (recommended):
- Download and install Android Studio: https://developer.android.com/studio
- In Android Studio -> SDK Manager install "Android SDK Platform-Tools" and the SDK platforms you need for emulators.
- Set environment variables on Windows (adjust paths to your installation):

```powershell
# Example - adjust path for your installation
setx ANDROID_HOME "C:\Users\<YourUser>\AppData\Local\Android\Sdk"
setx PATH "%PATH%;%ANDROID_HOME%\platform-tools"
# open a new terminal to pick up changes
```

Option B — standalone platform-tools (adb only):
- Download "Platform Tools" (adb) from: https://developer.android.com/studio/releases/platform-tools
- Extract and add the `platform-tools` folder to your PATH.

Verification:

```powershell
adb version
adb devices
```

6) USB drivers for physical devices (Windows)

- Android: install appropriate USB drivers from the device manufacturer (Samsung, Huawei, etc.) or the Google USB Driver where applicable. Enable Developer Options and USB debugging on the device.
- iOS: requires macOS — install Xcode and related tools; macOS handles device drivers via Xcode.

7) iOS (macOS only)

If you want to test on iOS you need a macOS machine:
- Install Xcode from the App Store.
- Open Xcode and accept the license.
- Install additional tools if needed (e.g., ios-deploy) to run tests on physical devices.
- Verify tools:

```bash
xcode-select --install
xcodebuild -version
```

8) Appium Inspector (GUI for element inspection)

Appium Inspector is available separately or via Appium Desktop (depending on release):

- Appium Inspector (newer standalone inspector): https://github.com/appium/appium-inspector/releases
- Appium Desktop (contains Inspector in some versions): https://github.com/appium/appium-desktop/releases

Windows instructions:
- Download the appropriate installer (.exe/.zip), extract and run.
- In Appium Inspector configure Desired Capabilities using `resources/desired_capabilities.json` from this repository.

9) Verify Appium and environment

```powershell
# versions
appium --version
node --version
npm --version
appium-doctor --android --ios
# check adb
adb devices
# run sample tests
pytest -q tests/
```

10) Troubleshooting (quick tips)
- If `appium-doctor` reports missing dependencies, install the missing components and re-run it.
- On Windows, if PATH changes are not visible, open a new terminal after updating environment variables.
- Make sure your emulator/device is running and visible to `adb devices`.

11) Download sample apps for testing
Sauce Labs - > https://github.com/saucelabs/my-demo-app-android/releases

12) Allure report
- Install Allure commandline (requires Java):
- download openJdk from https://adoptium.net/ or https://openjdk.org/
- install Allure from https://docs.qameta.io/allure/#_installing_a_commandline
- add environment variable ALLURE_HOME pointing to Allure installation folder
- generate test case with allure report:

```powershell
pytest  --alluredir=allure-results
```
- generate report from results:

```powershell
allure generate allure-results --clean -o reports
```
- open report in browser:

```powershell
allure open ./reports/
```

## Resources
- [Appium Documentation](https://appium.io/docs/en/about-appium/intro/)
- [Android Developer Guide](https://developer.android.com/guide)
- [iOS Developer Documentation](https://developer.apple.com/documentation/)
- [Selenium WebDriver](https://www.selenium.dev/documentation/en/webdriver/)
- [Mobile Testing Best Practices](https://www.guru99.com/mobile-testing.html)
- [Continuous Integration for Mobile Apps](https://circleci.com/blog/continuous-integration-for-mobile-apps/)
- [Mobile Automation Tools Comparison](https://www.softwaretestinghelp.com/mobile-automation-testing-tools/)
- [Appium Pro - Tips and Tricks](https://appiumpro.com/)
## Running Tests
- Ensure your mobile device or emulator is set up and connected.
- Start the Appium server.
- Execute the test scripts using your preferred method (command line, IDE, etc.).
- Review the test results and logs for analysis.
- Experiment with different test scenarios and configurations to deepen your understanding of mobile automation testing.

Run all tests:

```bash
pytest tests/
```

Run a specific test file:

```bash
pytest tests/test_sample.py
```

Run a specific test case in a file:

```bash
pytest tests/test_sample.py::test_case_name
```

Generate HTML report (requires pytest-html plugin):

```bash
pytest --html=report.html
```

Run tests in parallel (requires pytest-xdist):

```bash
pytest -n 4 tests/
```

Run tests with a specific marker:

```bash
pytest -m marker_name tests/
```

Run tests and capture logs:

```bash
pytest --log-cli-level=INFO tests/
```

Customize pytest with a configuration file (pytest.ini or pyproject.toml).
