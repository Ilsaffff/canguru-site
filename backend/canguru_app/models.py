from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin


class MyUserManager(BaseUserManager):

    def save_user(self, email, username, password, **extra_fields):
        if not email:
            raise ValueError('Вы не ввели электронную почту')
        if not username:
            raise ValueError('Вы не ввели логин')
        user = self.model(
            email=self.normalize_email(email),
            username=username,
            **extra_fields
        )
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_user(self, email, username, password):
        return self.save_user(email, username, password)

    def create_superuser(self, email, username, password):
        return self.save_user(email, username, password, is_staff=True, is_superuser=True)


# class Grade(models.Model):
#     name = models.CharField(max_length=64, unique=True)  # enum

#     def __str__(self):
#         return self.name


class User(AbstractBaseUser, PermissionsMixin):
    id = models.AutoField(primary_key=True, unique=True)
    username = models.CharField(max_length=50, unique=True)
    email = models.CharField(max_length=100, unique=True, null=True)
    is_staff = models.BooleanField(default=False)
    grade = models.ForeignKey(Grade, on_delete=models.CASCADE, null=True)  # enum 
    intial_grade

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username']

    objects = MyUserManager()

    def __str__(self):
        return self.username


class Area(models.Model):
    name = models.CharField(max_length=100, unique=True)

    def __str__(self):
        return self.name


class Module(models.Model):
    name = models.CharField(max_length=100, null=True)

    area = models.ForeignKey(Area, on_delete=models.CASCADE, null=True)
    grade = models.ForeignKey(Grade, on_delete=models.CASCADE, null=True) # enum

    def __str__(self):
        return self.name


# class Tracking(models.Model):
#     modules_junior = models.IntegerField()
#     modules_junior_plus = models.IntegerField()
#     modules_middle = models.IntegerField()
#     modules_middle_plus = models.IntegerField()
#     modules_senior = models.IntegerField()

#     user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
