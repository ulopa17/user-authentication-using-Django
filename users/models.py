import uuid
from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Profile(models.Model):

    GENDER_CHOICE=[
        ('MALE', 'Male'),
        ('FEMALE', 'Female'),
        ('NO-CHOICE', 'Private')
    ]

    user = models.OneToOneField(User, on_delete=models.CASCADE)
    id = models.UUIDField(default=uuid.uuid4, unique=True, primary_key=True, editable=False)
    first_name = models.CharField(max_length=150)
    last_name = models.CharField(max_length=150)
    e_mail = models.EmailField(max_length=150, blank=True, null=True)
    bio = models.TextField()
    profile_pic = models.ImageField(upload_to='', blank=True, null=True, default='')
    gender = models.CharField(max_length=50, choices=GENDER_CHOICE)


    def __str__(self):
        return str(self.first_name)