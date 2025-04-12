
https://github.com/user-attachments/assets/b8bd542c-1c7e-4ea2-b13e-e4697e8a9c4b
# LambdaTest Hackathon - Test Automation Solution

This repository contains an automated test solution for the LambdaTest Hackathon challenge. The solution includes test cases for login functionality and JavaScript alerts handling.

## LambdaTest Test ID
Test ID: MGEU1-VZW9D-T181Z-GWTR9

## Demo Video 

https://github.com/user-attachments/assets/32cca012-f749-4a6b-a2db-d1155a877fb2


## Features

- Automated login tests (valid and invalid credentials)
- JavaScript alerts handling (Alert, Confirm, Prompt)
- Parallel test execution
- Rerun failed tests
- HTML test reports
- Secure credential handling
- Cross-browser testing support
- CI/CD Integration with Jenkins

## Prerequisites

- Python 3.8 or higher
- LambdaTest account and credentials
- pip (Python package manager)
- Jenkins (for CI/CD pipeline)

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

### Local Execution
```bash
pytest -v -n auto --reruns 2 --html=report.html
```

### Jenkins Pipeline
1. Create a new pipeline job in Jenkins
2. Point to this repository
3. The Jenkinsfile will automatically:
   - Set up Python virtual environment
   - Install dependencies
   - Run tests on LambdaTest
   - Generate and archive test reports

## Project Structure

```
├── config/
│   └── urls.py           # URL configurations
├── pages/
│   ├── login_page.py     # Login page object
│   └── js_alerts_page.py # JavaScript alerts page object
├── tests/
│   ├── test_login.py     # Login test cases
│   └── test_js_alerts.py # JavaScript alerts test cases
├── utils/
│   └── helpers.py        # Helper functions
├── .env                  # Environment variables (not tracked by git)
├── .env.example          # Example environment variables
├── .gitignore           # Git ignore file
├── Jenkinsfile          # CI/CD pipeline configuration
├── README.md            # Project documentation
└── requirements.txt     # Python dependencies
```

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
- ✅ CI/CD Integration (Jenkins)

## Notes

- Tests are configured to run on LambdaTest's cloud grid
- HTML reports are generated after test execution
- Failed tests are automatically retried twice
- Tests can be run in parallel for faster execution
- Jenkins pipeline automates the entire testing process 
