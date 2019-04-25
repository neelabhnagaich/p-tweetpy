from django.core.exceptions import ValidationError

def validate_content(value):
    if value=='abc':
        raise ValidationError("content cannot be empty")
    return value
