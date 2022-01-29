from pickle import TRUE
from django.contrib.auth.models import BaseUserManager


class UserManager(BaseUserManager):
    def create_user(self, email, full_name,phone, password):
        
        if not email:
            raise ValueError('Users must have an email address')
        if not full_name :
            raise ValueError('Users must have an  full_name')
        if not password:
            raise ValueError('Users must have an password')

        user = self.model(email = self.normalize_email(email),full_name = full_name, phone = phone)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, full_name, password):
        user = self.create_user(email = self.normalize_email(email),full_name = full_name, phone=None,
        password= password ,)
        user.is_admin = True
        user.save(using=self._db)
        return user

    