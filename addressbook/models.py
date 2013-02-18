from django.db import models


class Address(models.Model):
    name = models.CharField(max_length=50)
    mobile = models.BigIntegerField()
    email = models.EmailField(max_length=75)
    url = models.URLField()


