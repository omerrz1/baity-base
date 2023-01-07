from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager


class ownerManager(BaseUserManager):
    def create_user(self, username, email, password,phone):
        if not email:
            raise ValueError('please provide an email ! ')
        if not username:
            raise ValueError('')

        user = self.model(email=self.normalize_email(email))
        user.username = username
        user.phone = phone
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email,phone, username, password):
        user = self.create_user(
            email=email,phone=phone, username=username, password=password)
        user.is_staff = True
        user.is_admin = True
        user.save(using=self._db)
        return user

    def create(self, username, password,phone, email):
        user = self.create_user(
            email=email, username=username, phone= phone,password=password)
        user.save(using=self._db)
        return user

# user model


class Owner (AbstractBaseUser):
    username = models.CharField(unique=True, max_length=60)
    email = models.EmailField(verbose_name='email', unique=True)
    phone = models.IntegerField(unique= True)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    is_admin = models.BooleanField(default=False)

    REQUIRED_FIELDS = ['email','phone']
    USERNAME_FIELD = 'username'

    def has_perm(self, perm, obj=None):
        return True

    def has_module_perms(self, app_label):
        return True

    def __str__(self):
        return self.username

    objects = ownerManager()
