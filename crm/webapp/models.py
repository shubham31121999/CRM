from django.db import models

# Create your models here.
class ClientRecord(models.Model):
    created_date = models.DateTimeField(auto_now_add=True)

    first_name = models.CharField(max_length = 100)

    last_name = models.CharField(max_length = 100)

    