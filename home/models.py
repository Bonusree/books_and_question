
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin
from django.db import models

class CustomUserManager(BaseUserManager):
    def create_user(self, username, id, session,**extra_fields):
        user = self.model(
            username=username,
            id=id ,
            session=session,
            **extra_fields,
)
        #user.set_unusable_password()
        user.save(using=self._db)
        return user

    def create_superuser(self, username, id,session,**extra_fields):
        user = self.create_user(username=username, id=id, session=session)
        user.is_superuser = True
        user.is_admin=True
        user.save(using=self._db)
        return user

class CustomUser(AbstractBaseUser, PermissionsMixin):
    username = models.CharField(max_length=255, unique=True)
    id = models.CharField(max_length=255,primary_key=True,unique=True)  # Treat the id field as the phone id
    session=models.CharField(max_length=255,unique=False)
    is_staff = models.BooleanField(default=False) 
    is_superuser=models.BooleanField(default=False)
    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = ['id', 'session']

    objects = CustomUserManager()

    def __str__(self):
        return self.username

    def get_full_name(self):
        return self.username

    def get_short_name(self):
        return self.username
