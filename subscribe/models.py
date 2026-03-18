from django.db import models

# Create your models here.
NEWSLETTER_OPTION=[
    ('w','Weekly'),
    ('M','Monthly'),
    ('Y','Yearly')
]
class Subscribe(models.Model):
    name=models.CharField(max_length=200)
    email=models.EmailField(max_length=200)
    option=models.CharField(max_length=5,choices=NEWSLETTER_OPTION,default='M')