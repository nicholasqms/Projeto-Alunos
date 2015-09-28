from django.forms import IntegerField
from django.core import validators

class CEPField(IntegerField(localize=True))
    default_validators = [