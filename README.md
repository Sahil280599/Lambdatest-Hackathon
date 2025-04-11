# LambdaTest Hackathon - Test Automation Solution

This repository contains an automated test solution for the LambdaTest Hackathon challenge. The solution includes test cases for login functionality and JavaScript alerts handling.

## LambdaTest Test ID
Test ID: XPEQK-2UD96-YBDAK-MCTGW

## Features

- Automated login tests (valid and invalid credentials)
- JavaScript alerts handling (Alert, Confirm, Prompt)
- Parallel test execution
- Rerun failed tests
- HTML test reports
- Secure credential handling
- Cross-browser testing support

## Prerequisites

- Python 3.8 or higher
- LambdaTest account and credentials
- pip (Python package manager)

## Setup

1. Clone this repository:
```bash
git clone <repository-url>
cd <repository-directory>
```

2. Install dependencies:
```bash
pip install -r requirements.txt
```

3. Create a `.env` file in the root directory and add your LambdaTest credentials:
```
LAMBDATEST_USERNAME=your_username
LAMBDATEST_ACCESS_KEY=your_access_key
```

## Running Tests

### Run all tests
```bash
pytest -v -n auto --reruns 2 --html=report.html
```

### Run specific test file
```bash
pytest tests/test_login.py -v
pytest tests/test_js_alerts.py -v
```

### Run with specific browser and platform
```bash
pytest -v --browser=chrome --platform="Windows 10"
```

## Test Structure

- `conftest.py`: Contains shared fixtures and LambdaTest configuration
- `utils/helpers.py`: Contains helper functions for common operations
- `tests/test_login.py`: Login test cases
- `tests/test_js_alerts.py`: JavaScript alerts test cases

## Test Cases

### Login Tests
1. Valid login with correct credentials
2. Invalid login with incorrect credentials

### JavaScript Alerts Tests
1. JS Alert handling
2. JS Confirm handling
3. JS Prompt handling

## Features Implemented

- ✅ Solid framework creation with reusable components
- ✅ Dependency management with requirements.txt
- ✅ Test libraries (Pytest)
- ✅ Parallel test execution (pytest-xdist)
- ✅ Re-running failed cases (pytest-rerunfailures)
- ✅ Clean logs + reports (pytest-html)
- ✅ Secure handling of sensitive data (environment variables)

## Notes

- Tests are configured to run on LambdaTest's cloud grid
- HTML reports are generated after test execution
- Failed tests are automatically retried twice
- Tests can be run in parallel for faster execution 