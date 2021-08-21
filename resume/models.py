from django.db import models

# Create your models here.
class Contact(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    email_address = models.EmailField(max_length=100)
    message = models. TextField(max_length=500)


    def __str__(self):
        return self.email_address
