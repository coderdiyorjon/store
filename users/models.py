from django.db import models
from django.core.mail import send_mail

from django.contrib.auth.models import AbstractUser

# Create your models here.

class User(AbstractUser):
    image = models.ImageField(upload_to='users_images', null=True, blank=True)
    is_verified_email=models.BooleanField(default=False)

class EmailVerification(models.Model):
    code=models.UUIDField(unique=True)
    user=models.ForeignKey(to=User, on_delete=models.CASCADE)
    created=models.DateTimeField(auto_now_add=True)
    expiration=models.DateTimeField()

    def __str__(self):
        return f'EmailVerification object for {self.user.email}'

    def send_verification_email(self):
        send_mail(
            'Subject',
            'Message',
            'noreply@example.com',  # from_email
            [self.user.email],  # recipient_list
            fail_silently=False,
        )
