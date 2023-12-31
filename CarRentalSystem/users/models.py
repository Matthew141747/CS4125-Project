from django.db import models
from django.dispatch import receiver
from django.db.models.signals import post_save
from django.core.mail import send_mail  # Django's built-in function to send emails.
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager

class UserManager(BaseUserManager):
    def create_user(self, email, password=None, **extra_fields):
        if not email:
            raise ValueError('The Email field must be set')
        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, password=None, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)
        return self.create_user(email, password, **extra_fields)

class CustomUser(AbstractBaseUser):
    email = models.EmailField(unique=True, max_length=191)
    accountType = models.CharField(max_length=191)
    date_of_birth = models.DateField(default="2000-01-01")

    objects = UserManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['']

 
    def __str__(self):
        return self.email
    


# The EmailNotificationObserver class functions as the observer.
# It defines the behavior (send_welcome_email) in response to the subject's state change.
class EmailNotificationObserver:
    @staticmethod
    def send_welcome_email(user):
        # This method sends an email, which is the observer's action upon the subject's state change.
        send_mail(
            'Welcome to Car Rental System',
            'Your account has been successfully created.',
            'no-reply@carrentalsystem.com',  # Replace with your actual email
            [user.email],
            fail_silently=False,
        )

# This receiver function connects the User model's post_save signal to the observer's action.
# When a User instance is created (the subject's state changes), this function is called,
# which in turn calls the observer's method to send the email.
@receiver(post_save, sender=CustomUser)
def user_post_save(sender, instance, created, **kwargs):
    if created:
        EmailNotificationObserver.send_welcome_email(instance)


