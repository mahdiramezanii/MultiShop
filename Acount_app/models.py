from django.db import models
from django.contrib.auth.models import BaseUserManager, AbstractBaseUser
from django.utils import timezone


class UserManager(BaseUserManager):
    def create_user(self, phone, password=None):

        if not phone:
            raise ValueError('Users must have an phone number')

        user = self.model(
            phone=phone,

        )
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, phone, password=None):
        """
        Creates and saves a superuser with the given email, date of
        birth and password.
        """
        user = self.create_user(
            phone,
            password=password,

        )
        user.is_admin = True
        user.save(using=self._db)
        return user


class User(AbstractBaseUser):
    email = models.EmailField(
        verbose_name='email address',
        max_length=255,
    )
    phone=models.CharField(max_length=20,unique=True)
    is_active = models.BooleanField(default=True)
    is_admin = models.BooleanField(default=False)

    objects = UserManager()

    USERNAME_FIELD = 'phone'


    def __str__(self):
        return self.email

    def has_perm(self, perm, obj=None):
        return True

    def has_module_perms(self, app_label):
        return True

    @property
    def is_staff(self):
        return self.is_admin


class Otc(models.Model):
    token=models.CharField(max_length=250,null=True)
    phone=models.CharField(max_length=11)
    code=models.IntegerField()
    expiration_date=models.DateTimeField(default=timezone.now()+timezone.timedelta(minutes=2))

    def is_expiration_date(self):

        if self.expiration_date > timezone.now():
            return True
        else:
            return False

    def __str__(self):

        return self.phone