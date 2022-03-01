from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager 

# thirdly part!!!!!!!
# create a new user 
# create a superuser
class MyAccountManager(BaseUserManager):
    def create_user(self, email, username, password=None):
        if not email:
            raise ValueError("Users must have an email address")
        if not username:
            raise ValueError("Users must have a username")
        user = self.model(
            email = self.normalize_email(email),
            username = username
        )
        user.set_password(password)
        user.save(using=self._db)
        return user
    def create_superuser(self, email, username, password):
        user = self.create_superuser(
            email = self.normalize_email(email),
            username = username,
            password = password
        )
        user.is_admin = True
        user.is_staff = True
        user.is_superuser = True
        user.save(using=self._db)
        return user



def get_profile_image_filepath(self, filename):
    return f'profile_images/{self.pk}/{"prifole_image.png"}'

def get_default_profile_image():
    return "codingwithmitch/logo_1080_1080.png"

# Firstly I created a Account Model from AbstractBaseUser
class Account(AbstractBaseUser):
    email = models.EmailField(verbose_name="Email", max_length=60, unique=True)
    username = models.CharField(max_length=30, unique=True)
    date_joined = models.DateTimeField(verbose_name="Date joined", auto_now_add=True)
    last_login = models.DateTimeField(verbose_name="Last login", auto_now=True)
    # necessary 4 field for AbstractBaseUser
    is_admin = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)
    profile_image = models.ImageField(max_length=255, null=True, blank=True, upload_to=get_profile_image_filepath, default=get_default_profile_image)
    hide_email = models.BooleanField(default=True)

    # fourthly part

    objects = MyAccountManager()
    
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username']

    # secondly
    def __str__(self):
        return self.username
    def get_profile_image_filename(self):
        return str(self.profile_image)[str(self.profile_image).index('profile_images/{self.pk}/'):]
    # classic rule for admin
    def has_perm(self, perm, obj=None):
        return self.is_admin
    def has_module_perms(self, app_label):
        return True
