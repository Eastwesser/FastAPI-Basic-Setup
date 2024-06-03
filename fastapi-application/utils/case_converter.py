def camel_case_to_snake_case(input_str: str) -> str:
    """
    Convert a string from CamelCase to snake_case.

    >>> camel_case_to_snake_case("SomeSDK")
    'some_sdk'
    >>> camel_case_to_snake_case("RServoDrive")
    'r_servo_drive'
    >>> camel_case_to_snake_case("SDKDemo")
    'sdk_demo'
    """
    snake_case_str = ''
    for idx, char in enumerate(input_str):
        if idx > 0 and char.isupper():
            prev_char = input_str[idx - 1]
            if prev_char.islower() or (idx < len(input_str) - 1 and input_str[idx + 1].islower()):
                snake_case_str += '_'
        snake_case_str += char.lower()
    return snake_case_str
