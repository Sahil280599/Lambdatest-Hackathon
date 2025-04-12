class TestData:
    # Login Credentials
    VALID_USERNAME = "tomsmith"
    VALID_PASSWORD = "SuperSecretPassword!"
    INVALID_USERNAME = "invaliduser"
    INVALID_PASSWORD = "invalidpass"

    # Expected Messages
    LOGIN_SUCCESS_MESSAGE = "You logged into a secure area!"
    LOGIN_ERROR_MESSAGE = "Your username is invalid!"
    JS_ALERT_MESSAGE = "I am a JS Alert"
    JS_CONFIRM_MESSAGE = "I am a JS Confirm"
    JS_PROMPT_MESSAGE = "I am a JS prompt"
    JS_ALERT_SUCCESS = "You successfully clicked an alert"
    JS_CONFIRM_SUCCESS = "You clicked: Ok"
    JS_PROMPT_INPUT = "Hello, LambdaTest!"

    # Test Configuration
    RETRY_COUNT = 2
    PARALLEL_THREADS = "auto"
    WAIT_TIME = 10 