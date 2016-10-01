from django.core.exceptions import ValidationError


def validate_cpf(value):
    if not value.isdigit():
        raise ValidationError('CPF most contains only digits', 'digits')
    if len(value) != 11:
        raise ValidationError('CPF most have 11 characters', 'length')
