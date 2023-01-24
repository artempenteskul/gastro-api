from django.db import models
from django.contrib.auth.models import AbstractUser
from django.contrib.auth.base_user import BaseUserManager

from phonenumber_field.modelfields import PhoneNumberField


class UserManager(BaseUserManager):
    def create_user(self, email, password, **kwargs):
        if not email:
            raise ValueError('Email should be provided')

        email = self.normalize_email(email)
        new_user = self.model(email=email, **kwargs)
        new_user.set_password(password)
        new_user.save()
        return new_user

    def create_superuser(self, email, password, **kwargs):
        kwargs.setdefault('is_staff', True)
        kwargs.setdefault('is_superuser', True)
        kwargs.setdefault('is_active', True)

        if not kwargs.get('is_staff'):
            raise ValueError('Superuser is_staff property should be True')

        if not kwargs.get('is_superuser'):
            raise ValueError('Superuser is_superuser property should be True')

        if not kwargs.get('is_active'):
            raise ValueError('Superuser is_active property should be True')

        return self.create_user(email, password, **kwargs)


class User(AbstractUser):
    username = models.CharField(max_length=32, unique=True)
    email = models.EmailField(max_length=64, unique=True)
    phone = PhoneNumberField(null=False, unique=True)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username', 'phone']

    def __str__(self):
        return f'{self.username} - {self.email} - {self.phone}'
