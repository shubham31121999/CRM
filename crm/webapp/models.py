from django.db import models

# Create your models here.
class ClientRecord(models.Model):
    created_date = models.DateTimeField(auto_now_add=True)

    first_name = models.CharField(max_length = 100)

    last_name = models.CharField(max_length = 100)
    
    email = models.CharField(max_length = 100)

    phone = models.CharField(max_length = 20)

    address = models.CharField(max_length = 100)

    city = models.CharField(max_length = 100)

    state = models.CharField(max_length = 200)

    country = models.CharField(max_length = 200)

    def __str__(self):

        return self.first_name + ' ' + self.last_name



    