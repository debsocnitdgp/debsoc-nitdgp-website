
from django.db import models
# Create your models here.


class Participant(models.Model):
    username = models.CharField(max_length=255, unique=True)
    email = models.EmailField(max_length=255, unique=True)
    phone_no = models.CharField(max_length=20, null=True, blank=True)
    college = models.CharField(max_length=100)
    college_year = models.IntegerField(default='1')
    discord_id=models.CharField(max_length=100,null=True, blank=True)
    prior=models.CharField(max_length=200,null=True, blank=True)
    cv = models.FileField(upload_to='cv/', blank = True, null = True)
    ss = models.ImageField(
        upload_to='payment_ss/', blank=True, null=True)
    is_adj = models.BooleanField(default=False)
    payment_id=models.CharField(max_length=100,null=True)
    is_paid = models.BooleanField(default=False)

    def __str__(self) -> str:
        return self.username


