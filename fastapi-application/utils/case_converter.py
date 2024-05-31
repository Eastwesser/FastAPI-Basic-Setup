def camel_case_to_snake_case(input_str: str) -> str:
    """
    >>> camel_case_to_snake_case("SomeSDK")
    'some_sdk'
    >>> camel_case_to_snake_case("RServoDrive")
    'r_servo_drive'
    >>> camel_case_to_snake_case("SDKDemo")
    'sdk_demo'
    """
    if not input_str:
        return ''

    chars = [input_str[0].lower()]
    for char in input_str[1:]:
        if char.isupper():
            chars.append('_')
            chars.append(char.lower())
        else:
            chars.append(char)
    return ''.join(chars)
