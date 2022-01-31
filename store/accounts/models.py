import email
from xmlrpc.client import TRANSPORT_ERROR
from django.db import models
from django.contrib.auth.models import AbstractBaseUser
from .managers import UserManager

class User (AbstractBaseUser):
    email = models.EmailField(max_length=124, unique=True)
    full_name = models.CharField(max_length=124)
    phone = models.PositiveBigIntegerField(null=True , blank=True , unique=True)
    is_active = models.BooleanField(default=True)
    is_admin = models.BooleanField(default=False)
    objects = UserManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['full_name']

    def __str__(self) -> str:
        return self.email

    def has_perm(self, perm, obj=None):
        return True

    def has_perms(self, perm_list, obj=None):
        return all(self.has_perm(perm, obj) for perm in perm_list)

    def has_module_perms(self, module):
        return True

    @property
    def is_staff(self):
        return self.is_admin
