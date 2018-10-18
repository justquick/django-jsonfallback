from django.core.serializers.json import DjangoJSONEncoder
from django.db import models
from jsonfallback.fields import FallbackJSONField


class Book(models.Model):
    data = FallbackJSONField(encoder=DjangoJSONEncoder, null=False, default={'foo': 'bar'})

    def __str__(self):
        return str(self.data['title'])
