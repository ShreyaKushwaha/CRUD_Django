from django.db import models

# Create your models here.
class Detail(models.Model):
    name = models.CharField(max_length=200)
    email = models.EmailField(max_length=150,primary_key=True)
    phone = models.IntegerField()
    dob = models.DateField()
    pincode = models.IntegerField()

    def __str__(self):
        return self.email
    
