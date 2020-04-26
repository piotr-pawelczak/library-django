from django.core.exceptions import ValidationError


def validate_post_code(value):
    if "gmail.com" not in value:
        raise ValidationError("message")
    return value
